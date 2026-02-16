# Guided Project 1: HR AI Assistant for Resume Screening
# Business Scenario
# A mid-sized IT company receives hundreds of resumes daily for open job roles. HR recruiters spend hours manually screening resumes to check if candidates match job descriptions. This process is time-consuming, repetitive, and prone to human bias.

# To solve this, the company wants to deploy an AI-powered HR Assistant that can:

# Read candidate resumes.
# Compare them against job descriptions.
# Summarize strengths and highlight relevant skills.
# Provide a recommendation (Shortlist/Reject) with a clear justification.
# This system will act as the first-level screening tool, helping HR teams reduce workload and focus only on qualified candidates.

# Problem Statement
# As an AI developer, your task is to build an AI Resume Screening Assistant using LangChain Prompt Templates and a HuggingFace LLM (not OpenAI). The assistant should:

# Accept resume text and job description as inputs.
# Extract and summarize the candidate’s strengths in 3–4 bullet points.
# Match candidate skills against the job requirements.
# Give a decision (Shortlist / Reject) with one-line reasoning.
# Steps to Solve the Problem

# Step 1: Load a HuggingFace Model / Amzon Bedrock Model

# Use HuggingFace’s pipeline with a fine-tuned instruction model (e.g., tiiuae/falcon-7b-instruct).
# Wrap it with HuggingFacePipeline so it integrates seamlessly with LangChain.
# Step 2: Define a Prompt Template

# Create a structured prompt with placeholders for:
# {resume_text} → Candidate’s resume.
# {job_description} → Job posting details.
# The prompt should clearly instruct the AI to:
# Summarize candidate strengths.
# Highlight skills matching the job.
# Recommend Shortlist/Reject with reasoning.
# Step 3: Create an LLM Chain

# Use LLMChain to connect the HuggingFace LLM with the prompt template.
# This ensures the AI always follows the structured format.
# Step 4: Run Example (Simulation)

# Provide a sample resume (e.g., Python, ML, SQL skills).
# Provide a job description (e.g., Data Engineer role requiring Python, SQL, cloud).
# Run the chain and observe the structured response:
# Bullet-point strengths.
# Matching skills.
# Shortlist/Reject recommendation.
 

# ==============================
# GUIDED PROJECT 1
# AI HR Resume Screening System
# ==============================

# Import required modules
from langchain_core.prompts import PromptTemplate
from langchain_aws import ChatBedrockConverse
from langchain_core.output_parsers import StrOutputParser

# Step 1: Initialize LLM (AWS Bedrock - Cohere Model)
llm = ChatBedrockConverse(
    model='cohere.command-r-plus-v1:0',
    aws_access_key_id='',
    aws_secret_access_key='',
    region_name='us-east-1',
    max_tokens=200
)

# Step 2: Create Prompt Template
# This template defines how the LLM should evaluate resumes
template = """
You are an AI HR Assistant. Your task is to screen resumes.

### Candidate Resume:
{resume_text}

### Job Description:
{job_description}

### Instructions:
1. Summarize strengths (3-4 bullet points).
2. Highlight matching skills.
3. Provide recommendation: "Shortlist" or "Reject" with reason.
"""

prompt = PromptTemplate.from_template(template)

# Step 3: Create Chain (Prompt → LLM → Output Parser)
chain = prompt | llm | StrOutputParser()

# Step 4: Sample Resume and Job Description
resume = """
John Doe, 5 years of experience in Python, Machine Learning, and Data Engineering.
Worked on cloud platforms like AWS and GCP. Strong in SQL and data pipelines.
"""

job_desc = """
Looking for a Data Engineer with 4+ years of experience in Python, SQL, and cloud platforms.
"""

# Step 5: Invoke Chain
result = chain.invoke({
    "resume_text": resume,
    "job_description": job_desc
})

print(result)
