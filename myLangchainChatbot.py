# Install required modules/libraries
# pip install --upgrade pip
# pip install --upgrade langchain

# pip install openai
# Run `openai migrate` to automatically upgrade your codebase to use the 1.0.0 interface
# Or pin your installation to the old version, e.g. `pip install openai==0.28`

# pip install --upgrade flask python-dotenv-vault

# Create requirement.txt
# pip freeze > requirements.txt
# pip install -r requirements.txt

import os
from openai import OpenAI

# Load local env - old way
#from dotenv import load_dotenv, find_dotenv
#_=load_dotenv(find_dotenv()) # read local .env file
#client = OpenAI(api_key=os.environ['OPENAI_API_KEY'])

# Load remote env - new way with cloud-based (dotenv.org) .env file
from dotenv_vault import load_dotenv
load_dotenv()
api_key=os.getenv('OPENAI_API_KEY')
print(f"{api_key}")
print("hello")
