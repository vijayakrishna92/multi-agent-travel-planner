from crewai import Task
from agents import researcher_agent

researcher = Task(
    description=(
        "Research suitable places and attractions "
        "using the following trip details:\n\n"
        "{task_details}\n\n"
        "IMPORTANT: Only research places that match the site_types specified in preferences. "
        "The site_types are the categories you must use. "
        "For each site_type in the preferences, find 2 relevant places with complete addresses."
    ),
    expected_output=(
        "Return ONLY a properly formatted JSON object in the following structure:\n\n"
        "{\n"
        "  \"places\": {\n"
        "    \"<site_type_from_preferences>\": [\n"
        "      {\n"
        "        \"name\": \"<place_name>\",\n"
        "        \"location\": \"<full_address_with_city_state_pincode>\",\n"
        "        \"opening_timings\": \"<opening_time>\"\n"
        "      }\n"
        "    ]\n"
        "  }\n"
        "}\n\n"
        "Rules:\n"
        "- Use ONLY the site_types from preferences as category names (e.g., if preferences has ['historical', 'nature'], use only those)\n"
        "- Each category must contain 2 places\n"
        "- Provide complete address with city, state, and pincode for location field\n"
        "- Output JSON only\n"
        "- No markdown formatting (no ```json or ```)\n"
        "- No explanations or additional text\n"
        "- Do NOT include food, accommodations, or any sections not in site_types\n"
        "- Follow the structure exactly"
    ),
    agent=researcher_agent.researcher
)