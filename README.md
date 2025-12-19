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
