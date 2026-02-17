# Exercise 1: Build a Calculator Agent

# You are building an assistant that can solve math problems by deciding when to use a calculator tool.

# Steps:

# Import LangChain’s create_tool_calling_agent and load_tools.

# Create basic math tools for performing simple calculator operations.

# Create the tool calling agent that can use the tool when required.

# Run the following query:

# “What is (45 * 12) + 350?”

# Verify that the agent calls the calculator tool instead of hallucinating the answer.

# Goal: Learn how to set up a tool-using agent.

from langchain_aws import ChatBedrockConverse
from langchain.agents import create_tool_calling_agent,AgentExecutor
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.tools import tool

llm=ChatBedrockConverse(model='cohere.command-r-plus-v1:0',
                       region_name='us-east-1',
                       temperature=0,
                       max_tokens=200)

@tool
def calculator(exp:str)->str:
    """
    Evalutes the basic math expressions
    Example :"(45*12)+350"
    """
    try:
        result=eval(exp)
        return str(result)

    except Exception as e:
        return f"Error:{str(e)}"

tools=[calculator]

prompt=ChatPromptTemplate.from_messages([
    ("system","You are helpful assistant Use the Calculator tool for any math calculation"),
    ("human","{input}"),
    ("placeholder","{agent_scratchpad}")
])

agent=create_tool_calling_agent(
    llm=llm,
    tools=tools,
    prompt=prompt
)

agent_executor=AgentExecutor(
    agent=agent,
    tools=tools,
    verbose=True
)


response=agent_executor.invoke({"input":"What is (46*12)+159"})
print(response)
