import json
from geopy.geocoders import Nominatim
from ortools.constraint_solver import routing_enums_pb2
from ortools.constraint_solver import pywrapcp

# -----------------------------
# 1️⃣ Load your JSON file
# -----------------------------
with open('places.json', 'r') as f:
    places_data = json.load(f)['places']

# Flatten all places into a single list
all_places = []
for category in places_data:
    for place in places_data[category]:
        all_places.append({
            'name': place['name'],
            'address': place['location'],
            'category': category,  # keep category info
            'opening_timings': place.get('opening_timings', ''),
            'nearby_food': place.get('nearby_food', []),
            'nearby_accommodation': place.get('nearby_accommodation', [])
        })

# -----------------------------
# 2️⃣ Geocode addresses (free)
# -----------------------------
geolocator = Nominatim(user_agent="route_optimizer")
coordinates = []
for place in all_places:
    location = geolocator.geocode(place['address'])
    if location:
        coordinates.append((location.latitude, location.longitude))
    else:
        coordinates.append((0,0))  # fallback

# -----------------------------
# 3️⃣ Compute distance matrix
# -----------------------------
def compute_distance_matrix(coords):
    import math
    n = len(coords)
    matrix = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i == j:
                matrix[i][j] = 0
            else:
                # Euclidean distance approximation
                matrix[i][j] = math.sqrt((coords[i][0]-coords[j][0])**2 + (coords[i][1]-coords[j][1])**2)
    return matrix

distance_matrix = compute_distance_matrix(coordinates)

# -----------------------------
# 4️⃣ Solve TSP using OR-Tools
# -----------------------------
manager = pywrapcp.RoutingIndexManager(len(distance_matrix), 1, 0)
routing = pywrapcp.RoutingModel(manager)

def distance_callback(from_index, to_index):
    from_node = manager.IndexToNode(from_index)
    to_node = manager.IndexToNode(to_index)
    return int(distance_matrix[from_node][to_node]*1000000)  # scale to int

transit_callback_index = routing.RegisterTransitCallback(distance_callback)
routing.SetArcCostEvaluatorOfAllVehicles(transit_callback_index)

search_parameters = pywrapcp.DefaultRoutingSearchParameters()
search_parameters.first_solution_strategy = (
    routing_enums_pb2.FirstSolutionStrategy.PATH_CHEAPEST_ARC)

solution = routing.SolveWithParameters(search_parameters)

# -----------------------------
# 5️⃣ Extract full info in optimized order
# -----------------------------
optimized_order = []
if solution:
    index = routing.Start(0)
    while not routing.IsEnd(index):
        node = manager.IndexToNode(index)
        place_info = all_places[node].copy()
        place_info['latitude'] = coordinates[node][0]
        place_info['longitude'] = coordinates[node][1]
        optimized_order.append(place_info)
        index = solution.Value(routing.NextVar(index))

# -----------------------------
# 6️⃣ Save optimized route to JSON
# -----------------------------
with open('optimized_route.json', 'w') as f:
    json.dump({"optimized_places": optimized_order}, f, indent=4)

print("Optimized route saved to optimized_route.json")
