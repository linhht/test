# Usage:
# alias py="DOTENV_KEY='dotenv://:key_3e01f516ab3afccab63494b905a641d5cb978d3640d6d3d6a4e29f3e76fb58ec@dotenv.org/vault/.env.vault?environment=production' python"
# py main.py
# Load remote env - new way with cloud-based (dotenv.org) .env file
from dotenv_vault import load_dotenv
load_dotenv()

from langchain.chat_models import ChatOpenAI
from langchain.prompts import (
    ChatPromptTemplate,
    HumanMessagePromptTemplate,
    MessagesPlaceholder
)
from langchain.agents import OpenAIFunctionsAgent, AgentExecutor
from tools.sql import run_query_tool


chat = ChatOpenAI()
prompt = ChatPromptTemplate(
    messages=[
        HumanMessagePromptTemplate.from_template("{input}"),
        MessagesPlaceholder(variable_name="agent_scratchpad")
    ]
)

tools = [run_query_tool]

agent = OpenAIFunctionsAgent(
    llm=chat,
    prompt=prompt,
    tools=tools
)

agent_executor = AgentExecutor(
    agent=agent,
    verbose=True,
    tools=tools
)

agent_executor("How many users are in the database?")
