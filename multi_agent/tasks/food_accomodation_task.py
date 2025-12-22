from crewai import Task
from agents import food_accomodation_agent
food_accommodation_task = Task(
    description=(
        "Using the following places data:\n\n"
        "{places_data}\n\n"
        "And the user food & accommodation preferences:\n\n"
        "{food_accommodation_input}\n\n"
        "For EACH place:\n"
        "- Provide AT MOST 2 nearby food options\n"
        "- Provide AT MOST 2 nearby accommodations\n"
        "- Do NOT exceed these limits\n"
        "- Prefer closer and better-matching options\n"
    ),
    expected_output=(
        "Return ONLY a properly formatted JSON object...\n"
        "(your strict schema here)"
    ),
    agent=food_accomodation_agent.food_accommodation
)