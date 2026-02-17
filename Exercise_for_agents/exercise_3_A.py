# Exercise 1: Build a Chatbot with Simple ConversationBufferMemory

# You are tasked to build a basic chatbot that remembers previous user messages.

# Steps:

# Initialize a ConversationBufferMemory in LangChain.

# Connect it to an LLMChain with a simple prompt template like:
# “You are a helpful assistant. Use the past conversation for context. Current input: {input}”.

# Start a chat session:

# User: “My name is Sarah.”

# User: “What’s my name?”

# Run the chain and check if the model remembers the user’s name.

# Goal: Learn how to use buffer memory for storing complete chat history.

from langchain_core.prompts import ChatPromptTemplate
from langchain_core.chat_history import InMemoryChatMessageHistory
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_core.output_parsers import StrOutputParser
from langchain_aws import ChatBedrockConverse

llm = ChatBedrockConverse(model='cohere.command-r-plus-v1:0',
                         region_name='us-east-1',
                         max_tokens=200)

store={}
def get_session_history(session_id:str)->InMemoryChatMessageHistory:
    if session_id not in store:
        store[session_id]=InMemoryChatMessageHistory()
    return store[session_id]

prompt=ChatPromptTemplate.from_messages([
    ("system","You are assistant . Use the past conversation for the context"),
    ("placeholder","{chat_history}"),
    ("human","{input}")
])
chain = prompt|llm|StrOutputParser()

chain_with_mem=RunnableWithMessageHistory(
    chain,
    get_session_history,
    input_message_key="input",
    history_message_key="chat_history"
)

session_id='user-1'

response_1=chain_with_mem.invoke({"input":"My name is Yash"},config={"configurable":{"session_id":session_id}})

print("User:My name is Yash")
print("Bot:",response_1)

response_2=chain_with_mem.invoke({"input":"What is My name ?"},config={"configurable":{"session_id":session_id}})
print("User:What is my Name ?")
print("Bot:",response_2)
