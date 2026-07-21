from langchain_ollama import ChatOllama

llm = ChatOllama(model="llama3.2")

while(True):
    user_input = input("You: ")
    # break the loop (end the conversation) if user type /bye
    if user_input.strip() == "/bye":
        response = llm.invoke(user_input)
        print("LLAMA:", response.content)
        break

    response = llm.invoke(user_input)
    print("LLAMA: ", response.content)