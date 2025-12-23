import requests

def get_search_results(query):
    # Your local SearXNG URL
    url = "http://localhost:8080/search"
    
    # Parameters: q is the query, format is json
    params = {
        'q': query,
        'format': 'json',
        'engines': 'google,duckduckgo,bing' # Specify engines to use
    }
    
    response = requests.get(url, params=params)
    data = response.json()
    
    for result in data.get('results', []):
        print(f"Title: {result['title']}")
        print(f"URL: {result['url']}\n")

get_search_results("tourist places in bengaluru")


# Stop	docker compose stop	Services turn off; state is saved.
# Clean Exit	docker compose down	Services turn off and are removed from memory.
# Resume	docker compose up -d	Everything starts back up in the background.





# # class Solution(object):
# #     def lengthOfLongestSubstring(self, s):
# #         """
# #         :type s: str
# #         :rtype: int
# #         """
# #         l = []
# #         max_v = 0
# #         p=0
# #         for i in range(0,len(s)):
# #             if s[i] not in l:
# #                 l.append(s[i])
# #             else:
                
# #                     max_v = max(max_v, len(l))
# #                     l = [s[i]]
# #                     l.append(s[i])
                    
                
                
# #         print(max(max_v, len(l)))
                
# #             # d v d f
# #             # 0 1 2 3
# #             # ddf
                    
        
                
                
# # solution = Solution()
# # #result = 
# # solution.lengthOfLongestSubstring('dvdf')
# # solution.lengthOfLongestSubstring('bbbbb')
# # solution.lengthOfLongestSubstring(' ')
# # #print(result)

# import requests
# import time

# # -----------------------------
# # CONFIG
# # -----------------------------
# NOMINATIM_URL = "https://nominatim.openstreetmap.org/search"

# OVERPASS_SERVERS = [
#     "https://overpass.kumi.systems/api/interpreter",
#     "https://overpass-api.de/api/interpreter",
#     "https://overpass.nchc.org.tw/api/interpreter"
# ]

# HEADERS = {
#     "User-Agent": "MultiAgentTravelPlanner/1.0 (vijaykrishnavk@gmail.com)",
#     "Accept": "application/json"
# }

# INTEREST_TO_TAGS = {
#     "nature": [
#         ("natural", "beach"),
#     ],
#     "museum": [
#         ("tourism", "museum")
#     ],
#     "historic": [
#         ("historic", None)
#     ]
# }

# # -----------------------------
# # STEP 1: City → Bounding Box
# # -----------------------------
# def get_city_bbox(city):
#     params = {
#         "q": city,
#         "format": "json",
#         "limit": 1,
#         "email": "vijaykrishnavk@gmail.com"
#     }

#     r = requests.get(
#         NOMINATIM_URL,
#         params=params,
#         headers=HEADERS,
#         timeout=30
#     )
#     r.raise_for_status()

#     bbox = r.json()[0]["boundingbox"]
#     lat_min, lat_max, lon_min, lon_max = map(float, bbox)
#     return lat_min, lon_min, lat_max, lon_max


# # -----------------------------
# # STEP 2: Build SAFE Overpass Query
# # -----------------------------
# def build_overpass_query(bbox, interests):
#     lat_min, lon_min, lat_max, lon_max = bbox
#     blocks = []

#     for interest in interests:
#         for key, val in INTEREST_TO_TAGS.get(interest, []):
#             if val:
#                 blocks.append(
#                     f'nwr["{key}"="{val}"]({lat_min},{lon_min},{lat_max},{lon_max});'
#                 )
#             else:
#                 blocks.append(
#                     f'nwr["{key}"]({lat_min},{lon_min},{lat_max},{lon_max});'
#                 )

#     return f"""
#     [out:json][timeout:120];
#     (
#         {''.join(blocks)}
#     );
#     out center tags qt;
#     """


# # -----------------------------
# # STEP 3: Call Overpass (with failover)
# # -----------------------------
# def fetch_overpass(query):
#     for url in OVERPASS_SERVERS:
#         try:
#             r = requests.post(
#                 url,
#                 data=query,
#                 headers=HEADERS,
#                 timeout=180
#             )
#             if r.status_code == 200:
#                 return r.json()
#         except requests.exceptions.RequestException:
#             pass

#     raise Exception("All Overpass servers failed")


# # -----------------------------
# # STEP 4: Fetch Places
# # -----------------------------
# def fetch_places(city, interests):
#     bbox = get_city_bbox(city)
#     time.sleep(1)

#     query = build_overpass_query(bbox, interests)
#     data = fetch_overpass(query)

#     places = []
#     for el in data["elements"]:
#         tags = el.get("tags", {})
#         name = tags.get("name")
#         if not name:
#             continue

#         lat = el.get("lat") or el.get("center", {}).get("lat")
#         lon = el.get("lon") or el.get("center", {}).get("lon")

#         places.append({
#             "name": name,
#             "lat": lat,
#             "lon": lon
#         })

#     return places


# # -----------------------------
# # MAIN
# # -----------------------------
# if __name__ == "__main__":
#     city = "San Francisco"
#     user_interests = ["nature", "museum", "historic"]

#     results = fetch_places(city, user_interests)

#     print(f"\nPlaces to visit in {city}:\n")
#     for i, place in enumerate(results[:20], start=1):
#         print(f"{i}. {place['name']} ({place['lat']}, {place['lon']})")
