import urllib.request
import urllib.error

from langchain.tools import tool

# CREATING TOOL FOR AGENT
@tool
def fetch_text_from_url(url: str) -> str:
    """Downloads the complete plain-text document from the given URL.
       Use this tool only to obtain the document contents.
       Never return the raw text directly unless the user explicitly requests it.
       Instead, analyze or summarize the fetched text."""

    # preparing request
    request = urllib.request.Request(
        url,
        headers={"User-Agent": "Mozilla/5.0 (compatible; quickstart-research/1.0)"}     # setting header to mimick Mozilla style header to prevent blocking by server
    )

    try:
        with urllib.request.urlopen(request, timeout=120) as response:  # urlopen() sed a get request  # with ensures that response object (response) is automatically and safely closed after use
            raw =  response.read()
    except urllib.error.URLError as e:
        return f"Fetch failed: {e}"
    
    text = raw.decode("utf-8", errors="replace")    # errors="replace" replace the invalid byte to � instead of raising error
    
    return text








# CREATING LLM MODEL

from langchain.chat_models import init_chat_model      # we can make any llm model along with by telling provider with init_chat_model, eventhough all providers have their on specific class also

model = init_chat_model(
    "ollama:llama3.2",
    temperature = 0.1,
    # timeout = 300,
    max_tokens = 1800,
)


# ADDING MEMORY TO AGENT
from langgraph.checkpoint.memory import InMemorySaver

# memory allows the agent to remember previous conversations and context.
checkpointer = InMemorySaver()








# CREATING AGENT

# there are two different frameworks of agents
#   1. LamgChain agents  (gives more contro; on fine-grained)
#   2. Deep agents    (come with a range of commonly useful capabilities already built in, such as planning, file system tools, and subagents)


from langchain.agents import create_agent

agent = create_agent(
    model=model,
    tools=[fetch_text_from_url],
    system_prompt="""
You are a literary assistant.

When the user provides a novel URL:

1. Call fetch_text_from_url.
2. Read the returned text.
3. Do NOT return the raw text.
4. Produce the requested output using the fetched text.
5. Never expose the fetched document unless the user explicitly asks for it.
6. If the document is too large, explain that it must be processed in chunks.""",
    checkpointer=checkpointer,  # agent autoatically use this memory obj (to save conversation and understanding context)
)


# https://www.gutenberg.org/files/43/43-0.txt       The Strange Case Of Dr. Jekyll And Mr. Hyde by Robert Louis Stevenson
# https://www.gutenberg.org/files/46/46-0.txt       A Christmas Carol A Ghost Story of Christmas by Charles Dickens
# https://www.gutenberg.org/files/35/35-0.txt       The Time Machine An Invention by H. G. Wells


content = f"""Project Gutenberg hosts public-domain books in plain text.

Novel URL:
https://www.gutenberg.org/files/35/35-0.txt

Task:
Read the novel from the URL and generate a comprehensive summary.

Instructions:
- Identify the novel title.
- Identify the author.
- Produce a summary between 900 and 1,100 words.
- Preserve the chronological order of events.
- Include all major characters.
- Include the central conflict.
- Include all important plot developments.
- Include the climax and the ending.
- Do not invent or infer events that are not present in the text.
- Do not omit important plot points.
- Write in plain English suitable for someone who has never read the novel.
- Spoilers are allowed and expected.

Output exactly in this format:

Title: <title>

Author: <author>

Summary:
<900-1100 word summary>"""



agent_result = agent.invoke(
    {"messages": [{"role": "user", "content": content}]},
    config={"configurable": {"thread_id": "novel_mmary"}},
)

print(agent_result["messages"][-1].content)

