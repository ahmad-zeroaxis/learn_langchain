from pydantic import BaseModel
from langchain.agents import create_agent
from langchain.tools import tool



class Answer(BaseModel):
    summary: str
    confidence: float



agent = create_agent(
    model="ollama:llama3.2",
    response_format=Answer
)



result = agent.invoke({"messages": [{"role": "user", "content": "Summarize AI trends"}]})
print(result["structured_response"].summary)
print(result["structured_response"].confidence)

print(result["structured_response"])
