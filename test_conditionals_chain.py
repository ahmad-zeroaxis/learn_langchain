from typing import Literal
from dotenv import load_dotenv
from pydantic import BaseModel, Field
from langchain_core.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.output_parsers import PydanticOutputParser
from langchain_core.runnables import RunnableBranch, RunnableLambda

load_dotenv() 





class Feedback(BaseModel):
    sentiment: Literal['positive', 'negative'] = Field( description='Give the sentiment of feedback' )

pyd_output_parser = PydanticOutputParser(pydantic_object=Feedback)


model = ChatGoogleGenerativeAI(
    model="gemini-3.1-flash-lite"
)


prompt = PromptTemplate(
    template="""Extract the sentiment of the following feedback text into positive or negative \n{feedback} \n{formate_instructions}""",
    input_variables=['feedback'],
    partial_variables={'formate_instructions': pyd_output_parser.get_format_instructions()}
)

positive_feedback_prompt = PromptTemplate(
    template="""Write an appropriate feedback to following positive feedback text. Do not use markdown, just write reply in simple text. \nfeedback: {feedback}""",
    input_variables=['feedback']
)

negative_feedback_prompt = PromptTemplate(
    template="""Write an appropriate feedback to following negative feedback text. Do not use markdown, just write reply in simple text. \nnfeedback: {feedback}""",
    input_variables=['feedback']
)


output_parser = StrOutputParser()




classifier_chain = prompt | model | pyd_output_parser 


branch_chain = RunnableBranch(
    (lambda x: x.sentiment == 'positive', positive_feedback_prompt | model | output_parser),
    (lambda x: x.sentiment == 'negative', negative_feedback_prompt | model | output_parser),
    RunnableLambda(lambda x: "could not find sentiment")
)


final_chain = classifier_chain | branch_chain


result = final_chain.invoke({'feedback': 'The shoes are awfull.'})
print(result)
