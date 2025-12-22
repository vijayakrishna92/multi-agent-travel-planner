from crewai import Task
from agents import researcher_agent
researcher = Task(
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
                    "  \"places\": {\n"
                    "    \"<category_name>\": [\n"
                    "      {\n"
                    "        \"name\": \"<place_name>\",\n"
                    "        \"location\": \"<location>\",\n"
                    "        \"opening_timings\": \"<opening_time>\"\n"
                    "      }\n"
                    "    ]\n"
                    "  }\n"
                    "}\n\n"
                    "Rules:\n"
                    "- Category names must match site types (nature, temple, historical, cultural, etc.)\n"
                    "- Each category must contain 1 or more places\n"
                    "- Output JSON only\n"
                    "- No markdown\n"
                    "- No explanations\n"
                    "- Follow the structure exactly"
                ),
    agent=researcher_agent.researcher
)