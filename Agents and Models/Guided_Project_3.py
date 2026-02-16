# =====================================
# GUIDED PROJECT 3
# RAG + Memory Financial Assistant
# =====================================

# Import modules
from langchain_classic.chains.combine_documents import create_stuff_documents_chain
from langchain_core.chat_history import InMemoryChatMessageHistory
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_aws import ChatBedrockConverse, BedrockEmbeddings
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_classic.chains import create_retrieval_chain

# Step 1: Load Financial Report PDF
loader = PyPDFLoader("financial_report.pdf")
documents = loader.load()

# Step 2: Split into Chunks
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=800,
    chunk_overlap=100
)
texts = text_splitter.split_documents(documents)

# Step 3: Initialize LLM
llm = ChatBedrockConverse(
    model='cohere.command-r-plus-v1:0',
    region_name='us-east-1',
    max_tokens=200
)

# Step 4: Setup Embeddings + Vector DB
embeddings = BedrockEmbeddings(
    model_id='cohere.embed-english-v3',
    region_name='us-east-1'
)

db = Chroma.from_documents(texts, embeddings)
retriever = db.as_retriever(search_kwargs={"k": 3})

# Step 5: Chat Prompt Template
chat_prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a financial report analyst. Use context below:\n<context>{context}</context>"),
    ("placeholder", "{chat_history}"),
    ("human", "{input}")
])

# Step 6: Create Retrieval Chain
docs_chain = create_stuff_documents_chain(llm, chat_prompt)
retriever_chain = create_retrieval_chain(retriever, docs_chain)

# Step 7: Setup Memory
store = {}

def get_session_history(session_id: str):
    if session_id not in store:
        store[session_id] = InMemoryChatMessageHistory()
    return store[session_id]

chain_with_memory = RunnableWithMessageHistory(
    retriever_chain,
    get_session_history,
    input_messages_key="input",
    history_messages_key="chat_history",
    output_messages_key="answer"
)

# Step 8: Run Queries
session_id = "Oct7"

queries = [
    "What is revenue growth in 2025?",
    "What risks were mentioned?"
]

for q in queries:
    response = chain_with_memory.invoke(
        {"input": q},
        config={"configurable": {"session_id": session_id}}
    )
    print("\nQ:", q)
    print("A:", response["answer"])

