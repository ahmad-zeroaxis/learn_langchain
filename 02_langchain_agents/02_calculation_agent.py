from langchain.chat_models import init_chat_model
from langchain.agents import create_agent
from langchain.tools import tool
# from langchain.messages import SystemMessage    # SystemMessage is accept by system_prompt of agent to define behaviour at runtime


# DEFINING LLM MODEL 
model = init_chat_model(
    "ollama:llama3.1",
    temperature=0,
    num_predict=500,   # maximum tokens that can be generated, for ollama argument is num_predict
)



# DEFINE TOOLS FOR AGENT

@tool
def add(a: int, b: int) -> int:
    """Adds `a` and `b`.

    Args:
        a: First int
        b: Second int
    """
    return a + b



@tool
def subtract(a: int, b: int) -> int:
    """Subtract `a` and `b`.

    Args:
        a: First int
        b: Second int
    """
    return a - b



@tool
def multiply(a: int, b: int) -> int:
    """Multiply `a` and `b`.

    Args:
        a: First int
        b: Second int
    """
    return a * b



@tool
def divide(a: int, b: int) -> float:
    """Divide `a` and `b`.

    Args:
        a: First int
        b: Second int
    """
    return a / b





# CREATING AGENT
 
my_agent = create_agent(
    model="ollama:llama3.2",
    tools = [add, subtract, multiply, divide],
    system_prompt="You are a agent for calculations",
)

result = my_agent.invoke(
    {
        "messages": [
            {"role": "user",
            "content": "What is 18 / 2"}
        ]
    }
)

print(result["messages"][-1].content)


# for message in result["messages"]:
#     print("ROLE:", message.type)
#     print(message.content)
#     print("----------------")