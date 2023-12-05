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

customer_style="""American English \
in a calm and respectful tone
"""

customer_email="""
Arrr, I be fuming that me blender lid \
flew off and splattered me kitchen walls \
with smoothie! And to make matters worse, \
the warranty don't cover the cost of \
cleaning up me kitchen. I need yer help \
right now, matey!
"""

customer_messages=prompt_template.format_messages(
    style=customer_style,
    text=customer_email
)

#print(type(customer_messages))
#print(type(customer_messages[0]))
#print(customer_messages[0])

# Call the LLM to translate to the style of the customer message
#customer_response=chat(customer_messages)
#print(customer_response.content)

service_reply="""Hey there customer, \
the warranty does not cover \
cleaning expenses for your kitchen \
because it's your fault that \
you misused your blender \
by forgetting to put the lid on before \
starting the blender. \
Tough luck! See ya!"""

service_style_pirate="""\
a polite tone \
that speaks in English Pirate\
"""

service_messages=prompt_template.format_messages(
    style=service_style_pirate,
    text=service_reply
)

#print(service_messages[0].content)
#service_response=chat(service_messages)
#print(service_response.content)
