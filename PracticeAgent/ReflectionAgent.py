from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_aws import ChatBedrockConverse
import requests
from bs4 import BeautifulSoup


llm=ChatBedrockConverse(
    model='cohere.command-r-plus-v1:0',
    aws_access_key_id='',
    aws_secret_access_key='',
    region_name='us-east-1',
    max_tokens=200,
    temperature=0.5
)

url="https://timesofindia.indiatimes.com/business/india-business/akash-ambani-showcases-jios-ai-ecosystem-to-pm-modi-at-india-ai-impact-summit-2026/articleshow/128432179.cms"

html=requests.get(url).text
soup=BeautifulSoup(html,'html.parser')
article_text=" ".join([p.get_text() for p in soup.find_all('p')][:8])

template="""
Summarize the following text in 5 concise sentences
{article}"""
summary_prompt=PromptTemplate.from_template(template)

chain=summary_prompt|llm|StrOutputParser()
reflection_prompt=PromptTemplate.from_template("""
here is the summary 
{summary}
Reflect on clarity , conciseness , and engagement . improve it 
""")

reflector=reflection_prompt|llm|StrOutputParser()

response1=chain.invoke({"article":article_text})
print("Response 1 :",response1)


print("*"*25)
response2=reflector.invoke({"summary":response1})
print("Response 2 : ",response2)