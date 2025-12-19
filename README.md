# 🌍 CrewAI Trip Planner

> An intelligent, multi-agent travel planning system powered by CrewAI and Ollama

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![CrewAI](https://img.shields.io/badge/CrewAI-latest-green.svg)](https://github.com/joaomdmoura/crewAI)
[![Ollama](https://img.shields.io/badge/Ollama-Llama-red.svg)](https://ollama.ai/)

## 📖 Overview

An open-source trip planner that uses specialized AI agents to collaborate and create personalized travel itineraries. Built with **local LLMs using Ollama** - no API costs, complete privacy, and runs entirely on your machine!

Each agent handles a specific aspect of trip planning, working together to optimize your journey.

## ✨ Why This Project?

- 🔒 **100% Local & Private** - Your travel data never leaves your machine
- 💰 **Zero API Costs** - Uses free, open-source Llama models via Ollama
- 🤖 **Multi-Agent Intelligence** - Specialized agents collaborate for better results
- 🎯 **Fully Customizable** - Modify agents and workflows to your needs
- 📚 **Learning Resource** - Great for understanding multi-agent systems

## 🤖 Agent Architecture

- **Manager Agent**: Orchestrates all agents and ensures quality control
- **Budget Agent**: Tracks expenses and allocates resources across categories
- **Weather Agent**: Provides forecasts and weather-based recommendations
- **Research Agent**: Discovers attractions based on your interests
- **Transport Agent**: Plans all transportation logistics
- **Accommodation Agent**: Finds suitable stays within budget
- **Food Agent**: Recommends dining options matching preferences
- **Itinerary Planner Agent**: Synthesizes everything into a complete day-by-day schedule

## 🚀 Features

- ✅ Multi-agent collaboration using CrewAI framework
- ✅ Budget-aware planning with real-time tracking
- ✅ Weather-optimized scheduling
- ✅ Multiple transport options coordination
- ✅ Personalized recommendations based on interests
- ✅ Complete itinerary generation with timing
- ✅ Runs 100% locally with Ollama (Llama models)
- ✅ No API keys or internet required for LLM inference

## 🛠️ Tech Stack

- **Python 3.8+**
- **CrewAI** - Multi-agent orchestration framework
- **Ollama** - Local LLM runtime
- **Llama 3.2** (or Llama 3.1) - Open-source language model
- **LangChain** - LLM integration
- Weather API integration (optional)

## 📦 Installation

### Prerequisites

1. **Install Ollama**
```bash
   # macOS/Linux
   curl -fsSL https://ollama.ai/install.sh | sh
   
   # Windows: Download from https://ollama.ai/download
```

2. **Pull Llama model**
```bash
   # Recommended: Llama 3.2 (3B - faster) or Llama 3.1 (8B - more capable)
   ollama pull llama3.2
   
   # Or for better performance (requires more RAM):
   ollama pull llama3.1:8b
```

3. **Verify Ollama is running**
```bash
   ollama list
```

### Install Trip Planner
```bash
# Clone the repository
git clone https://github.com/yourusername/crewai-trip-planner.git
cd crewai-trip-planner

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### Requirements.txt
```txt
crewai>=0.28.0
crewai-tools>=0.2.0
langchain>=0.1.0
langchain-community>=0.0.20
python-dotenv>=1.0.0
requests>=2.31.0
```

## 🎯 Usage

### Basic Example
```python
from crewai import Crew, Agent, Task, Process
from langchain_community.llms import Ollama

# Initialize Ollama with Llama
llm = Ollama(model="llama3.2")

# Define your trip
trip_details = {
    "start_location": "Bangalore",
    "destination": "Mysore",
    "interests": ["palace", "zoo", "temple", "museum"],
    "days": 2,
    "start_day": "Saturday",
    "budget": 15000,
    "num_people": 3,
    "transport_pref": "train and scooter"
}

# Create and run crew (implementation in main.py)
crew = create_trip_planning_crew(trip_details, llm)
result = crew.kickoff()

print(result)
```

### Run the Application
```bash
python main.py
```

## 📁 Project Structure
```
crewai-trip-planner/
├── agents/
│   ├── manager_agent.py
│   ├── budget_agent.py
│   ├── weather_agent.py
│   ├── research_agent.py
│   ├── transport_agent.py
│   ├── accommodation_agent.py
│   ├── food_agent.py
│   └── itinerary_agent.py
├── tasks/
│   └── task_definitions.py
├── tools/
│   ├── weather_tool.py
│   └── search_tool.py
├── config/
│   └── config.yaml
├── main.py
├── requirements.txt
├── .env.example
├── .gitignore
└── README.md
```

## ⚙️ Configuration

Create a `.env` file (optional, for external APIs):
```bash
# Optional: Weather API (free tier available)
WEATHER_API_KEY=your_weather_api_key

# Ollama settings (defaults shown)
OLLAMA_HOST=http://localhost:11434
OLLAMA_MODEL=llama3.2
```

## 🎨 Customization

### Use Different Llama Models
```python
# Faster, less capable (3B parameters)
llm = Ollama(model="llama3.2")

# More capable (8B parameters)
llm = Ollama(model="llama3.1:8b")

# Most capable (70B parameters - requires powerful GPU)
llm = Ollama(model="llama3.1:70b")
```

### Add Custom Agents

Extend the framework by adding your own specialized agents in the `agents/` directory.

## 🔧 Troubleshooting

**Ollama not responding?**
```bash
# Check if Ollama is running
ollama serve

# Test the model
ollama run llama3.2 "Hello"
```

**Out of memory?**
- Use smaller model: `llama3.2` (3B)
- Reduce context window in agent definitions
- Close other applications

**Slow performance?**
- Use GPU acceleration if available
- Switch to smaller model
- Reduce number of parallel agents

## 🤝 Contributing

Contributions are welcome! This is an open-source project built for the community.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

### Areas for Contribution
- 🌟 New agent types (e.g., Activity Booking Agent, Review Agent)
- 🔧 Performance optimizations
- 🌍 Multi-language support
- 📱 Web/mobile interface
- 🧪 Test coverage
- 📖 Documentation improvements

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Built with [CrewAI](https://github.com/joaomdmoura/crewAI) framework
- Powered by [Ollama](https://ollama.ai/) and [Llama](https://llama.meta.com/) models
- Inspired by the need for privacy-focused, cost-free AI travel planning

## 📞 Contact

Questions? Suggestions? Open an issue or reach out!

---

**⭐ If you find this project helpful, please give it a star!**
