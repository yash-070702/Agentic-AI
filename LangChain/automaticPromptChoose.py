# ===================== IMPORTS =====================
from transformers import pipeline
from langchain_community.llms import HuggingFacePipeline
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

from langchain_core.runnables import RunnableLambda, RunnableBranch


# ===================== LLM SETUP =====================
hf_pipeline = pipeline(
    task="text2text-generation",
    model="google/flan-t5-base",
    max_new_tokens=300
)

llm = HuggingFacePipeline(pipeline=hf_pipeline)


# ===================== PROMPT TEMPLATES =====================

definition_prompt = PromptTemplate(
    input_variables=["question"],
    template="Define the following concept clearly:\n{question}"
)

explain_prompt = PromptTemplate(
    input_variables=["question"],
    template="Explain the following in detail with examples:\n{question}"
)

code_prompt = PromptTemplate(
    input_variables=["question"],
    template="Answer the following coding question with explanation:\n{question}"
)


# ===================== ROUTER FUNCTION =====================

def route_question(inputs):
    question = inputs["question"].lower()

    if "what is" in question or "define" in question:
        route = "definition"
    elif "how" in question or "why" in question:
        route = "explain"
    elif "code" in question or "implement" in question:
        route = "code"
    else:
        route = "explain"

    # IMPORTANT: keep BOTH route + question
    return {
        "route": route,
        "question": inputs["question"]
    }


# ===================== BRANCH =====================

branch = RunnableBranch(
    (
        lambda x: x["route"] == "definition",
        definition_prompt | llm | StrOutputParser()
    ),
    (
        lambda x: x["route"] == "explain",
        explain_prompt | llm | StrOutputParser()
    ),
    (
        lambda x: x["route"] == "code",
        code_prompt | llm | StrOutputParser()
    ),
    # Default branch (safety net)
    explain_prompt | llm | StrOutputParser()
)


# ===================== FINAL CHAIN =====================

chain = (
    RunnableLambda(route_question)
    | branch
)


# ===================== TESTING =====================

print("\n--- TEST 1 ---")
print(chain.invoke({"question": "What is LangChain?"}))

print("\n--- TEST 2 ---")
print(chain.invoke({"question": "How does memory work in LangChain?"}))

print("\n--- TEST 3 ---")
print(chain.invoke({"question": "Write code to reverse a string in Python"}))
