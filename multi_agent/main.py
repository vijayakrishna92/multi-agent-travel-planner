from crewai import Crew, Process
from agents import researcher_agent, food_accomodation_agent
from tasks import researcher_task, food_accomodation_task
import json
import user_input


def main():
    researcher_crew = Crew(
        agents=[researcher_agent.researcher],
        tasks=[researcher_task.researcher],
        process=Process.sequential,
        verbose=True
    )
    
    raw_places_output = researcher_crew.kickoff(
        inputs= user_input.RESEARCHER_INPUTS
    )
    places_data = json.loads(str(raw_places_output))

    print(places_data)
    
    food_accomodation_crew = Crew(
        agents=[food_accomodation_agent.food_accommodation],
        tasks=[food_accomodation_task.food_accommodation_task],
        process=Process.sequential,
        verbose=True
    )
    raw_food_accomodation_data = food_accomodation_crew.kickoff(
        inputs= {
            "places_data": places_data,
            "food_accommodation_input": user_input.FOOD_ACCOMMODATION_INPUT
                }
    )
    food_accomodation_data = json.loads(str(raw_food_accomodation_data))
    print(food_accomodation_data)
    
    
if __name__ == "__main__":
    main()
    
# litellm, crewai, python-dotenv, pip install -qU langchain-groq


# inputs={
#             'trip_details': {
#                 'starting_point': 'New York, NY',
#                 'destination': 'San Francisco, CA',
                
#                 'transport': {
#                     'mode': 'self-drive',
#                     'electric_vehicle': False, 
#                     'show_charging_stations': False
#                 },
                
#                 'budget': {
#                     'amount': 5000,
#                     'currency': "USD"
#                 },
                
#                 'food_preferences': {
#                     'types': ["Italian", "Asian", "Vegetarian"],
#                     'dietary_restrictions': []
#                 },
                
#                 'duration': {
#                     'number_of_days': 3,
#                     'start_date': "2025-06-15",
#                     'start_time': "09:00",
#                     'end_date': "2025-06-18",
#                     'end_time': "18:00"
#                 },
                
#                 'travelers': {
#                     'total_count': 4,
#                     'breakdown': [
#                         {
#                             'type': "adult",
#                             'count': 2
#                         },
#                         {
#                             'type': "child",
#                             'count': 2
#                         }
#                     ]
#                 },
                
#                 'preferences': {
#                     'site_types': ["historical", "nature", "adventure", "cultural"],
#                     'interests': ["museums", "hiking", "local cuisine", "photography"],
#                     'round_trip': True,  
#                     'accommodation_type': "hotel"
#                 }
#             }
#         }