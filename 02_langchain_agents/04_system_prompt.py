# system_prompt parameter is used to describe the behaviour of agent
# system prompt parameter accepts a string or SystemMessage, for dynamic prompts at runtime

from langchain_core.messages import SystemMessage
from langchain.agents import create_agent


tone = input("Tone of agent: ")
length = input("Response length: ")
agent = create_agent(
    model="ollama:llama3.1",
    system_prompt=SystemMessage(
        content=f"""
You are an AI assistant.

Rules:
- Tone: {tone}
- Response length: {length}
- Use bullet points whenever possible.
""")
)

result = agent.invoke({"messages": [{"role": "user", "content": "Define AI"}]})
print(result["messages"][1].content)