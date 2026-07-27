import os
import getpass
import hashlib
from dotenv import load_dotenv
from langchain_chroma import Chroma
from langchain_community.document_loaders import PyPDFLoader
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_community.vectorstores.utils import filter_complex_metadata




load_dotenv() 

if not os.environ.get("GOOGLE_API_KEY"):
  os.environ["GOOGLE_API_KEY"] = getpass.getpass("Enter API key for Google Gemini: ")


FILE_PATH = r"04_RAG\docs\Linix_Commands_Cheatsheet.pdf"



# Step#1: LOAD

loader = PyPDFLoader(FILE_PATH)

documents = loader.load()   # Load full pdf at once

documents = filter_complex_metadata(documents)




# Step#2:   SELECT EMBEDDING MODEL

embedding_model = GoogleGenerativeAIEmbeddings(
    model="gemini-embedding-2"
)




# Step#3:   VECTOR STORE

vector_store = Chroma(
    collection_name="linix_commands",
    embedding_function=embedding_model,
    persist_directory="./chroma_langchain_db",  # Where to save data locally, remove if not necessary
)


# this function will generate same id for same document using hashing, to prevent readding the same document
def make_id(doc):
    return hashlib.sha256(doc.page_content.encode()).hexdigest()

ids = [make_id(doc) for doc in documents]


# only insert new ids into vector store
existing = vector_store.get(ids=ids)
new_ids = [id_ for id_ in ids if id_ not in existing["ids"]]

if new_ids:
    new_docs = [doc for doc, id_ in zip(documents, ids) if id_ in new_ids]
    vector_store.add_documents(documents=new_docs, ids=new_ids)
    print(f"Added {len(new_docs)} new chunks.")
else:
    print("All chunks already in the store, skipping embedding.")





# Step#4: RETRIVERS

# with the help of retrivers we can implement different search strategies

# there are multiple Retrivers: Data Source and Search strategies (wikipedia retrivers, vector store retrivers, MMR)

# in LangChain all Retrivers are runnables (we can make chains)


# create retriver using vector store 
retriver = vector_store.as_retriever(search_kwargs={"k": 1})    # k tells how many results i want i return

query = "What does nk dir command do?"

result_docs = retriver.invoke(query)

for i, doc in enumerate(result_docs):
  print(f"\n----- Result {i+1} -----")
  print(doc.page_content)