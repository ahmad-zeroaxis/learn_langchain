# general formate
{
    "messages": [HumanMessage(),
              AIMessage(),
              ToolMessage()],

    "structured_response": object(),

    "config": {"configurable": {"thread_id": str(uuid7())}}

    "key": value,
}





# example

{'messages': [
    HumanMessage(content='Summarize AI trends', additional_kwargs={}, response_metadata={}, id='5c0bdd7d-701e-49d6-be07-4125c5fc9420'), 
    
    AIMessage(content='', additional_kwargs={}, response_metadata={'model': 'llama3.2', 'created_at': '2026-07-20T06:41:54.8952421Z', 'done': True, 'done_reason': 'stop', 'total_duration': 11892205500, 'load_duration': 3579877800, 'prompt_eval_count': 154, 'prompt_eval_duration': 2907254000, 'eval_count': 62, 'eval_duration': 5397408000, 'logprobs': None, 'model_name': 'llama3.2', 'model_provider': 'ollama'}, id='lc_run--019f7e42-5057-74d3-9a41-bf4aa04bec2f-0', tool_calls=[{'name': 'Answer', 'args': {'summary': 'The current AI trends include the increasing adoption of machine learning in various industries, advancements in natural language processing, and the development of Explainable AI (XAI) to increase transparency and trustworthiness.', 'confidence': 0.9}, 'id': '0b1d9c26-24a7-404e-bc74-c66ebdee459f', 'type': 'tool_call'}], invalid_tool_calls=[], usage_metadata={'input_tokens': 154, 'output_tokens': 62, 'total_tokens': 216}), 
    
    ToolMessage(content="Returning structured response: summary='The current AI trends include the increasing adoption of machine learning in various industries, advancements in natural language processing, and the development of Explainable AI (XAI) to increase transparency and trustworthiness.' confidence=0.9", name='Answer', id='3674959d-1f51-4727-90de-e095da4cc6c3', tool_call_id='0b1d9c26-24a7-404e-bc74-c66ebdee459f')
    ], 
    
    'structured_response': Answer(summary='The current AI trends include the increasing adoption of machine learning in various industries, advancements in natural language processing, and the development of Explainable AI (XAI) to increase transparency and trustworthiness.', confidence=0.9)}










{
    'messages': [
        HumanMessage(content='Define AI', additional_kwargs={}, response_metadata={}, id='6318715e-453b-4c66-8d25-e49253cbeb7b'), 
        
        AIMessage(content="I'd be happy to explain what AI is in simple terms!\n\n**Artificial Intelligence (AI) Definition:**\n\nAI refers to a computer system that can:\n\n• Think and learn like humans\n• Make decisions based on data and experience\n• Adapt to new situations and environments\n• Perform tasks that typically require human intelligence, such as:\n\t+ Recognizing images and speech\n\t+ Understanding natural language\n\t+ Making predictions and recommendations\n\nIn other words, AI is a way for computers to become more intelligent and capable of handling complex tasks on their own!", additional_kwargs={}, response_metadata={'model': 'llama3.1', 'created_at': '2026-07-20T07:51:07.0262887Z', 'done': True, 'done_reason': 'stop', 'total_duration': 83251744000, 'load_duration': 59422178400, 'prompt_eval_count': 43, 'prompt_eval_duration': 2156072000, 'eval_count': 114, 'eval_duration': 21594274000, 'logprobs': None, 'model_name': 'llama3.1', 'model_provider': 'ollama'}, id='lc_run--019f7e80-94dc-7ca3-9643-6c771e1a9bb7-0', tool_calls=[], invalid_tool_calls=[], usage_metadata={'input_tokens': 43, 'output_tokens': 114, 'total_tokens': 157})
    ]
}



