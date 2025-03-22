import os
from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
from langchain_core.messages import HumanMessage, SystemMessage

# Load environment variables from a .env file
load_dotenv()

"""
In LangChain, the message interface is used to structure and manage the flow of messages between the user and the chat model. 
This interface helps in defining different types of messages that can be sent to the model, such as system messages and human messages.

Message Interface
The message interface in LangChain is designed to handle different types of messages that can be exchanged during a conversation. 
It provides a way to encapsulate the content and type of each message, making it easier to manage and process them.

SystemMessage
A SystemMessage is used to provide instructions or context to the chat model. 
These messages are typically used to set the stage for the conversation or to give the model specific guidelines on how to respond.

HumanMessage
A HumanMessage represents a message from the user. 
These messages are the actual inputs or queries that the user wants the chat model to respond to.

"""
# Initialize the chat model
model = init_chat_model("gpt-4o-mini", model_provider="openai")

messages = [
    SystemMessage("Translate the following from English into Italian"),
    HumanMessage("hi!"),
]

print(model.invoke(messages))