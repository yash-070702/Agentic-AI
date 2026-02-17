
# Problem Statement:

# Build a basic chain using LangChain. The goal is to help you understand how PromptTemplate and LLMChain work together to create structured prompts and generate outputs.

# Steps to Solve:

# Import the required LangChain classes (PromptTemplate, LLMChain, and an LLM ).

# Define a PromptTemplate that asks the model to:

# Take a topic as input.

# Generate a short explanation in simple terms.

# Create an LLMChain using the PromptTemplate and the chosen model.

# Run the chain with the topic "Quantum Computing" and print the output.

# Modify the chain so that the model also provides one real-world application of the concept.

# =========================================
# EXERCISE 1 A
# Topic Explanation + Real-Life Example
# =========================================

from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_aws import ChatBedrockConverse

# Step 1: Initialize LLM
llm = ChatBedrockConverse(
    model='cohere.command-r-plus-v1:0',
    region_name='us-east-1',
    max_tokens=200
)

# Step 2: Create Explanation Prompt
template = """
You are a tutor explaining to children.
Explain the topic in simple words.

Topic: {topic}
"""

prompt = PromptTemplate.from_template(template)
chain = prompt | llm | StrOutputParser()

# Step 3: Generate Summary
summary = chain.invoke({"topic": "Quantum Computing"})
print(summary)

# Step 4: Generate Real-Life Example
template2 = """
Based on this explanation, give a real-life example:

Explanation: {summary}
"""

prompt2 = PromptTemplate.from_template(template2)
chain2 = prompt2 | llm | StrOutputParser()

example = chain2.invoke({"summary": summary})
print(example)
