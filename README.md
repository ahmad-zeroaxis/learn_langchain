### Installing ollama provider locally 
    irm https://ollama.com/install.ps1 | iex



### Once ollama is installed we can fetch/download any model available on ollama.com/library
    ollama pull model_name
    e.g.,
    ollama pull llama3.2



### View available models run the following command
    ollama list



### Run any model in terminal
    ollama run llama3.2



### Make a project using uv
    uv init project_name



### Installing langchain python package (uv will automatically make virtual environment)
### langchain is a framework that is used to make agentic workflows
    uv add langchain



### We also need to install langchain-ollama python package to interact with ollama in python code
    uv add langchain-ollama



### Install python-dotenv to handle environmental variables
    uv add python-dotenv