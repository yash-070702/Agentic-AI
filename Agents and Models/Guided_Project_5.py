# Guided Project 5: AI Email Tone Improver 
# Business Scenario
# In today’s fast-paced workplace, email remains the primary mode of communication. However, employees often send emails that may sound rude, abrupt, or unprofessional due to time pressure or limited writing skills. Such emails can damage client relationships, create misunderstandings, and negatively affect workplace culture.

# To address this, the organization wants to deploy an AI-powered assistant that can automatically rewrite draft emails into polished, polite, and professional messages. This will help employees maintain a consistent communication standard without requiring extensive writing training.

# Problem Statement
# The business requires an AI Email Tone Improver that:

# Accepts raw or unpolished email drafts written by users.
# Analyzes tone, politeness, and professionalism.
# Suggests improved versions of the emails while retaining their original meaning.
# Functions without heavy fine-tuning by leveraging Few-Shot Prompting in LangChain.
# Step-by-Step Approach
# Step 1: Define Business Goal

# Build an AI assistant that transforms employee draft emails into polished and professional versions.
# Ensure the system is lightweight, explainable, and customizable.
# Step 2: Choose Model & Framework

# Use LangChain for orchestration.
# Use Hugging Face models (e.g., FLAN-T5, Falcon, or LLaMA-based instruct models) for open-source generation.
# Avoid dependency on proprietary APIs (e.g., OpenAI).
# Step 3: Design Few-Shot Examples

# Create a small dataset of poorly written emails (rude/abrupt/unpolished) and their improved versions (professional, polite, concise).
# Use these examples in the FewShotPromptTemplate to guide the model.
# Step 4: Define Prompt Template

# Use a system-style instruction:
# “You are an AI Email Assistant. Rewrite the draft email into a polite, professional, and concise format.”
# Insert few-shot examples into the template to demonstrate expected behavior.
# Step 5: Implement with LangChain

# Load the Hugging Face model via HuggingFacePipeline.
# Build a FewShotPromptTemplate with curated examples.
# Create a LangChain LLMChain that connects the model with the prompt.
# Step 6: Run and Test

# Input different raw email drafts such as:
# “Send the file now.”
# “Why didn’t you reply yet?”
# “Meeting cancelled. Tell everyone.”
# Verify that the AI rewrites them into clear, professional messages.


# =========================================
# GUIDED PROJECT 5
# AI Email Polishing Assistant
# =========================================

from langchain_core.prompts import FewShotPromptTemplate, PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_aws import ChatBedrockConverse

# Step 1: Initialize LLM
llm = ChatBedrockConverse(
    model='cohere.command-r-plus-v1:0',
    region_name='us-east-1',
    max_tokens=200
)

# Step 2: Few-Shot Email Examples
examples = [
    {
        "draft_email": "Send me the report ASAP.",
        "improved_email": "Hi team, could you please share the report at your earliest convenience?"
    },
    {
        "draft_email": "Where is my refund?",
        "improved_email": "Hello, I wanted to follow up regarding my refund status."
    }
]

# Step 3: Example Template
example_template = """
Draft Email: {draft_email}
Improved Email: {improved_email}
"""

example_prompt = PromptTemplate.from_template(example_template)

# Step 4: Final Prompt
overall_template = """
You are an AI Email Assistant.
Rewrite emails to sound polite and professional.

Draft Email: {draft_email}
Improved Email:
"""

prompt = FewShotPromptTemplate(
    examples=examples,
    example_prompt=example_prompt,
    suffix=overall_template,
    input_variables=["draft_email"]
)

# Step 5: Create Chain
chain = prompt | llm | StrOutputParser()

# Step 6: Test
test_email = "Give me the slides fast."
result = chain.invoke({"draft_email": test_email})

print("Improved:", result)
