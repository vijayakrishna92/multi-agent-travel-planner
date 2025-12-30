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
         "Return ONLY a valid JSON object with the following exact structure:\n\n"
        "{\n"
        '  "<place_id>": {\n'
        '    "food_options": [\n'
        "      {\n"
        '        "name": string,\n'
        '        "type": string,\n'
        '        "dietary_restrictions": string,\n'
        '        "budget": string,\n'
        '        "distance": string\n'
        "      }\n"
        "    ],\n"
        '    "accommodations": [\n'
        "      {\n"
        '        "name": string,\n'
        '        "type": string,\n'
        '        "star_rating": string,\n'
        '        "budget": string,\n'
        '        "child_friendly": string,\n'
        '        "amenities": string\n'
        "      }\n"
        "    ]\n"
        "  }\n"
        "}\n\n"
        "Rules:\n"
        "- One top-level key per place_id from places_data\n"
        "- food_options MUST contain 0–2 items\n"
        "- accommodations MUST contain 0–2 items\n"
        "- Do NOT add extra keys\n"
        "- Do NOT include explanations, comments, or markdown\n"
        "- Output JSON only"
    ),
    agent=food_accomodation_agent.food_accommodation
)