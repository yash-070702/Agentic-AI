# Exercise 8: Structured Information Extractor

# You are designing a prompt to extract structured details from text.

# Steps:

# Create a PromptTemplate with one variable:
# "Extract the following details from the text: Person’s Name, Age, and City. Return the output in JSON format. Text: {text}".

# Use this input text:
# "My name is Sarah, I am 29 years old, and I live in New York City."

# Format the prompt with the text above.

# Run with an LLM and check if the output is valid JSON.

# Goal: Learn how to design prompt templates for structured outputs.

from langchain_core.prompts import PromptTemplate
from langchain_aws import ChatBedrockConverse
import json
from langchain_core.output_parsers import StrOutputParser

llm=ChatBedrockConverse(model='cohere.command-r-plus-v1:0',
                       region_name="us-east-1",
                       max_tokens=200)

extract_temp="""
extract the following details from the text
-Person Name 
-Age
-city

Return the output strictly in valid json format
Text:{text}

JSON Format:

"name":"",
"age":"",
"city":""

"""

extract_prompt=PromptTemplate.from_template(extract_temp)

chain=extract_prompt | llm | StrOutputParser()

response=chain.invoke({"text":"My name is Yash , I am 23 years old and I live in Saharanpur"})
print(response)

parsed_op=json.loads(response)
print(parsed_op)