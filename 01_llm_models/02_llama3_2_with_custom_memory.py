from langchain_ollama import ChatOllama

llm = ChatOllama(model="llama3.2")

history = []
while(True):
    user_input = input("You: ")
    # break the loop (end the conversation) if user type /bye
    if user_input.strip() == "/bye":
        break
    
    history.append(f"Human: {user_input}")

    response = llm.invoke(history)
    
    history.append(f"AI: {response.content}")

    print("LLAMA: ", response.content) 