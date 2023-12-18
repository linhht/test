import os
from openai import OpenAI
import sys

# Load remote env - new way with cloud-based (dotenv.org) .env file
from dotenv_vault import load_dotenv
load_dotenv()
client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))
#print(os.getenv('OPENAI_API_KEY'))

# Usage:
# alias py="DOTENV_KEY='dotenv://:key_3e01f516ab3afccab63494b905a641d5cb978d3640d6d3d6a4e29f3e76fb58ec@dotenv.org/vault/.env.vault?environment=production' python"
# py main.py

