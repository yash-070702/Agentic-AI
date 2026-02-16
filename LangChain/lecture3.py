

from transformers import pipeline
from langchain_community.llms import HuggingFacePipeline
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
# Updated Import Path
from langchain.memory import ConversationBufferMemory
from langchain_core.runnables import RunnablePassthrough

# 1. Initialize the HuggingFace Pipeline
hf_pipeline = pipeline(
    "text-generation",
    model="google/flan-t5-base",
    max_new_tokens=200
)

llm = HuggingFacePipeline(pipeline=hf_pipeline)

# 2. Initialize Memory
# Set memory_key="history" to match your prompt variable
memory = ConversationBufferMemory(
    memory_key="history", 
    return_messages=False  # Set to False if your prompt expects a single string block
)

# 3. Define the Prompt
prompt = PromptTemplate(
    input_variables=["history", "question"],
    template="""
You are a helpful tutor.

User question:
{question}

Answer clearly and simply.
"""
)

# 4. Build the Chain using LCEL
# We use a helper function to load history safely
chain = (
    {
        "history": lambda x: memory.load_memory_variables({})["history"],
        "question": RunnablePassthrough()
    }
    | prompt
    | llm
    | StrOutputParser()
)

# 5. Execution
# Note: When using the dict in step 4, pass the string directly or adjust the dict
question1 = "What is LangChain?"
response1 = chain.invoke(question1)
print("AI:", response1)

# Save to memory
memory.save_context(
    {"question": question1},
    {"output": response1}
)

question2 = "Why is it useful?"
response2 = chain.invoke(question2)
print("AI:", response2)

# Save to memory
memory.save_context(
    {"question": question2},
    {"output": response2}
)