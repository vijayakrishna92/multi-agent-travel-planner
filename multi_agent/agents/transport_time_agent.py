# places, budjet, people, if 1 pm food, if night accoomdation. id
from crewai import Agent
from core.agent_llm import get_llm

transport_time_agent = Agent(
    role="ItinerarySequencingAgent",
    goal="Produce a single, time-ordered daily itinerary by sequencing places "
        "based on timing constraints. Start with morning activities (e.g., breakfast), "
        "followed by visits, meals, and rest periods, ensuring each place fits its "
        "appropriate time window and the overall schedule is feasible.",
    backstory=(
        "You act as a personal travel secretary who plans what comes next throughout the day. "
        "You determine the correct order of places, assign realistic time slots, "
        "and specify transport between consecutive locations when the user is not "
        "self-driving."
    ),
    llm=get_llm(),
    verbose = True
)