# Exercise 7: Customizable Writing Assistant

# You are creating a content generation assistant.

# Steps: 

# Write a PromptTemplate with two input variables:
# "Write a {tone} blog post on the topic: {topic}. Keep it under 100 words."

# Test the template with:

# {tone} = "formal", {topic} = "Future of Artificial Intelligence".

# {tone} = "casual", {topic} = "Tips for staying productive while working from home".

# Format and print the prompts.

# Run with an LLM to compare differences in tone.

# Goal: Understand dynamic prompt design for generating varied outputs.

from langchain_core.prompts import PromptTemplate
from langchain_aws import ChatBedrockConverse
from langchain_core.output_parsers import StrOutputParser

llm=ChatBedrockConverse(
    model="cohere.command-r-plus-v1:0",
    region_name='us-east-1',
    max_tokens=200
)

blog_template="""Write a {tone} blog post on the topic :{topic}. Keep it under 100 words"""

blog_prompt=PromptTemplate.from_template(blog_template)

chain=blog_prompt|llm|StrOutputParser()


response1=chain.invoke({"tone":"formal","topic":"Future of Artificial Intelligence"})

print("Printing response 1 -:")
print(response1)

response2=chain.invoke({"tone":"casual","topic":"Future of Artificial Intelligence"})
print('Printing response 2 -:')
print(response2)

