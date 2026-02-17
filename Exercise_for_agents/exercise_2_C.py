
# Exercise 3: Structured Output Prompt (JSON Format)

# Write a LangChain based code to extract structured data from a text. Folow the steps given below:
 

#  Steps :

# Provide the following input text:
# "Tesla reported a revenue of $24 billion in Q2 2023 with a net profit of $2.7 billion."

# Create a prompt in LangChain: "Extract the company name, revenue, and net profit from the following text and return it in JSON format: {text}".

# Run the chain and check if the model produces valid JSON.

# Parse the JSON response in Python and print each field.

# Goal: Learn structured prompting for data extraction.

from langchain_core.prompts import PromptTemplate
from langchain_aws import ChatBedrockConverse
import json 

llm=ChatBedrockConverse(model='cohere.command-r-plus-v1:0',
                       region_name="us-east-1",
                       max_tokens=200)

text="Tesla reported a revenue of $24 billion in Q2 2023 with a net profit of $2.7 billion"

template="""
I will provide you with the text and ur task is to exract the company name , revenue and net profit from the given text . the text is {text}
JSON Format:{{
"company":"",
"revenue":"",
"net_profit":""
}}
"""

jsonprompt=PromptTemplate.from_template(template)
formatted_prompt=jsonprompt.format(text=text)

response=llm.invoke(formatted_prompt)

print(response.content)

