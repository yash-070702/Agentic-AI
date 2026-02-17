# Exercise 3: ConversationBufferWindowMemory for Limited Context

# You are building a resource-efficient assistant that only remembers the last few exchanges.

# Steps :

# Implement  ConversationBuffer Window Memory  using trim_messages and set k=2 (remembers only the last 2 messages).

# Connect it with an RunnableWithMessageHistory

# Run the following conversation:

# User: “I live in Paris.”

# User: “I love croissants.”

# User: “What’s my favorite food?”

# User: “Where do I live?”

# Observe: The assistant should remember the croissant but forget Paris because the memory window is limited.

# Goal: Understand windowed memory and trade-offs between recall vs. efficiency.


from langchain_core.prompts import ChatPromptTemplate
from langchain_core.chat_history import InMemoryChatMessageHistory
from langchain_core.runnables.history import RunnableWithMessageHistory 
from langchain_core.output_parsers import StrOutputParser
from langchain_aws import ChatBedrockConverse
from langchain_core.messages import trim_messages


llm=ChatBedrockConverse(model='cohere.command-r-plus-v1:0',
                       region_name='us-east-1',
                       max_tokens=200)
store={}

def get_session_history(session_id:str)->InMemoryChatMessageHistory:
    if session_id not in store:
        store[session_id]=InMemoryChatMessageHistory()
        
    messages=store[session_id].messages
    trimmed=trim_messages(messages=messages,
                         token_counter=len,
                         max_tokens=2,
                         strategy='last'
                         )
    store[session_id]=InMemoryChatMessageHistory(messages=trimmed)

    return store[session_id]

prompt=ChatPromptTemplate.from_messages([
    ("system","You are the helping assistant . Use the past conversation for the context and answer the following"),
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

session_id='user-1'

questions=[
    "I live in Paris",
    "I love croissants",
    "What is my favourite food",
    "where do i live"
]

print("Priting chat with bot")

for q in questions:
    response=chain_with_mem.invoke({"input":q},config={"configurable":{"session_id":session_id}})
    print("User:",q)
    print("AI:",response)



