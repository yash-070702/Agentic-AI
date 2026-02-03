#this is example for pipelining chaining 
#firstly we will create summary over AI and then with second prompt we will understand it like a 10 year old boy 



from transformers import pipeline
from langchain_community.llms import HuggingFacePipeline
from langchain_core.prompts import PromptTemplate

# -----------------------------
# 1. Hugging Face model
# -----------------------------
hf_pipeline = pipeline(
    "text-generation",
    model="gpt2",
    max_new_tokens=80
)


llm = HuggingFacePipeline(pipeline=hf_pipeline)

# -----------------------------
# 2. Prompt 1 — Summary
# -----------------------------
summary_prompt = PromptTemplate(
    input_variables=["topic"],
    template="Write a short 2 line summary about {topic}."
)

# -----------------------------
# 3. Prompt 2 — Simple Explanation
# -----------------------------
explain_prompt = PromptTemplate(
    input_variables=["summary"],
    template="Explain the following summary in very simple words:\n{summary}"
)

# -----------------------------
# 4. STEP 1 — Generate summary
# -----------------------------
summary = llm.invoke(
    summary_prompt.format(topic="Artificial Intelligence")
)

# -----------------------------
# 5. STEP 2 — Explain summary
# -----------------------------
final_output = llm.invoke(
    explain_prompt.format(summary=summary)
)

print("SUMMARY:\n", summary)
print("\nEXPLANATION:\n", final_output)
