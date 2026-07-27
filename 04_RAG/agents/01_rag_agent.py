import os
import getpass
import hashlib
from dotenv import load_dotenv
from langchain_chroma import Chroma
from langchain_google_genai import GoogleGenerativeAIEmbeddings




load_dotenv() 

if not os.environ.get("GOOGLE_API_KEY"):
  os.environ["GOOGLE_API_KEY"] = getpass.getpass("Enter API key for Google Gemini: ")




# SELECT EMBEDDING MODEL

embedding_model = GoogleGenerativeAIEmbeddings(
    model="gemini-embedding-2-preview"
)




# CONNECT TO VECTOR STORE

vector_store = Chroma(
    collection_name="linix_commands",
    embedding_function=embedding_model,
    persist_directory="./chroma_langchain_db",  # Where to save data locally, remove if not necessary
)




# Step#4: RETRIVERS

# create retriver using vector store 
retriver = vector_store.as_retriever(search_kwargs={"k": 1})    # k tells how many results i want i return

query = "What tar xf file.tar command do?"

relevent_docs = retriver.invoke(query)

for i, doc in enumerate(relevent_docs):
  print(f"\n----- Result {i+1} -----")
  print(doc.page_content)