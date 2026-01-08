from crewai import Agent
from core.agent_llm import get_llm

researcher = Agent(
    role="destination research specialist",
    goal=(
        "Research destination-specific places strictly based on user preferences "
        "and return structured, machine-readable location data"
    ),
    backstory=(
        "You are an expert travel researcher who understands user intent, "
        "filters attractions based on preferences, and outputs clean structured data "
        "for downstream itinerary planning agents."
    ),
    llm=get_llm(),
    verbose = True
)