# three types of streaming is supported
# updates       state updates after each agent step
# messages      (token, metadata)
# custom        custom data from inside your graph nodes


from langchain.agents import create_agent

agent = create_agent(
    model = "ollama:llama3.2"
)

stream = agent.stream_events(   # gives stream of events
    {"messages": [{
        "role": "user",
        "content": "what is computer?"
    }]},
    version='v3'
)

# LangChain has changed the event format over time.
# v1 → Older format
# v2 → Improved format
# v3 → Latest event schema (recommended)

# Each version defines:
# Event names
# Event fields
# How tokens are represented
# Metadata included


for message in stream.messages:
    for delta in message.text:
        print(delta, end="", flush=True)

# print(type(result_generator.text))