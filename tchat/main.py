# Usage:
# alias py="DOTENV_KEY='dotenv://:key_3e01f516ab3afccab63494b905a641d5cb978d3640d6d3d6a4e29f3e76fb58ec@dotenv.org/vault/.env.vault?environment=production' python"
# py main.py
from langchain.chat_models import ChatOpenAI
from langchain.chains import LLMChain
from langchain.prompts import HumanMessagePromptTemplate, ChatPromptTemplate, MessagesPlaceholder
from langchain.memory import ConversationBufferMemory, FileChatMessageHistory, ConversationSummaryMemory
import os
# Load remote env - new way with cloud-based (dotenv.org) .env file
from dotenv_vault import load_dotenv
load_dotenv()

chat = ChatOpenAI(verbose=True)

memory = ConversationSummaryMemory(
#memory = ConversationBufferMemory(
    #chat_memory=FileChatMessageHistory("messages.json"),
    memory_key="messages",
    return_messages=True,
    llm=chat
)

prompt = ChatPromptTemplate(
    input_variables=["content", "meassages"],
    messages=[
        MessagesPlaceholder(variable_name="messages"),
        HumanMessagePromptTemplate.from_template("{content}")
    ]
)

chain = LLMChain(
    llm=chat,
    prompt=prompt,
    memory=memory,
    verbose=True
)

while True:
    content = input(">> ")

    result = chain({"content": content})

    print(result["text"])
