# Usage:
# alias py="DOTENV_KEY='dotenv://:key_3e01f516ab3afccab63494b905a641d5cb978d3640d6d3d6a4e29f3e76fb58ec@dotenv.org/vault/.env.vault?environment=production' python"
# py main.py
# pip install tiktoken
# pip install chromadb
# Load remote env - new way with cloud-based (dotenv.org) .env file
from dotenv_vault import load_dotenv
load_dotenv()

from langchain.document_loaders import TextLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores.chroma import Chroma
# To support sqlite3
__import__('pysqlite3')
import sys
sys.modules['sqlite3'] = sys.modules.pop('pysqlite3')


embeddings = OpenAIEmbeddings()
# emb = embeddings.embed_query("Hello, my name is John")
# print (emb)

text_splitter = CharacterTextSplitter(
    separator="\n",
    chunk_size=200,
    chunk_overlap=0
)

loader = TextLoader("facts.txt")
docs = loader.load_and_split(
    text_splitter=text_splitter
)

db = Chroma.from_documents(
    documents=docs,
    embedding=embeddings,
    persist_directory="emb"
)

# results = db.similarity_search(
#     "What is an interesting fact about the English language?"
# )

# for doc in docs:
#     print(doc.page_content)
#     print("\n")
