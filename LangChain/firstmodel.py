

#################################
#################################
# Introduction to Language Models without LangChain

# from transformers import pipeline

# # load a text generation model
# generator = pipeline(
#     "text-generation",
#     model="gpt2"
# )

# # give a prompt
# response = generator(
#     "Explain artificial intelligence in simple words",
#     max_length=50,
#     truncation=True
# )


# print(response[0]["generated_text"])


#################################
#################################
# Introduction to Language Models with controlled parameters    

# from transformers import pipeline, set_seed
# # Load GPT-2 text generation pipeline
# generator = pipeline("text-generation", model="gpt2")
# # Prompt
# prompt = "The best way to learn coding is"
# # Fix seed for reproducibility
# set_seed(42)
# # Different temperatures to test
# temperatures = [0.1, 0.5, 1.0, 1.5]
# # Generate responses for each temperature
# for temp in temperatures:
#     output = generator(
#         prompt,
#         max_length=40,
#         num_return_sequences=1,
#         temperature=temp
#     )
#     print(f"\n=== Temperature = {temp} ===")
#     print(output[0]["generated_text"])

#################################
#################################

# Introduction to Language Models with LangChain

from langchain_community.llms import HuggingFacePipeline
from langchain_core.prompts import PromptTemplate
from transformers import pipeline

hf_pipeline = pipeline(
    "text-generation",
    model="gpt2",
    max_length=100,
    truncation=True
)

llm = HuggingFacePipeline(pipeline=hf_pipeline)

prompt = PromptTemplate(
    input_variables=["topic"],
    template="Explain {topic} in very simple words for a beginner."
)

response = llm.invoke(prompt.format(topic="Artificial Intelligence"))

print(response)
