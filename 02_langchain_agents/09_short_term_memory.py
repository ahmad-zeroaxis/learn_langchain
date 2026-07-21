from langchain.agents import create_agent
from langgraph.checkpoint.memory import InMemorySaver


agent = create_agent(
    model="ollama:llama3.2",
    checkpointer=InMemorySaver(),
)

thread_config = {"configurable": {"thread_id": "1"}}


user_input = input("You: ")
while(user_input.strip() != "/bye"):
    response = agent.invoke(
        {"messages": [
            {
                "role": "user",
                "content": user_input,
            }
        ]},
        config=thread_config,
    )["messages"][-1].content
    
    print("LAMA3.2:", response, '\n')   # python syntax of chaining, it will directly store it in response

    user_input = input("You: ")
    









# In production, use a checkpointer backed by a database



# pip install langgraph-checkpoint-postgres



# from langchain.agents import create_agent
# from langgraph.checkpoint.postgres import PostgresSaver  

# def get_user_info() -> str:
#     """Look up information about the current user."""
#     return "No user profile on file."

# DB_URI = "postgresql://postgres:postgres@localhost:5432/postgres?sslmode=disable"
# with PostgresSaver.from_conn_string(DB_URI) as checkpointer:
#     checkpointer.setup() # auto create tables in PostgreSQL
#     agent = create_agent(
#         "gpt-5.5",
#         tools=[get_user_info],
#         checkpointer=checkpointer,
#     )