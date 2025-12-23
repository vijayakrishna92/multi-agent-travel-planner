from crewai import Crew,Process
from agents import food_accomodation_agent
from tasks import food_accomodation_task
import json
import user_input

def foods_accomodations(places_data):   
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
    with open('places.json', 'w') as f:
        json.dump(food_accomodation_data, f, indent=4)  # indent=4 makes it readable

    print("Saved to places.json")