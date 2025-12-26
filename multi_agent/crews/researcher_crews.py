from crewai import Crew, Process
from agents import researcher_agent
from tasks import researcher_task
import json
from core import json_toon
import user_input

def researchers():
    researcher_crew = Crew(
        agents=[researcher_agent.researcher],
        tasks=[researcher_task.researcher],
        process=Process.sequential,
        verbose=True
    )
    u_input = {'task_details':json_toon.json_toon_converter(user_input.RESEARCHER_INPUTS)}
    raw_places_output = researcher_crew.kickoff(
        inputs=u_input
    )
    places_data = json.loads(str(raw_places_output))
    
    # Add sequential IDs
    place_id = 1
    for category in places_data['places'].values():
        for place in category:
            place['id'] = place_id
            place_id += 1

    print(places_data)
    
    # Save to JSON file (overwrites if exists)
    output_file = 'places_output.json'
    with open(output_file, 'w') as f:
        json.dump(places_data, f, indent=2)
    
    print(f"\nOutput saved to {output_file}")
    
    # Extract id and location
    extracted = []
    for category in places_data['places'].values():
        for place in category:
            extracted.append({
                'id': place['id'],
                'location': place['location']
            })
    
    print("\n--- Extracted ID and Locations ---")
    print(extracted)
    
    return extracted