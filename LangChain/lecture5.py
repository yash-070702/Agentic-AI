from transformers import pipeline
from langchain_community.llms import HuggingFacePipeline
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableMap

# -------------------- LLM SETUP --------------------
hf_pipeline = pipeline(
    task="text-generation",
    model="Salesforce/codegen-350M-mono",
    max_new_tokens=300
)

llm = HuggingFacePipeline(pipeline=hf_pipeline)

# -------------------- CODE GENERATOR --------------------
code_generator_prompt = PromptTemplate(
    input_variables=["requirement"],
    template="""
You are an expert software developer.

Generate clean Python code for the following requirement.

Requirement:
{requirement}

Rules:
- Only output code
- Add comments where useful
"""
)

code_generator_chain = (
    code_generator_prompt
    | llm
    | StrOutputParser()
)

# -------------------- CODE REVIEWER --------------------
code_reviewer_prompt = PromptTemplate(
    input_variables=["code"],
    template="""
You are a senior code reviewer.

Review the following code:
{code}

Provide:
1. Improvements
2. Edge cases
3. Best practices suggestions

Do NOT rewrite the code.
"""
)

code_reviewer_chain = (
    code_reviewer_prompt
    | llm
    | StrOutputParser()
)

# -------------------- PIPELINE --------------------
full_chain = (
    RunnableMap({"code": code_generator_chain})
    | code_reviewer_chain
)

result = full_chain.invoke({
    "requirement": "Write a Python function to check whether a string is a palindrome."
})

print(result)
