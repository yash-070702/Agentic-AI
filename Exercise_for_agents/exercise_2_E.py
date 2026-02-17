# Exercise 2 E: Basic Prompt Template for Greeting Bot

# You are tasked to create a simple greeting bot using LangChain.

#  Steps:

# Import and initialize PromptTemplate from LangChain.

# Create a template: "You are a friendly assistant. Greet the user with their name: {name}".

# Format the prompt by passing "Alice" as the value for {name}.

# Print the final formatted prompt.

# Goal: Learn how to define and format a basic PromptTemplate.


from langchain_core.prompts import PromptTemplate
template="""
you are the freindly assistant . Greet the user with their name : {name}"""

prompt=PromptTemplate.from_template(template)
formatted_prompt=prompt.format(name='Alice')

print(formatted_prompt)

