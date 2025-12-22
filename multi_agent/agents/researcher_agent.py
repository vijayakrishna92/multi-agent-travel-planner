from crewai import Agent
from core.agent_llm import get_llm

researcher = Agent(
    role="senior travel researcher",
    goal="design a personalized trip plan based on structured trip details",
    backstory=(
        "You are an expert travel researcher who converts structured trip inputs "
        "into clear, visual-friendly itinerary data."
    ),
    llm=get_llm(),
    verbose = True
)