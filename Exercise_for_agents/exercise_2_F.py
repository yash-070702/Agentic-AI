# Exercise 6: Math Problem Solver Prompt

# You are building a tool that asks the model to solve math problems step by step.

# Steps:

# Create a PromptTemplate with two variables:
# "Solve the following math problem step by step and give the final answer. Problem: {problem}".

# Pass the value {problem} = "What is 45 divided by 9 plus 12?".

# Format and print the final prompt.

# Run it with an LLM and verify if the model explains the steps.

# Goal: Practice multi-variable PromptTemplate usage and structured instructions.

from langchain_core.prompts import PromptTemplate
from langchain_aws import ChatBedrockConverse
from langchain_core.output_parsers import StrOutputParser

llm=ChatBedrockConverse(model='cohere.command-r-plus-v1:0',
                       region_name='us-east-1',
                       max_tokens=200)

template="""
Solve the following math problem step by step and give the final answer 
Problem : {problem}
"""

prompt=PromptTemplate.from_template(template)
chain=prompt|llm|StrOutputParser()

response=chain.invoke({"problem":"What is 45 divided by 9 plus 12?"})
print(response)

