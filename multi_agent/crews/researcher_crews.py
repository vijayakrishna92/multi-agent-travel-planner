from crewai import Crew, Process
from agents import researcher_agent
from tasks import researcher_task
import json
from core import json_toon
import user_input
import re

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
        #inputs = user_input.RESEARCHER_INPUTS
    )
     # Robust JSON parsing
    try:
        # Check if it's already a dict/list (already parsed)
        if isinstance(raw_places_output, (dict, list)):
            places_data = raw_places_output
        else:
            # Convert to string and clean it
            data_str = str(raw_places_output).strip()
            
            # Remove markdown code blocks if present
            if '```json' in data_str:
                # Extract content between ```json and ```
                match = re.search(r'```json\s*(.*?)\s*```', data_str, re.DOTALL)
                if match:
                    data_str = match.group(1).strip()
            elif data_str.startswith('```') and data_str.endswith('```'):
                # Remove generic code blocks
                data_str = data_str[3:-3].strip()
            
            # Handle empty string
            if not data_str:
                raise ValueError("Empty data string received from crew")
            
            # Parse JSON
            places_data = json.loads(data_str)
            
    except json.JSONDecodeError as e:
        print(f"JSON parsing error: {e}")
        print(f"Raw data type: {type(raw_places_output)}")
        print(f"Raw data (first 500 chars): {str(raw_places_output)[:500]}")
        
        # Try to extract JSON from the raw output
        data_str = str(raw_places_output)
        
        # Look for JSON object pattern
        json_match = re.search(r'\{.*\}', data_str, re.DOTALL)
        if json_match:
            try:
                places_data = json.loads(json_match.group(0))
                print("Successfully extracted JSON from raw output")
            except:
                raise ValueError("Could not parse JSON from crew output")
        else:
            raise ValueError("No valid JSON found in crew output")
    
    except Exception as e:
        print(f"Unexpected error: {e}")
        print(f"Raw data: {raw_places_output}")
        raise
    
    # Validate the structure
    if not isinstance(places_data, dict) or 'places' not in places_data:
        raise ValueError("Invalid data structure: expected dict with 'places' key")
    
    # Add sequential IDs
    place_id = 1
    for category in places_data['places'].values():
        if isinstance(category, list):
            for place in category:
                if isinstance(place, dict):
                    place['id'] = place_id
                    place_id += 1
    
    print(places_data)
    
    # Save to JSON file (overwrites if exists)
    output_file = 'researcher_output.json'
    with open(output_file, 'w') as f:
        json.dump(places_data, f, indent=2)
    
    print(f"\nOutput saved to {output_file}")
    
    # Extract id and location
    food_accomodation_ip = []
    for category in places_data['places'].values():
        if isinstance(category, list):
            for place in category:
                if isinstance(place, dict) and 'id' in place and 'location' in place:
                    food_accomodation_ip .append({
                        'id': place['id'],
                        'location': place['location']
                    })
    
    print("\n--- food_accomodation_input ID and Locations ---")
    print(json.dumps(food_accomodation_ip , indent=2))
    
    transportation_timings_ip = []
    for category in places_data['places'].values():
        if isinstance(category, list):
            for place in category:
                if isinstance(place, dict) and 'id' in place and 'location' in place:
                    transportation_timings_ip.append({
                        'id': place['id'],
                        'location': place['location'],
                        'opening_timings':place['opening_timings']
                    })
    
    print("\n--- transportation_timings_ip ID and Locations ---")
    print(json.dumps(transportation_timings_ip, indent=2))
    
    return food_accomodation_ip,transportation_timings_ip