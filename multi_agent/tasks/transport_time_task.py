from crewai import Task
from agents import transport_time_agent

transport_time_task = Task(
    description=(
        "Using the following inputs:\n\n"
        "1. Transport & traveler data:\n"
        "{user_input}\n\n"
        "2. Places to visit (ONLY use these places):\n"
        "{transport_data}\n\n"
        "3. Nearby food & accommodation options by place_id:\n"
        "{food_accommodation_output}\n\n"
        "Create a SINGLE, realistic, time-ordered daily travel plan written in clear, "
        "human-readable bullet points.\n\n"

        "Mandatory flow:\n"
        "- Start from the starting location at the given starting time\n"
        "- FIRST describe intercity travel to the destination city\n"
        "- After arrival, plan travel to the nearest first visiting place\n"
        "- Schedule breakfast BEFORE starting sightseeing\n"
        "- Visit places one by one in an efficient geographic sequence\n"
        "- Insert lunch, evening snacks, and dinner at appropriate times\n"
        "- End the day with accommodation at night\n\n"

        "STRICT rules (must follow):\n"
        "- ONLY use places provided in places_data\n"
        "- Each place_id can be visited ONLY ONCE in the entire itinerary\n"
        "- You MUST explicitly include travel time between every two different locations\n"
        "- If two places are in different towns or cities, allocate realistic road travel time\n"
        "- If one-way travel time exceeds 2 hours, treat it as a half-day or full-day trip\n"
        "- Do NOT schedule sightseeing before or after long-distance travel on the same day\n"
        "- Follow place order sequentially once decided (no jumping back)\n"
        "- Respect opening_timings of places\n"
        "- Roads or streets are NOT sightseeing attractions unless explicitly defined as places\n"
        "- Food suggestions MUST come from food_accommodation_output for the current place_id\n"
        "- Accommodation MUST come from food_accommodation_output for the last visited place_id\n"
        "- Do NOT invent restaurant or hotel names\n"
        "- Maximum meals per day: 1 breakfast, 1 lunch, 1 snack, 1 dinner\n"
        "- If not self-driving, explicitly mention transport mode and major transit points\n"
        "- The final plan MUST be physically possible and time-feasible\n"
        "- If the plan becomes unrealistic, reduce the number of places per day\n"
    ),
    expected_output=(
        "Return the itinerary as clear, chronological bullet points or short paragraphs.\n\n"
        "Formatting rules:\n"
        "- Start each step with the time (e.g., '06:00 AM – 08:30 AM')\n"
        "- Clearly describe travel, food, visits, and rest in sentence form\n"
        "- Mention transport mode when traveling\n"
        "- Mention place name and activity when visiting\n"
        "- Mention restaurant name for meals\n"
        "- Mention hotel name for night stay\n"
        "- Do NOT use JSON, tables, or code blocks\n"
        "- Do NOT include explanations or meta commentary\n"
    ),
    agent=transport_time_agent.transport_time_agent
)
