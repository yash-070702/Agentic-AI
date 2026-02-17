from langchain_community.chat_message_histories import SQLChatMessageHistory
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnableWithMessageHistory
from langchain_core.output_parsers import StrOutputParser
from langchain_aws import ChatBedrockConverse

dpath="chat_memory.sqlite"


def get_session_history(session_id:str):
    return SQLChatMessageHistory(session_id=session_id,connection_string=f"sqlite:///{dpath}")

prompt=ChatPromptTemplate.from_template("""
You are a freindly AI assisstant that remembers user preferecnes 
Chat history:{history}
User:{input}
""")

llm=ChatBedrockConverse(
    model='cohere.command-r-plus-v1:0',
    aws_access_key_id='',
    aws_secret_access_key='',
    region_name='us-east-1',
    max_tokens=200,
    temperature=0.5
)

chat_chain=prompt|llm|StrOutputParser()

memory_agent=RunnableWithMessageHistory(
    chat_chain,
    get_session_history,
    input_messages_key='input',
    history_messages_key="history"
)

session_id='user1'

print(memory_agent.invoke({"input":"Hi i am data scientist"},config={"configurable":{"session_id":session_id}}))
print(memory_agent.invoke({"input":"My fav programming language is JS"},config={"configurable":{"session_id":session_id}}))