{
    'messages': [
        HumanMessage(content="What's the weather in San Francisco?", additional_kwargs={}, response_metadata={}, id='38662d74-8d17-4363-b83b-3622b0f1faad'), 
        
        AIMessage(content='', additional_kwargs={}, response_metadata={'model': 'llama3.1', 'created_at': '2026-07-20T09:00:14.0929932Z', 'done': True, 'done_reason': 'stop', 'total_duration': 3986742800, 'load_duration': 272906300, 'prompt_eval_count': 159, 'prompt_eval_duration': 313583000, 'eval_count': 18, 'eval_duration': 3377738000, 'logprobs': None, 'model_name': 'llama3.1', 'model_provider': 'ollama'}, id='lc_run--019f7ec1-11f8-7df1-96b9-7f5d7d95cf35-0', tool_calls=[{'name': 'get_weather', 'args': {'city': 'San Francisco'}, 'id': '638b8ba5-4775-4bd5-8ad3-42732e361c8f', 'type': 'tool_call'}], invalid_tool_calls=[], usage_metadata={'input_tokens': 159, 'output_tokens': 18, 'total_tokens': 177}), 
        
        ToolMessage(content='Weather in San Francisco: overcast clouds, Temperature: 14.35°C, Humidity: 82%', name='get_weather', id='8bbeea79-9ea6-4c9b-b6ef-2eda1773983c', tool_call_id='638b8ba5-4775-4bd5-8ad3-42732e361c8f'), 
        
        AIMessage(content="The tool call returned the weather data for San Francisco, which was then used to format an answer to the user's question about the weather in that city.", additional_kwargs={}, response_metadata={'model': 'llama3.1', 'created_at': '2026-07-20T09:00:21.4195502Z', 'done': True, 'done_reason': 'stop', 'total_duration': 6285580200, 'load_duration': 241321500, 'prompt_eval_count': 115, 'prompt_eval_duration': 202529000, 'eval_count': 32, 'eval_duration': 5813512000, 'logprobs': None, 'model_name': 'llama3.1', 'model_provider': 'ollama'}, id='lc_run--019f7ec1-259d-7111-ac3b-6ea5c0078787-0', tool_calls=[], invalid_tool_calls=[], usage_metadata={'input_tokens': 115, 'output_tokens': 32, 'total_tokens': 147})]
}








{'messages': [
    HumanMessage(content="What's the weather in San Francisco?", additional_kwargs={}, response_metadata={}, id='f9d58e2f-94a4-4010-b165-e1601f8ef67b'), 
    
    AIMessage(content='', additional_kwargs={}, response_metadata={'model': 'llama3.2', 'created_at': '2026-07-20T09:15:47.3650989Z', 'done': True, 'done_reason': 'stop', 'total_duration': 3304399300, 'load_duration': 276600100, 'prompt_eval_count': 192, 'prompt_eval_duration': 1587303000, 'eval_count': 18, 'eval_duration': 1423761000, 'logprobs': None, 'model_name': 'llama3.2', 'model_provider': 'ollama'}, id='lc_run--019f7ecf-523c-7d60-8721-c7fd4ff53297-0', tool_calls=[{'name': 'get_weather', 'args': {'city': 'San Francisco'}, 'id': '8423e167-7342-42d3-ab3d-206e083c5ca4', 'type': 'tool_call'}], invalid_tool_calls=[], usage_metadata={'input_tokens': 192, 'output_tokens': 18, 'total_tokens': 210}), 
    
    ToolMessage(content='Weather in San Francisco: overcast clouds, Temperature: 14.41°C, Humidity: 82%', name='get_weather', id='358650d8-2eb6-4a2f-90bf-247199bb86c2', tool_call_id='8423e167-7342-42d3-ab3d-206e083c5ca4'), 
    
    AIMessage(content="The current weather in San Francisco is mostly overcast with a temperature of 14.41°C (57.94°F) and high humidity at 82%. It's a relatively cool day in the city, so you may want to pack a light jacket or sweater if you're planning to be outside for an extended period.", additional_kwargs={}, response_metadata={'model': 'llama3.2', 'created_at': '2026-07-20T09:15:54.597028Z', 'done': True, 'done_reason': 'stop', 'total_duration': 6126497500, 'load_duration': 264160000, 'prompt_eval_count': 115, 'prompt_eval_duration': 97839000, 'eval_count': 66, 'eval_duration': 5733463000, 'logprobs': None, 'model_name': 'llama3.2', 'model_provider': 'ollama'}, id='lc_run--019f7ecf-6382-71e3-8cb3-65fee8bcc88c-0', tool_calls=[], invalid_tool_calls=[], usage_metadata={'input_tokens': 115, 'output_tokens': 66, 'total_tokens': 181})
    ]
}












