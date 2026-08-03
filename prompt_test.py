from langchain_core.prompts import PromptTemplate


prompt = PromptTemplate(
    template="Generate 2 facts about {topic}",
    input_variables=['topic']
)



prompt = prompt.invoke({'topic': 'Football'})

print(prompt)
print(prompt.text)