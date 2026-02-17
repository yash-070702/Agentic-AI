from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_aws import ChatBedrockConverse

llm=ChatBedrockConverse(
    model='cohere.command-r-plus-v1:0',
    aws_access_key_id='',
    aws_secret_access_key='',
    region_name='us-east-1',
    max_tokens=200,
    temperature=0.5
)

template="""
you are the trip planner .break down the task into smaller , actionable stages and output each step in a clear and concise manner 
Task:{task}
output a step by step intinary with time and place
Steps:
"""

prompt=PromptTemplate.from_template(template)

chain=prompt|llm|StrOutputParser()

task="Plan a trip to mysore"
response=chain.invoke({"task":task})

print(response)