{'messages': [
    HumanMessage(content='Hi, my name is Ahmad', additional_kwargs={}, response_metadata={}, id='9cd9cdc1-8ae7-40a9-bf60-d546183a28ed'), 
    
    AIMessage(content='', additional_kwargs={}, response_metadata={'model': 'llama3.2', 'created_at': '2026-07-20T13:07:26.7718174Z', 'done': True, 'done_reason': 'stop', 'total_duration': 7593682400, 'load_duration': 3749085600, 'prompt_eval_count': 148, 'prompt_eval_duration': 2662831000, 'eval_count': 14, 'eval_duration': 1172726000, 'logprobs': None, 'model_name': 'llama3.2', 'model_provider': 'ollama'}, id='lc_run--019f7fa3-5808-72b3-885d-1a6f6bb232d1-0', tool_calls=[{'name': 'get_user_info', 'args': {}, 'id': 'e67fa8b6-a1b2-4017-a5b6-a850b2df6b63', 'type': 'tool_call'}], invalid_tool_calls=[], usage_metadata={'input_tokens': 148, 'output_tokens': 14, 'total_tokens': 162}), 
    
    ToolMessage(content='No user profile on file.', name='get_user_info', id='e7c15c96-8a72-45e4-a3df-09686171590c', tool_call_id='e67fa8b6-a1b2-4017-a5b6-a850b2df6b63'), AIMessage(content="Hello Ahmad! I don't have any information about you yet. How can I assist you today? Do you need help with something specific or would you like me to provide some general assistance?", additional_kwargs={}, response_metadata={'model': 'llama3.2', 'created_at': '2026-07-20T13:07:31.7149946Z', 'done': True, 'done_reason': 'stop', 'total_duration': 4935088700, 'load_duration': 283344200, 'prompt_eval_count': 93, 'prompt_eval_duration': 818669000, 'eval_count': 39, 'eval_duration': 3821225000, 'logprobs': None, 'model_name': 'llama3.2', 'model_provider': 'ollama'}, id='lc_run--019f7fa3-75ba-79d3-90c5-b40a4a099035-0', tool_calls=[], invalid_tool_calls=[], usage_metadata={'input_tokens': 93, 'output_tokens': 39, 'total_tokens': 132})]}








