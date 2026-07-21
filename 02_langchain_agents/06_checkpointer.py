from langchain.agents import create_agent
from langchain_core.utils.uuid import uuid7
from langgraph.checkpoint.memory import InMemorySaver
from langchain.tools import tool
import requests
from dotenv import load_dotenv
import os



# loading environmental variables
load_dotenv()

@tool
def get_weather(city: str) -> str:
    """Get weather for a given city."""

    weather_api_key = os.getenv("OPEN_WEATHER_API_KEY")
    url = (f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={weather_api_key}&units=metric")       # units=metric will give temperature in degree
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





# Persisting conversation history with thread_id requires the agent to be configured with a checkpointer when running locally, When deployed on LangSmith, a checkpointer is provisioned automatically

agent = create_agent(
    model="ollama:llama3.2",
    tools=[get_weather],
    checkpointer=InMemorySaver(),  # do chaching
)


config = {"configurable": {"thread_id": str(uuid7())}}

result = agent.invoke(
    {"messages": [{"role": "user", "content": "What's the weather in San Francisco?"}]},
    config=config,
    )


print(result["messages"][-1].content)