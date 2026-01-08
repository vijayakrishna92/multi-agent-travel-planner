from crewai import Task
from agents import researcher_agent

researcher = Task(
    description=(
        "You are provided with structured trip information.\n\n"

        "TRIP DETAILS:\n"
        "- Destination city: {destination}\n"
        "- Trip duration: {number_of_days} days\n"
        "- Trip start date: {start_date}\n"
        "- Total travelers: {total_count}\n"
        "- Preferred site types: {site_types}\n"
        "- Traveler interests: {interests}\n\n"

        "Your task is to research tourist places to visit in and around "
        "{destination} that are suitable for {total_count} travelers over "
        "a {number_of_days}-day trip starting on {start_date}.\n\n"

        "Place selection rules:\n"
        "- ONLY include places located in {destination}\n"
        "- ONLY include places that match the site types in {site_types}\n"
        "- Prefer places that align with traveler interests: {interests}\n"
        "- Exclude places that are closed on {start_date} (due to holidays or maintenance)\n"
        "- If opening timings are unavailable for {start_date}, mark as 'Unknown'\n\n"

        "For EACH site type, find the required number of relevant tourist places.\n\n"

        "For every place, provide:\n"
        "- Name of the place\n"
        "- Complete address (must include {destination}, state, and pincode)\n"
        "- Opening timings (consider {start_date})\n"
        "- Crowd level (Low / Medium / High, based on typical tourist volume)\n\n"

        "Do NOT include food spots, hotels, transportation details, or itinerary planning."
    ),
    expected_output=(
        "Return ONLY a valid JSON object in the following structure:\n\n"
        "{\n"
        "  \"destination\": \"<destination_city>\",\n"
        "  \"places\": {\n"
        "    \"<site_type>\": [\n"
        "      {\n"
        "        \"name\": \"\",\n"
        "        \"location\": \"\",\n"
        "        \"opening_timings\": \"\",\n"
        "        \"crowd_level\": \"Low | Medium | High\"\n"
        "      }\n"
        "    ]\n"
        "  }\n"
        "}\n\n"
        "Rules:\n"
        "- Use ONLY site types from {site_types}{interests}\n"
        "- Each place MUST include crowd_level\n"
        "- Output JSON only\n"
        "- No additional text"
    ),
    agent=researcher_agent.researcher
)