{'ls_integration': 'langchain_chat_model', 'thread_id': '019f847f-e989-7c10-b297-e88cc8a551dc', 'langgraph_step': 1, 'langgraph_node': 'model', 'langgraph_triggers': ('branch:to:model',), 'langgraph_path': ('__pregel_pull', 'model'), 'langgraph_checkpoint_ns': 'model:56489fa6-165a-df78-111a-4ee2602ef0ca', 'checkpoint_ns': 'model:56489fa6-165a-df78-111a-4ee2602ef0ca', 'ls_provider': 'google_genai', 'ls_model_name': 'gemini-3.1-flash-lite', 'ls_model_type': 'chat', 'ls_temperature': 0.0, 'ls_max_tokens': 500, 'lc_versions': {'langchain-core': '1.4.9', 'langchain': '1.3.14', 'langchain-google-genai': '4.2.7'}}
[]
{'ls_integration': 'langchain_chat_model', 'thread_id': '019f847f-e989-7c10-b297-e88cc8a551dc', 'langgraph_step': 1, 'langgraph_node': 'model', 'langgraph_triggers': ('branch:to:model',), 'langgraph_path': ('__pregel_pull', 'model'), 'langgraph_checkpoint_ns': 'model:56489fa6-165a-df78-111a-4ee2602ef0ca', 'checkpoint_ns': 'model:56489fa6-165a-df78-111a-4ee2602ef0ca', 'ls_provider': 'google_genai', 'ls_model_name': 'gemini-3.1-flash-lite', 'ls_model_type': 'chat', 'ls_temperature': 0.0, 'ls_max_tokens': 500, 'lc_versions': {'langchain-core': '1.4.9', 'langchain': '1.3.14', 'langchain-google-genai': '4.2.7'}}
[]
{'ls_integration': 'langchain_chat_model', 'thread_id': '019f847f-e989-7c10-b297-e88cc8a551dc', 'langgraph_step': 1, 'langgraph_node': 'model', 'langgraph_triggers': ('branch:to:model',), 'langgraph_path': ('__pregel_pull', 'model'), 'langgraph_checkpoint_ns': 'model:56489fa6-165a-df78-111a-4ee2602ef0ca', 'checkpoint_ns': 'model:56489fa6-165a-df78-111a-4ee2602ef0ca', 'ls_provider': 'google_genai', 'ls_model_name': 'gemini-3.1-flash-lite', 'ls_model_type': 'chat', 'ls_temperature': 0.0, 'ls_max_tokens': 500, 'lc_versions': {'langchain-core': '1.4.9', 'langchain': '1.3.14', 'langchain-google-genai': '4.2.7'}}
[]
{'ls_integration': 'langchain_create_agent', 'thread_id': '019f847f-e989-7c10-b297-e88cc8a551dc', 'langgraph_step': 2, 'langgraph_node': 'tools', 'langgraph_triggers': ('__pregel_push',), 'langgraph_path': ('__pregel_push', 0, False), 'langgraph_checkpoint_ns': 'tools:7a61060a-44d7-9d6d-c622-c67cb5635f9f'}
'4:46 PM'
{'ls_integration': 'langchain_chat_model', 'thread_id': '019f847f-e989-7c10-b297-e88cc8a551dc', 'langgraph_step': 3, 'langgraph_node': 'model', 'langgraph_triggers': ('branch:to:model',), 'langgraph_path': ('__pregel_pull', 'model'), 'langgraph_checkpoint_ns': 'model:a7ffca38-4b81-db5d-c0c7-b88662921093', 'checkpoint_ns': 'model:a7ffca38-4b81-db5d-c0c7-b88662921093', 'ls_provider': 'google_genai', 'ls_model_name': 'gemini-3.1-flash-lite', 'ls_model_type': 'chat', 'ls_temperature': 0.0, 'ls_max_tokens': 500, 'lc_versions': {'langchain-core': '1.4.9', 'langchain': '1.3.14', 'langchain-google-genai': '4.2.7'}}
[{'type': 'text', 'text': 'The current', 'index': 0}]
{'ls_integration': 'langchain_chat_model', 'thread_id': '019f847f-e989-7c10-b297-e88cc8a551dc', 'langgraph_step': 3, 'langgraph_node': 'model', 'langgraph_triggers': ('branch:to:model',), 'langgraph_path': ('__pregel_pull', 'model'), 'langgraph_checkpoint_ns': 'model:a7ffca38-4b81-db5d-c0c7-b88662921093', 'checkpoint_ns': 'model:a7ffca38-4b81-db5d-c0c7-b88662921093', 'ls_provider': 'google_genai', 'ls_model_name': 'gemini-3.1-flash-lite', 'ls_model_type': 'chat', 'ls_temperature': 0.0, 'ls_max_tokens': 500, 'lc_versions': {'langchain-core': '1.4.9', 'langchain': '1.3.14', 'langchain-google-genai': '4.2.7'}}
[{'type': 'text', 'text': ' time is 4:46 PM.', 'index': 0}]
{'ls_integration': 'langchain_chat_model', 'thread_id': '019f847f-e989-7c10-b297-e88cc8a551dc', 'langgraph_step': 3, 'langgraph_node': 'model', 'langgraph_triggers': ('branch:to:model',), 'langgraph_path': ('__pregel_pull', 'model'), 'langgraph_checkpoint_ns': 'model:a7ffca38-4b81-db5d-c0c7-b88662921093', 'checkpoint_ns': 'model:a7ffca38-4b81-db5d-c0c7-b88662921093', 'ls_provider': 'google_genai', 'ls_model_name': 'gemini-3.1-flash-lite', 'ls_model_type': 'chat', 'ls_temperature': 0.0, 'ls_max_tokens': 500, 'lc_versions': {'langchain-core': '1.4.9', 'langchain': '1.3.14', 'langchain-google-genai': '4.2.7'}}
[{'type': 'text', 'text': '', 'extras': {'signature': 'EjQKMgERTTIPP9xlPadHJwtFD2AZj0jRaaMBPpVvo0FJ0qOvLEyikPcV94R6N5H1+WixZkwa'}, 'index': 0}]
{'ls_integration': 'langchain_chat_model', 'thread_id': '019f847f-e989-7c10-b297-e88cc8a551dc', 'langgraph_step': 3, 'langgraph_node': 'model', 'langgraph_triggers': ('branch:to:model',), 'langgraph_path': ('__pregel_pull', 'model'), 'langgraph_checkpoint_ns': 'model:a7ffca38-4b81-db5d-c0c7-b88662921093', 'checkpoint_ns': 'model:a7ffca38-4b81-db5d-c0c7-b88662921093', 'ls_provider': 'google_genai', 'ls_model_name': 'gemini-3.1-flash-lite', 'ls_model_type': 'chat', 'ls_temperature': 0.0, 'ls_max_tokens': 500, 'lc_versions': {'langchain-core': '1.4.9', 'langchain': '1.3.14', 'langchain-google-genai': '4.2.7'}}
[]