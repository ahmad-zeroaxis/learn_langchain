from langchain_ollama import ChatOllama
from langchain_core.chat_history import InMemoryChatMessageHistory
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage      # SystemMessage is optional, we can give instructions LLM through this 


llm = ChatOllama(model="llama3.2")

history = InMemoryChatMessageHistory()

while(True):
    user_input = input("You: ")
    if user_input.strip() == "/bye":
        break

    history.add_user_message(user_input)

    response = llm.invoke(history.messages)

    history.add_ai_message(response.content)

    print(f"LLAMA: {response.content}")