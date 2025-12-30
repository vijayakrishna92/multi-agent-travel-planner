from crewai import Crew,Process
from agents import food_accomodation_agent
from tasks import food_accomodation_task
from core import json_toon
import json
import user_input
import re

def foods_accomodations(places_data):   
    food_accomodation_crew = Crew(
        agents=[food_accomodation_agent.food_accommodation],
        tasks=[food_accomodation_task.food_accommodation_task],
        process=Process.sequential,
        verbose=True
    )
    p_input = {'places_data':json_toon.json_toon_converter(places_data)}
    f_a_input = {'food_accommodation_input':json_toon.json_toon_converter(user_input.FOOD_ACCOMMODATION_INPUT)}
    raw_food_accomodation_data = food_accomodation_crew.kickoff(
        inputs= {
            "places_data": p_input,
            "food_accommodation_input":f_a_input
                }
        # inputs = {
        #     "places_data": places_data,
        #     "food_accommodation_input": user_input.FOOD_ACCOMMODATION_INPUT
        #         }
    )
        # Robust JSON parsing
    try:
        # Check if it's already a dict/list (already parsed)
        if isinstance(raw_food_accomodation_data, (dict, list)):
            food_accomodation_data = raw_food_accomodation_data
        else:
            # Convert to string and clean it
            data_str = str(raw_food_accomodation_data).strip()
            
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
            food_accomodation_data = json.loads(data_str)
            
    except json.JSONDecodeError as e:
        print(f"JSON parsing error: {e}")
        print(f"Raw data type: {type(raw_food_accomodation_data)}")
        print(f"Raw data (first 500 chars): {str(raw_food_accomodation_data)[:500]}")
        
        # Try to extract JSON from the raw output
        data_str = str(raw_food_accomodation_data)
        
        # Look for JSON object pattern
        json_match = re.search(r'\{.*\}', data_str, re.DOTALL)
        if json_match:
            try:
                food_accomodation_data = json.loads(json_match.group(0))
                print("Successfully extracted JSON from raw output")
            except:
                raise ValueError("Could not parse JSON from crew output")
        else:
            raise ValueError("No valid JSON found in crew output")
    
    except Exception as e:
        print(f"Unexpected error: {e}")
        print(f"Raw data: {raw_food_accomodation_data}")
        raise
    
    # Print and save
    print(food_accomodation_data)
    
    with open('food_accomodation_output.json', 'w') as f:
        json.dump(food_accomodation_data, f, indent=4)
    