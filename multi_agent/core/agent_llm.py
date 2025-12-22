# core/llm.py

import os
import getpass
from dotenv import load_dotenv
from langchain_groq import ChatGroq

load_dotenv()

def get_llm(
    model: str = "groq/llama-3.1-8b-instant",
    temperature: float = 0.7
):
    if "GROQ_API_KEY" not in os.environ:
        os.environ["GROQ_API_KEY"] = getpass.getpass(
            "Enter your Groq API key: "
        )

    return ChatGroq(
        model=model,
        api_key=os.environ.get("GROQ_API_KEY"),
        temperature=temperature
    )
