from langchain_docling.loader import DoclingLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter


FILE_PATH = r"docs\Transformers.pdf"


# Step#1: LOAD

loader = DoclingLoader(FILE_PATH)

documents = loader.load()   # Load full pdf at once



# Step#2: SPLITT

full_text = "\n".join([doc.page_content for doc in documents])

text_splitter = RecursiveCharacterTextSplitter(chunk_size=100, chunl_overlap=0)

texts = text_splitter.split_text(full_text)
