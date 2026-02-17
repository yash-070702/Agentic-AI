from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_aws import ChatBedrockConverse
from langchain_core.runnables import RunnableLambda

llm = ChatBedrockConverse(
    model_id="amazon.nova-lite-v1:0",
    region_name = "us-east-1",
    temperature = 0.5,
    max_tokens = 100
)

knowledge_base = {
    "Mysore Palace": "The Palace of Mysore (also known as the Amba Vilas Palace)",
    "K.R.S": " One of the famous dams of South India, Krishna Raja Sagara Dam",
    "Mysore Zoo": "To connect visirors and animals through exemplary animal welfare"
}

def lookup_knowledge(question: str):
    for key, response in knowledge_base.items():
        if key.lower() == question.lower():
            return response
    return "I dont have an specific reponse about this question"

template = """
        You are an helpful agent, use the given context only to answer the question
        if answer is not found in the context then just repsond info is not available
        Context: {context}
        Question: {question}

        Anser briefly and factually
    """

prompt = PromptTemplate.from_template(template)

reactive_agent = (
    RunnableLambda(lambda x : {
        "context": lookup_knowledge(x["question"]),
        "question": x["question"]
    })
    | prompt
    | llm
    | StrOutputParser()
)

print("A", reactive_agent.invoke({"question": "K.R.S"}))