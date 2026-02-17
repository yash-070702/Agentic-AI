# Exercise 3: Multi-Tool Agent (Calculator + Wikipedia)

# You are designing a hybrid research assistant that can perform math + look up facts.

# Steps:

# Load two tools:

# math tools created for simple  calculations / loading math-tool from LangChain

# wikipedia (or arxiv if installed) for fact lookup.

# Initialize an agent with both tools.

# Run queries like:

# “Who won the Nobel Prize in Physics in 2020? Multiply the number of winners by 3.”

# Verify that the agent first looks up the answer in Wikipedia, then uses the calculator tool.

# Goal: Understand how agents can reason step by step and chain multiple tools.

from langchain_aws import ChatBedrockConverse
from langchain.agents import create_tool_calling_agent , AgentExecutor , load_tools
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.tools import tool

llm=ChatBedrockConverse(model='cohere.command-r-plus-v1:0',
                       region_name='us-east-1',
                       max_tokens=200,
                       temperature=0)

wiki_tool=load_tools(['wikipedia'])[0]

@tool
def calculator(exp:str)->str:
    """Evalutaes the basic maths expression"""

    try:
        return eval(exp)

    except Exception as e:
        return f"error: {str(e)}"

tools=[wiki_tool,calculator]

prompt=ChatPromptTemplate.from_messages([
    ("system","You are the helpful assistant . Use wikipedia for facts and calculator for math"),
    ("human","{input}"),
    ("placeholder","{agent_scratchpad}")
])

agent=create_tool_calling_agent(
    llm=llm,
    prompt=prompt,
    tools=tools
)

agent_invoker=AgentExecutor(
    agent=agent,
    tools=tools,
    verbose=True
)

response=agent_invoker.invoke({"input":"Who won the nobel prize in 2020 ? Multiply the number of winners with 3"})

print(response['output'])