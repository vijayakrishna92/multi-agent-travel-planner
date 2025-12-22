RESEARCHER_INPUTS={
            'trip_details': {
                'destination': 'San Francisco, CA',
                
                'budget': {
                    'amount': 5000,
                    'currency': "USD"
                },
                
                'duration': {
                    'number_of_days': 3,
                    'start_date': "2025-06-15",
                    'start_time': "09:00",
                    'end_date': "2025-06-18",
                    'end_time': "18:00"
                },
                
                'travelers': {
                    'total_count': 4,
                    'breakdown': [
                        {
                            'type': "adult",
                            'count': 2
                        },
                        {
                            'type': "child",
                            'count': 2
                        }
                    ]
                },
                
                'preferences': {
                    'site_types': ["historical", "nature", "adventure", "cultural"],
                    'interests': ["museums", "hiking", "local cuisine", "photography"],
                }
            }
        }

FOOD_ACCOMMODATION_INPUT = {
    "food_preferences": {
        "types": ["Italian", "Asian", "Vegetarian"],
        "dietary_restrictions": ["no-alcohol"],
        "budget_per_meal": {
            "min": 10,
            "max": 40,
            "currency": "USD"
        }
    },

    "accommodation_preferences": {
        "type": "hotel",                
        "star_rating_min": 3,
        "budget_per_night": {
            "min": 100,
            "max": 250,
            "currency": "USD"
        },
        "child_friendly": True,
        "amenities": ["wifi", "parking"]
    },

    "distance_constraints": {
        "max_distance_km": 3
    }
}