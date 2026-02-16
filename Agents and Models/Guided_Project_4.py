# Guided Project 4: AI Job Interview Coach
# Business Scenario
# In the modern job market, candidates often face challenges in preparing for interviews in a structured, confident, and professional manner. HR teams and career counselors seek an AI-powered Interview Coach that can simulate realistic interview scenarios, evaluate candidate responses, and provide constructive feedback.

# The goal is to build a Job Interview Coaching Assistant using LangChain that leverages Prompt Templates and Few-Shot Examples. By exposing the AI to examples of strong and weak responses, the assistant can guide learners toward delivering structured, impactful, and professional answers.

# Problem Statement
# Design and implement an AI Interview Coach using LangChain that:

# Utilizes a Prompt Template to enforce structured responses (e.g., introduction, main answer, feedback).
# Incorporates Few-Shot Examples to demonstrate what constitutes strong versus weak interview answers.
# Simulates realistic interview questions across multiple domains (e.g., software engineering, data science, business analysis).
# Provides personalized, step-by-step feedback to help candidates improve their performance.
# Step-by-Step Approach
# Step 1: Load an Open-Source LLM

# Use a Hugging Face model (e.g., tiiuae/falcon-7b-instruct or google/flan-t5-base) integrated via LangChain.
# Step 2: Define a Prompt Template

# Create a template with placeholders such as:

# {job_role} → target role for the interview
# {interview_question} → question asked by the interviewer
# {candidate_response} → candidate’s answer to be evaluated
# Step 3: Add Few-Shot Examples

# Provide 2–3 examples of interview questions with both weak and strong answers.
# Demonstrate how structured feedback should be presented.
# Step 4: Build the Chain

# Use FewShotPromptTemplate in LangChain to combine examples with the dynamic template.
# Step 5: Simulate Interview Q&A

# User provides a job role and candidate response.

# The system:

# Reframes the candidate’s answer.
# Compares it against strong examples.
# Provides structured feedback, including strengths, areas for improvement, and final recommendations.
# Step 6: Test with Sample Questions Example questions:

# “Tell me about yourself.”
# “Why do you want to join our company?”
# “Explain a challenging project you worked on.”
# Step 7: Evaluation & Enhancement

# Ensure the system maintains a professional, coaching-oriented tone.
# Test across different roles (e.g., Software Engineer, Data Analyst, Business Analyst).
# Extend to multi-turn sessions where the AI recalls prior candidate responses.


# =========================================
# GUIDED PROJECT 4
# AI Interview Feedback Coach
# Few-Shot Prompting Example
# =========================================

# Import required modules
from langchain_core.prompts import FewShotPromptTemplate, PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_aws import ChatBedrockConverse

# Step 1: Initialize LLM
llm = ChatBedrockConverse(
    model='cohere.command-r-plus-v1:0',
    region_name='us-east-1',
    max_tokens=200
)

# Step 2: Provide Few-Shot Examples
# These examples teach the model how to evaluate answers
examples = [
    {
        "interview_question": "Tell me about yourself",
        "candidate_response": "I like coding.",
        "feedback": "Weak answer. Lacks structure and achievements."
    },
    {
        "interview_question": "Tell me about yourself",
        "candidate_response": "I am a backend engineer with 5 years of experience in Python and cloud systems.",
        "feedback": "Strong answer. Structured and professional."
    }
]

# Step 3: Define Example Format
example_template = """
Interview Question: {interview_question}
Candidate Response: {candidate_response}
Feedback: {feedback}
"""

example_prompt = PromptTemplate.from_template(example_template)

# Step 4: Define Final Prompt Structure
overall_template = """
You are an AI Interview Coach.

Evaluate the candidate's answer and provide:

1. Strengths
2. Improvements
3. Final Recommendation (Strong / Weak)

Interview Question: {interview_question}
Candidate Response: {candidate_response}
Feedback:
"""

# Step 5: Create Few-Shot Prompt
prompt = FewShotPromptTemplate(
    examples=examples,
    example_prompt=example_prompt,
    suffix=overall_template,
    input_variables=["interview_question", "candidate_response"]
)

# Step 6: Create Chain
chain = prompt | llm | StrOutputParser()

# Step 7: Test
response = chain.invoke({
    "interview_question": "Explain a challenging project you worked on.",
    "candidate_response": "I migrated legacy databases to cloud and improved performance by 40%."
})

print(response)
