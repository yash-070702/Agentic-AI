# Exercise 2: Web Search Agent for Knowledge Retrieval

# You are tasked to build an assistant that can answer current events questions by searching the web.

# Steps:

# Load the serpapi or tavily search tool (depending on availability).

# Create an agent that uses the search tool + LLM.

# Ask the agent:

# “What is the latest news about artificial intelligence in healthcare?”

# Observe how the agent retrieves real-time data before generating the response.

# Goal: Practice building an agent that integrates external APIs for knowledge..

from langchain_aws import ChatBedrockConverse
from langchain.agents import create_tool_calling_agent , AgentExecutor
from langchain_core.prompts import ChatPromptTemplate
from langchain_community.tools.tavily_search import TavilySearchResults
import os

os.environ["TAVILY_API_KEY"]="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"

llm=ChatBedrockConverse(
    model='cohere.command-r-plus-v1:0',
    region_name='us-east-1',
    max_tokens=200,
    temperature=0
)

search_tool=TavilySearchResults(max_results=5)
tools=[search_tool]

prompt=ChatPromptTemplate.from_messages([
    ("system","You are the helpful assistant . Use the search tool for the current events or the real time information"),
    ("human","{input}"),
    ("placeholder","{agent_scratchpad}")
])

agent=create_tool_calling_agent(
    llm=llm,
    prompt=prompt,
    tools=tools
)
agent_executor=AgentExecutor(
    agent=agent,
    tools=tools,
    verbose=True
)

response=agent_executor.invoke({"input":"what is the latest news related to IPL2026"})

print(response['output'])
