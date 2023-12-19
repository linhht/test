# Usage:
# alias py="DOTENV_KEY='dotenv://:key_3e01f516ab3afccab63494b905a641d5cb978d3640d6d3d6a4e29f3e76fb58ec@dotenv.org/vault/.env.vault?environment=production' python"
# py prompt.py
from langchain.vectorstores import Chroma
from langchain.embeddings import OpenAIEmbeddings
from langchain.chains import RetrievalQA
from langchain.chat_models import ChatOpenAI

# To support sqlite3
__import__('pysqlite3')
import sys
sys.modules['sqlite3'] = sys.modules.pop('pysqlite3')

# Load remote env - new way with cloud-based (dotenv.org) .env file
from dotenv_vault import load_dotenv
load_dotenv()

chat = ChatOpenAI()
embeddings = OpenAIEmbeddings()
db = Chroma(
    persist_directory="emb",
    embedding_function=embeddings
)
retriever = db.as_retriever()

chain = RetrievalQA.from_chain_type(
    llm=chat,
    retriever=retriever,
    chain_type="stuff"
)

result = chain.run("What is an interesting fact about the English language?")

print(result)
