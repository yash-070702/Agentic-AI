# Problem Statement:
# In this exercise, you will learn how to use Runnable to create a workflow that chains multiple steps together. The task is to create a mini Q&A assistant that:

# Reformulates the user’s question into a clearer version.

# Passes the reformulated question to the LLM.

# Returns the final structured answer with a short title and explanation.

# Steps to Solve:
# Import the required LangChain classes (RunnableSequence, PromptTemplate, and ChatOpenAI).

# Create a PromptTemplate that takes the user question and reformulates it into a clearer, more specific version.

# Create a second PromptTemplate that answers the reformulated question in a structured way with:

# A short title.

# A detailed explanation.

# Use RunnableSequence to chain these two templates together.

# Run the full pipeline with the input:
# "Why is the sky blue?"
# and print the structured answer.

from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableSequence
from langchain_aws import ChatBedrockConverse

llm=ChatBedrockConverse(
    model='cohere.command-r-plus-v1:0',
    region_name="us-east-1",
    max_tokens=200
)

reformulate_template="""
Reformulate the given question in more readable and understandable form
that question is : {question_to_change}
"""

reformulate_prompt=PromptTemplate.from_template(reformulate_template)

answer_template="""
answer the following question in structured and manner way
"""

answer_prompt=PromptTemplate.from_template(answer_template)

chain=RunnableSequence([reformulate_prompt ,llm ,answer_prompt , llm])

result=chain.invoke({"question_to_change":"why is sky blue"})
print(result)