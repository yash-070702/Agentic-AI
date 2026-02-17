from langchain_classic.agents import initialize_agent , AgentType
from langchain.tools import tool
from langchain.tools import DuckDuckGoSearchResults
from langchain_aws import ChatBedrockConverse

llm=ChatBedrockConverse(
    model='cohere.command-r-plus-v1:0',
    aws_access_key_id='',
    aws_secret_access_key='',
    region_name='us-east-1',
    max_tokens=200,
    temperature=0.5
)

@tool 
def calculator(exp:str)->str:
    """we done calculation"""
    try:
        result=eval(exp)
        return str(result)

    except Exception as e:
        return f"error in calculation : {str(e)}"

@tool 
def web_search(query:str)->str:
    """we are doing websearch"""
    search=DuckDuckGoSearchResults()
    return search.run(query)


tools=[calculator,web_search]

agent=initialize_agent(
    tools=tools,
    llm=llm,
    agent_type=AgentType,
    verbose=True
)


query1=5+8
response1=agent.run(query1)
print("response 1 :",response1)

query2='Who is the president of USA?'
response2=agent.run(query2)
print("response 2 :",response2)