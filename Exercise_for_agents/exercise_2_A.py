# Exercise 1: Create a Simple Q&A Prompt

# Build a Q&A assistant using LangChain by following the below given steps:
 

#  Steps:

# Use PromptTemplate in LangChain to create a prompt: "Answer the following question clearly and concisely: {question}".

# Pass a custom question like "What is the capital of  india?".

# Run the chain with an LLM (e.g., Amazon Bedrock or HuggingFace).

# Display the result.

# Goal: Learn how to design and run a basic prompt template in LangChain

from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_aws import ChatBedrockConverse

llm=ChatBedrockConverse(model='cohere.command-r-plus-v1:0',
                       aws_access_key_id='',
                       aws_secret_access_key='',
                       region_name='us-east-1',
                       max_tokens=200)



template="""
You are a teacher and helping a student to answer
so i will provide you with a question

your task is to generate the exact answer to the aksed question 

question to be answered  is {question}
"""

prompt=PromptTemplate.from_template(template)
chain=prompt|llm|StrOutputParser()

answer=chain.invoke({"question":"what us the capital of india"})

print(answer)

