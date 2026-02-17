# Exercise 3: Load and Split Documents for Chunking

# You are preparing documents for use in a RAG (Retrieval-Augmented Generation) pipeline.

# Steps:

# Take a long text file (at least 200–300 words).

# Use TextLoader to load it into LangChain.

# Apply CharacterTextSplitter with chunk size = 100 and overlap = 20.

# Print the number of chunks created and display at least the first 2 chunks.

# Goal: Learn document splitting & chunking for better retrieval.

from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import CharacterTextSplitter

loader=TextLoader("Ozone_Layer_depletion.txt")
documents=loader.load()

text_splitter=CharacterTextSplitter(
    chunk_size=100,
    chunk_overlap=20
)

chunks=text_splitter.split_documents(documents)

print("Number of Chunks Created",len(chunks))
print("first chunk content\n")
print(chunks[0].page_content)


print("="*25)

print("second chunk content\n")
print(chunks[1].page_content)
