import os
from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
from langchain_core.prompts import ChatPromptTemplate

# Load environment variables from a .env file
load_dotenv()
"""
ChatPromptTemplate is a utility that helps in creating structured prompts for chat models. 
It allows you to define templates for different types of messages (e.g., system messages, user messages) and then generate complete prompts by filling in the placeholders with actual values.

Explanation of ChatPromptTemplate
ChatPromptTemplate is used to create a template for chat prompts that can include both system and user messages. This helps in organizing and managing the conversation flow more effectively.

Key Components
Template Definition:
You define a template for system messages and user messages. 
These templates can include placeholders that will be filled with actual values when the prompt is generated.

Creating the Template:
The ChatPromptTemplate.from_messages method is used to create a ChatPromptTemplate from a list of message tuples. 
Each tuple consists of a message type (e.g., "system", "user") and the corresponding template string.
Generating the Prompt:
The invoke method of ChatPromptTemplate is used to generate the final prompt by filling in the placeholders with actual values.

"""
system_template = "Translate the following from English into {language}"

prompt_template = ChatPromptTemplate.from_messages(
    [
        ("system", system_template), 
        ("user", "{text}")
    ]
)
# Initialize the chat model
model = init_chat_model("gpt-4o-mini", model_provider="openai")
prompt = prompt_template.invoke({"language": "Spanish", "text": "hi!"})
print(model.invoke(prompt))



