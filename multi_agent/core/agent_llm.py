# core/llm.py

import os
import getpass
from dotenv import load_dotenv
from langchain_groq import ChatGroq
#from langchain_openai import ChatOpenAI

load_dotenv()

def get_llm(
    model: str = "groq/llama-3.1-8b-instant",
    temperature: float = 0.1
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

# openai

# def get_llm(
#     model: str = "gpt model name goes here",
#     temperature: float = 0.1 # range from 0.1 to 0.9 higher more creative
# ):
#     if "OPENAI_API_KEY" not in os.environ:
#         os.environ["OPENAI_API_KEY"] = getpass.getpass(
#             "Enter your openai API key: "
#         )

#     return ChatOpenAI(
#         model=model,
#         api_key=os.environ.get("OPENAI_API_KEY"),
#         temperature=temperature
#     )
