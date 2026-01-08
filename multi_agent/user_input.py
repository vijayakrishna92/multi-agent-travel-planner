RESEARCHER_INPUTS={
            'trip_details': {
                'destination': 'Mysore',
                
                'duration': {
                    'number_of_days': 2,
                    'start_date': "2025-06-15",
                    'start_time': "06:00",
                    'end_date': "2025-06-16",
                    'end_time': "18:00"
                },
                
                'travelers': {
                    'total_count': 2,
                    'breakdown': [
                        {
                            'type': "adult",
                            'count': 2
                        },
                        {
                            'type': "child",
                            'count': 0
                        }
                    ]
                },
                
                'preferences': {
                    'site_types': ["historical", "nature", "cultural"],
                    'interests': ["hiking", "local cuisine", "photography"],
                }
            }
        }

FOOD_ACCOMMODATION_INPUT = {
    "food_preferences": {
        "types": ["South indian", "Vegetarian"],
        "dietary_restrictions": ["no-alcohol"],
        "budget_per_meal": {
            "min": 50,
            "max": 400,
            "currency": "INR"
        }
    },

    "accommodation_preferences": {
        "type": "hotel",                
        "star_rating_min": 3,
        "budget_per_night": {
            "min": 500,
            "max": 1000,
            "currency": "INR"
        },
        "child_friendly": True,
        "amenities": ["wifi", "parking"]
    },

    "distance_constraints": {
        "max_distance_km": 3
    }
}
TRANSPORT_TIME_INPUT = {
    'travelers': {
                    'total_count': 2,
                    'breakdown': [
                        {
                            'type': "adult",
                            'count': 2
                        },
                        {
                            'type': "child",
                            'count': 0
                        }
                    ]
                },
    'budget': {
                    'amount': 5000,
                    'currency': "INR"
                },
    
    'starting point':'Bengaluru',
    'destination': 'Mysore',
    'starting time':'6:00 am',
    'duration': {
                    'number_of_days': 4,
                    'start_date': "2025-06-15",
                    'start_time': "09:00",
                    'end_date': "2025-06-18",
                    'end_time': "18:00"
                },
}