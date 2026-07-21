from langchain_ollama import ChatOllama
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage      # SystemMessage is optional, we can give instructions LLM through this 

llm = ChatOllama(model="llama3.2")


history = [
    SystemMessage(content="Your are a Mathimatics instructor and you have to respond only to the questions related to Mathimatics. If user ask any other question, politly deny him to respond that it is not related to your domain and is outside your area of expertise.")
]
while(True):
    user_input = input("You: ")
    # break the loop (end the conversation) if user type /bye
    if user_input.strip() == "/bye":
        break
    
    history.append(HumanMessage(content=user_input))

    response = llm.invoke(history)
    
    history.append(AIMessage(content=response.content))

    print("LLAMA: ", response.content) 


print(history)