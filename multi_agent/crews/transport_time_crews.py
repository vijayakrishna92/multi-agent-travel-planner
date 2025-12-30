from crewai import Crew, Process
from agents import transport_time_agent
from tasks import transport_time_task
import json
from core import json_toon
import user_input
import re

def transport_time(transport_data):
    researcher_crew = Crew(
        agents=[transport_time_agent.transport_time_agent],
        tasks=[transport_time_task.transport_time_task],
        process=Process.sequential,
        verbose=True
    )
    with open("food_accomodation_output.json", "r") as f:
        data = json.load(f)
    
    u_input = {'task_details':json_toon.json_toon_converter(user_input.TRANSPORT_TIME_INPUT)}
    transport_data_input = {'places_data':json_toon.json_toon_converter(transport_data)}
    food_accomodation_input = {'food_accomodation':json_toon.json_toon_converter(data)}
    raw_places_output = researcher_crew.kickoff(
        {
            "user_input": u_input,
            "transport_data":transport_data_input,
            "food_accommodation_output":food_accomodation_input,
                }
    )
    
    return str(raw_places_output)