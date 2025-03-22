import os
from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage

# Load environment variables from a .env file
load_dotenv()

# Initialize the chat model
model = init_chat_model("gpt-4o-mini", model_provider="openai")

print(model.invoke([
        HumanMessage(content="Hi! I'm Bob"),
        AIMessage(content="Hello Bob! How can I assist you today?"),
        HumanMessage(content="What's my name?"),
    ]))






