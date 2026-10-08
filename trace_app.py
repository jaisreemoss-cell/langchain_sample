import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage

# Load environment variables from the .env file
load_dotenv()

# Initialize ChatOpenAI (LangSmith picks up the env vars automatically)
chat = ChatOpenAI(model="gpt-4o-mini", temperature=0.7)

# Define at least 3 different prompts
prompts = [
    "Explain quantum computing in one simple sentence.",
    "What are the three macronutrients needed by the human body?",
    "Give me a fun weekend project idea for a software developer."
]

print("--- Running LangChain Prompts ---")
for i, text_prompt in enumerate(prompts, 1):
    message = HumanMessage(content=text_prompt)
    response = chat.invoke([message])
    
    print(f"\n[Prompt {i}]: {text_prompt}")
    print(f"[Response {i}]: {response.content}")

print("\n--- Execution Complete. Check LangSmith! ---")