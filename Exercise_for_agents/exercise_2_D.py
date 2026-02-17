# Exercise 4 : Role-based Prompt for an Interview Bot

# Write a LangChain code to build a mock interview assistant by following the below given steps:
 

# Steps for Students:

# Write a LangChain prompt:
# "You are a technical interviewer for a Data Scientist role. Ask me one question about machine learning. Wait for my answer. Then, provide constructive feedback and ask the next question."

# Implement this in LangChain using PromptTemplate and LLMChain.

# Run the chain and interact with the model for at least 3 questions.

# Note how different prompt wording changes the style of interview questions.

# Goal: Understand role-based prompting and iterative interaction.


from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_aws import ChatBedrockConverse

llm=ChatBedrockConverse(model='cohere.command-r-plus-v1:0',
                        aws_access_key_id='',
                        aws_secret_access_key='',
                        region_name='us-east-1',max_tokens=200)

template="""
suppose you are the interviewer and your task is to ask one question about the data science i will answer it than your task is to review it 
you suppose to provide the constructive feedback . Then ask the next machine learning question

Candidate's previous answer:
{previous_answer}
"""

interview_prompt=PromptTemplate.from_template(template)

chain=interview_prompt|llm|StrOutputParser()

candidate_ans=[
    'Machine learning is a subset of AI where models learns patterns from the data',
    "Overfitting occurs when a model perform well on training data but poorly on unseen data",
    "Regularism reduces overfitting by penalizing large weights"
]

prevoius_ans='None . Start the inteview '

for i in range(3):
    response=chain.invoke({"previous_answer":"previous_answer"})
    print("Printing Response",i+1)
    print(response)
    previous_answer=candidate_ans[i]