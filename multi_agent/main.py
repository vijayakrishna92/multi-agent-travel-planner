from crewai import Crew, Agent, Task, Process, LLM
import os

llm = LLM(model='ollama/llama3-groq-tool-use:8b', temperature=0.7)

researcher = Agent(
    role = 'senior researcher',
    goal = 'undercover ground breaking techologies',
    backstory = 'driven by curiosity, you explore and share the latest innovation',
    llm = llm
)

researcher_task = Task(
    description = 'identify the next big trend in the {topic}',
    expected_output = 'a paragraph report on emerging {topic} technologies',
    agent = researcher
)

def main():
    crew = Crew(
        agents = [researcher],
        tasks = [researcher_task],
        process = Process.sequential,
        verbose = True
    )
    
    result = crew.kickoff(
        inputs = {'topic':'ai agents'}
    )
    print(result)
    
if __name__ == "__main__":
    main()
    
# litellm, crewai, crewai tool