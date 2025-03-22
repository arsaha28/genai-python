import os
from dotenv import load_dotenv
from langchain.chat_models import init_chat_model

# Load environment variables from a .env file
load_dotenv()

"""
In the context of LangChain, a chat model is an abstraction that represents a conversational AI model capable of generating responses to user inputs. 
LangChain provides a framework to interact with various chat models, such as those provided by OpenAI, by initializing and invoking them.
In the provided code, the init_chat_model function is used to initialize a chat model with the specified parameters ("gpt-4o-mini" and model_provider="openai"). 
The model.invoke method is then used to send a prompt ("Where is Paris?") to the chat model and print the response.

Here's a brief breakdown of the key components:
Chat Model: An AI model designed to handle conversational input and output.
Runnable: In LangChain, a runnable refers to any component or function that can be executed, such as invoking a chat model to generate a response.

The code snippet demonstrates initializing a chat model and invoking it to get a response to a specific query.

"""
# Initialize the chat model
model = init_chat_model("phi3", model_provider="ollama")

print(model.invoke("Where is Paris?"))



