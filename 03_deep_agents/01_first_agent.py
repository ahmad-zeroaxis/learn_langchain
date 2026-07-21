from deepagents import create_deep_agent

agent = create_deep_agent(model="ollama:llama3.1")

result = agent.invoke({"messages": [{"role": "user", "content": "What is an LLM? Explain in one line"}]})

print(result["messages"][-1].content)