from crews import researcher_crews, food_accomodation_crews,transport_time_crews

def main():
    places_data,transport_data = researcher_crews.researchers()
    food_accomodation_crews.foods_accomodations(places_data)
    final_output = transport_time_crews.transport_time(transport_data)
    print(final_output)
    
    
if __name__ == "__main__":
    main()
    
# litellm, crewai, python-dotenv, pip install -qU langchain-groq pip install geopy  pip install ortools pip install py-toon-format
