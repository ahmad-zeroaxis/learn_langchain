import os
import getpass
from dotenv import load_dotenv
from langchain_chroma import Chroma
from langchain_core.prompts import PromptTemplate
from youtube_transcript_api import YouTubeTranscriptApi
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter



load_dotenv() 

if not os.environ.get("GOOGLE_API_KEY"):
  os.environ["GOOGLE_API_KEY"] = getpass.getpass("Enter API key for Google Gemini: ")



# TRANSCRIPT LOADER API
yt_api = YouTubeTranscriptApi()


# TEXT SPLITTER
splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)


# EMBEDDING MODEL
embedding_model = GoogleGenerativeAIEmbeddings(
    model="gemini-embedding-2-preview"
)


# VECTOR STORE
vector_store = Chroma(
    collection_name="yt_videos_transcripts",
    embedding_function=embedding_model,
    persist_directory="chroma_langchain_db",
)


# RETRIVER
retriver = vector_store.as_retriever(
    search_type="mmr",
    search_kwargs={"k": 4}
)


# PROMPT
prompt = PromptTemplate(
    template="""
        You are a helpfull assistant.
        Answer ONLY from provided context.
        If the context is insufficient, just say you dont't know.

        Context: {context}
        Question: {question}
    """,
    input_variables=['context', 'question'],
    validate_template = True,
)


# GENERAIVE MODEL (LLM)
llm = ChatGoogleGenerativeAI(
    model="gemini-3.5-flash-lite",
    temperature=0.3
)


# USER INPUTS
video_id = "yUFpTtM7PvI"    # OpenAI hack HuggingFace
# video_id = "VwCZxSqTIaY"    # Vector DB explained
# video_id = "RAIVgn5RWXo"    # AI Engineer versus Full Stack Engineer
# video_id = "d-NJTcTvyhw"    # KAFKA
question = "Explain how OpenAi hacked HuggingFace?"






# loading
try:
    transcript = yt_api.fetch(video_id=video_id, languages=["en"])
    str_transcript = ' '.join( data.text for data in transcript.snippets )

except Exception as e:
    print(type(e).__name__)
    print(e)

else:
    # splitting
    chunks = splitter.create_documents(
        texts=[str_transcript],
        metadatas=[{"source": "youtube"}]
    )

    # storing
    # vector_store.add_documents(chunks)    # run once for each video

    # retriving
    context_docs = retriver.invoke(question)
    context = '\n\n'.join(text.page_content for text in context_docs)

    # prompting
    final_prompt = prompt.invoke( {'context': context, 'question': question} )

    # generation
    answer = llm.invoke(final_prompt)
    print(answer.text)