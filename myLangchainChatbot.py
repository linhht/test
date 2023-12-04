# Install required modules/libraries
# pip install --upgrade pip
# pip install --upgrade langchain
# pip install openai
# Run `openai migrate` to automatically upgrade your codebase to use the 1.0.0 interface
# Or pin your installation to the old version, e.g. `pip install openai==0.28`
# pip install python-dotenv
# Create requirement.txt
# pip freeze > requirements.txt
# pip install -r requirements.txt

import os
from openai import OpenAI

# Load local env
from dotenv import load_dotenv, find_dotenv
_=load_dotenv(find_dotenv()) # read local .env file
client = OpenAI(api_key=os.environ['OPENAI_API_KEY'])

# Set the model variable based on the current date
llm_model="gpt-3.5-turbo"

"""
# Start a direct API call to OpenAI
def get_completion(prompt, model=llm_model):
    messages=[
        {
            "role": "user",
            "content": prompt
        }
    ]
    response=client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=0
    )
    return response.choices[0].message["content"]

# Test prompt
get_completion("What is 1+1?")
"""
# To control the randomness and creativity of the generated
# text by an LLM, use temperature = 0.0
from langchain.chat_models import ChatOpenAI

chat=ChatOpenAI(temperature=0.0, model=llm_model)
#print(chat)

# Create promt
from langchain.prompts import ChatPromptTemplate

template_string="""Translate the text \
that is delimited by triple backticks \
into a style that is {style}. \
text: ```{text}```
"""
prompt_template=ChatPromptTemplate.from_template(template_string)
#print(prompt_template.messages[0].prompt)
#print(prompt_template.messages[0].prompt.input_variables)