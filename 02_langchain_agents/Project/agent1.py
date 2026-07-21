import os
import requests
from datetime import datetime
from dotenv import load_dotenv

from langchain.chat_models import init_chat_model
from langchain.agents import create_agent
from langchain.tools import tool
from langchain_core.messages import HumanMessage
from langchain_core.utils.uuid import uuid7
from langgraph.checkpoint.memory import InMemorySaver


# load evironmental variables
load_dotenv()



@tool
def get_weather(city: str) -> str:
    """Get weather for a given city with description temperature and humidity."""     # docstring, it is description which tells the model what the toll does and when to use this function

    weather_api_key = os.getenv("OPEN_WEATHER_API_KEY")
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={weather_api_key}&units=metric"       # units=metric will give temperature in degree
    response = requests.get(url)
   
    data = response.json()
    if response.status_code != 200:
        return f"Error: {data.get('message', 'Unknown error')}"

    return (
        f"Weather in {city}: "
        f"{data['weather'][0]['description']}, "
        f"Temperature: {data['main']['temp']}°C, "
        f"Humidity: {data['main']['humidity']}%"
    )



@tool
def convert_currency(from_currency: str, to_currency: str, amount: int) -> str | float:
    """
    Get an amount from one currency to another.
    Example:
        from_currency = "USD"
        to_currency = "PKR"
    """

    exchangerate_api_key = os.getenv("EXCHANGERATE_API_KEY")    # fetch api key from .env
    url=f"https://api.exchangerate.host/convert?access_key={exchangerate_api_key}&from={from_currency}&to={to_currency}&amount={amount}"

    response = requests.get(url)
    if response.status_code != 200:     # success response is 200
        return "Error occured while API call"
    else:
        data = response.json()
        return data["result"]



@tool
def current_date() -> str:
    """Get current date"""
    return datetime.now().strftime("%d-%m-%Y")



@tool
def current_time() -> str:
    """Get current time"""
    return datetime.now().strftime("%#I:%M %p")      # am, pm formate








# LLM model
model = init_chat_model(
    model="gemini-3.1-flash-lite",
    model_provider="google_genai",
    temperature=0,
    max_tokens=300,
    api_key=os.getenv("GOOGLE_API_KEY"),
)



checkpointer = InMemorySaver()

# AGENT
agent = create_agent(
    model=model,
    tools=[convert_currency, get_weather, current_date, current_time],
    system_prompt=(
       "You are a helpful assistant. Only use tools when the user's "
       "message clearly requires weather information or currency conversion or current date or curent time."
       "For greetings or general chat, just respond normally without calling any tool."
    ),
    checkpointer=checkpointer,
)



thread_config = {"configurable": {"thread_id": str(uuid7())}}   # uuid7() generates unique id

user_input = input("You: ")
while(user_input.strip() != "bye"):
    print("Gemini: ", end="")
    for chunk, metadata in agent.stream(
        {"messages": [HumanMessage(content=user_input)]},
        stream_mode="messages",
        config=thread_config,
    ):
        if metadata.get("langgraph_node") != "model":
            continue

        content = chunk.content

        if isinstance(content, str):
            if content:
                print(content, end="", flush=True)

        elif isinstance(content, list):
            for part in content:
                text = part.get("text", "")
                if text:
                    print(text, end="", flush=True)


    print('\n')     # new line and spacing after agent's response
    user_input = input("You: ")
