from transformers import pipeline
from langchain_community.llms import HuggingFacePipeline
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

from langchain_core.runnables import RunnableMap, RunnableBranch

hf_pipeline = pipeline(
    "text-generation",
    model="google/flan-t5-base",
    max_new_tokens=200
)

llm1 = HuggingFacePipeline(pipeline=hf_pipeline)

template1 = """You are a writer. Given the name of the bird and the color of it, it is your job to write a brief note about the bird.
Name: {name}
Color: {color}
Note: This is a brief note about the above mentioned bird: """



prompt1=PromptTemplate(
    input_variables=["name", "color"],
    template=template1 
)


# prompt1 = PromptTemplate.from_template(template1)
chain1 = prompt1 | llm1 | StrOutputParser()  

template2 = """You are a reviewer of the content. Given the summary about a bird, it is your job to write a review for that summary.
Bird Summary: {summary}
Review of summary:"""

prompt2=PromptTemplate(
    input_variables=["summary"],
    template=template2 
)

# prompt2 = PromptTemplate.from_template(template2)
chain2 = prompt2 | llm1 | StrOutputParser()

# Approach 1 This maps inputs to chain1 and feeds its output to chain2
full_chain = RunnableMap({
    "summary": chain1
}) | chain2


result = full_chain.invoke({"name": "Pigeon", "color": "Blue and green"},verbose=True)
print("Final Review:\n", result)