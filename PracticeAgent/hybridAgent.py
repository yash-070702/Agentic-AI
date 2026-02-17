from langchain_aws import ChatBedrockConverse
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser


llm=ChatBedrockConverse(
    model='cohere.command-r-plus-v1:0',
    aws_access_key_id='',
    aws_secret_access_key='',
    region_name='us-east-1',
    max_tokens=200,
    temperature=0.5
)

template="""you are the customer support for the e commerce website
Answer the following support query : {query}"""

prompt=PromptTemplate.from_template(template)

def role_based_response(query):
    """Handle simple queries within predefined rules"""
    rules={
        "order status":"Your order is bring processed and should be delivered within 3 days",
        "shipping time":"Shipping takes 2 3 bussiness days , depending on ur location",
        "return policy":"You can return itme within 3 working days"
    }

    query=query.lower()
    for key , response in rules.items():
        if key in query:
            return response

    return None

def llm_response(query):
    """Generate a response using a language model for complex queries"""

    try:
        chain=prompt|llm|StrOutputParser()
        return chain.invoke({"query":query})

    except Exception as e :
        return f"error generating LLM response:{e}"

def hybrid_agent(query):
    response=role_based_response(query)

    if response:
        return response

    else:
        return llm_response(query)

query="i want to buy new clothes"
response=hybrid_agent(query)

print("response :",response)
