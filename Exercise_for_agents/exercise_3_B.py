# Exercise 2: Conversation Summary Memory for Long Chats
# Imagine you are building a customer support assistant. Since conversations can become long, the system should summarize previous messages instead of storing the entire chat history.

# Steps:
# Create a memory instance using InMemoryChatMessageHistory().

# Create an LCEL chain that generates a summary from the stored chat history.

# Simulate a conversation with at least 5 turns, such as questions about order status, shipping, or returns.

# After the 5th turn, generate and print the conversation summary using LangChain.

# Verify that the summary captures the essential context without storing the full text of the conversation.

# Goal: Learn conversation summarization memory for long interactions.

from langchain_core.prompts import PromptTemplate,ChatPromptTemplate
from langchain_core.chat_history import InMemoryChatMessageHistory
from langchain_core.runnables.history import RunnableWithMessageHistory 
from langchain_core.output_parsers import StrOutputParser
from langchain_aws import ChatBedrockConverse

llm=ChatBedrockConverse(model='cohere.command-r-plus-v1:0',
                       region_name='us-east-1',
                       max_tokens=200)
store={}

def get_session_history(session_id:str)->InMemoryChatMessageHistory:
    if session_id not in store:
        store[session_id]=InMemoryChatMessageHistory()

    return store[session_id]

prompt=ChatPromptTemplate.from_messages([
    ("system","You are the customer care assistant . Use the past conversation for the context and answer the following"),
    ("placeholder","{chat_history}"),
    ("human","{input}")
])


chain=prompt|llm|StrOutputParser()

chain_with_mem=RunnableWithMessageHistory(
    chain,
    get_session_history,
    history_message_key="chat_history",
    input_message_key="input"
)

session_id='user_1'

question=["Hi,I want to check my order status",
         "Yes my order id is 12345",
         "When will my order will be shipped",
         "Does it has return policy",
         "can i change my delivery address"]


print("Priting chat with bot")

for q in question:
    response=chain_with_mem.invoke({"input":q},config={"configurable":{"session_id":session_id}})
    print("User:",q)
    print("AI:",response)

response=chain_with_mem.invoke({"input":"Generate the summary of the chat we done till yet"},config={"configurable":{"session_id":session_id}})

print("Summary of the chat is ")
print(response)