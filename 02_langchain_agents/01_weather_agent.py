from langchain.agents import create_agent
import requests
from dotenv import load_dotenv
import os

# loading environmental variables
load_dotenv()


def get_weather(city: str) -> str:         # city: str is a hint that city is expected to be a string and --> str is also a hint that function is expected to return a string
    """Get weather for a given city."""     # docstring, it is description which tells the model what the toll does and when to use this function

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




agent = create_agent(
    model="ollama:llama3.1",     # llm model along with provider (ollama)
    tools = [get_weather],      # tells the agent which python functions it is allowed to call, functions are passed in list
    system_prompt="You are a weather assistant.",       # tells the behavious to model

)


result = agent.invoke(
    {"messages": [
        {"role": "user", 
        "content": "What is the weather in Rawalpindi?"}
    ]}
)


print(result["messages"][-1].content)


# check all conversation
# for message in result["messages"]:
#     print("ROLE:", message.type)
#     print(message.content)
#     print("----------------")