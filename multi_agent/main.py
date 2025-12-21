from crewai import Crew, Agent, Task, Process, LLM
import os
import tiktoken
import json

encoding = tiktoken.get_encoding("cl100k_base")

def count_tokens(text: str) -> int:
    return len(encoding.encode(text))

llm = LLM(model='ollama/gemma3:1b', temperature=0.7)

researcher = Agent(
    role="senior travel researcher",
    goal="design a personalized trip plan based on structured trip details",
    backstory=(
        "You are an expert travel researcher who converts structured trip inputs "
        "into clear, visual-friendly itinerary data."
    ),
    llm=llm
)

researcher_task = Task(
    description=(
        "Research suitable places, attractions, food options, and accommodations "
        "using the following trip details:\n\n"
        "{trip_details}\n\n"
        "Base your research on destination, duration, budget, traveler count, "
        "food preferences, and site interests."
    ),
    expected_output=(
            "Return ONLY a properly formatted JSON object in the following structure:\n\n"
    "{\n"
    "  \"places\": [\n"
    "    {\n"
    "      \"name\": \"<place_name>\",\n"
    "      \"location\": \"<location>\",\n"
    "      \"opening_timings\": \"<opening_time>\",\n"
    "      \"food\": [\n"
    "        {\n"
    "          \"name\": \"<food_place_name>\",\n"
    "          \"location\": \"<food_location>\"\n"
    "        }\n"
    "      ],\n"
    "      \"accommodation\": [\n"
    "        {\n"
    "          \"name\": \"<hotel_name>\",\n"
    "          \"location\": \"<hotel_location>\",\n"
    "          \"budget\": \"<budget_amount>\"\n"
    "        }\n"
    "      ]\n"
    "    }\n"
    "  ]\n"
    "}\n\n"
    "Rules:\n"
    "- Output JSON only\n"
    "- No markdown\n"
    "- No explanations\n"
    "- Follow the structure exactly"
    ),
    agent=researcher
)
trip_details = {
    'starting_point': 'New York, NY',
    'destination': 'San Francisco, CA',
    # rest of your dict...
}



def main():
    crew = Crew(
        agents=[researcher],
        tasks=[researcher_task],
        process=Process.sequential,
        verbose=True
    )
    prompt_text = f"""
    Role: {researcher.role}
    Goal: {researcher.goal}
    Backstory: {researcher.backstory}

    Task:
    {researcher_task.description}

    Input:
    {json.dumps(trip_details)}
    """

    input_tokens = count_tokens(prompt_text)
    print("Estimated input tokens:", input_tokens)
    
    result = crew.kickoff(
        inputs={
            'trip_details': {
                'starting_point': 'New York, NY',
                'destination': 'San Francisco, CA',
                
                'transport': {
                    'mode': 'self-drive',
                    'electric_vehicle': False, 
                    'show_charging_stations': False
                },
                
                'budget': {
                    'amount': 5000,
                    'currency': "USD"
                },
                
                'food_preferences': {
                    'types': ["Italian", "Asian", "Vegetarian"],
                    'dietary_restrictions': []
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
                    'round_trip': True,  
                    'accommodation_type': "hotel"
                }
            }
        }
    )
    result_text = str(result)
    completion_tokens = count_tokens(result_text)

    print("Estimated completion tokens:", completion_tokens)
    print("Estimated total tokens:", input_tokens + completion_tokens)
    print(result)
    
if __name__ == "__main__":
    main()
    
# litellm, crewai, crewai tool