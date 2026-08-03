import os
import numpy as np
from dotenv import load_dotenv
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import CharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings


os.load_dotenv()


FILE_PATH = r"04_RAG\docs\Linix_Commands_Cheatsheet.pdf"


# Step#1: LOAD

loader = PyPDFLoader(FILE_PATH)

docs = loader.load()




# Step#2: SPLITT

splitter = CharacterTextSplitter(
    chunk_size=100,
    chunk_overlap=15,
    separator=''
)

docs_chunks = splitter.split_documents(docs)

for index, chunk in enumerate(docs_chunks):
    print(f"\n---- Chunk {index+1} ----")
    print(chunk.page_content)




# Step#3:  EMBEDDINGS

# function to find similarities btw document and querry, basically we find angular distance btw vectors
def cosine_similarities(vect1, vect2):
    dot_product = np.dot(vect1, vect2)
    norm1 = np.linalg.norm(vect1)
    norm2 = np.linalg.norm(vect2)
    return dot_product / (norm1 * norm2)


# select embedding model
embedding_model = GoogleGenerativeAIEmbeddings(
    model="gemini-embedding-2-preview"
)

str_docs_chunks = [chunk.page_content for chunk in docs_chunks]

document_embeddings = embedding_model.embed_documents(str_docs_chunks)

query = "What is the use of cd command?"
query_embedding = embedding_model.embed_query(query)


cosine_similarities(document_embeddings, query_embedding)