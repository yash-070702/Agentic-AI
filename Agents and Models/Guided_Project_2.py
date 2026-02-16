# Guided Project 2: Research Paper Summarizer 
# Business scenario
# A university research office and multiple engineering teams routinely ingest dozens of new research papers each week. Researchers and product managers need fast, reliable summaries that extract the core problem, the method proposed, and the key findings so they can triage, synthesize literature reviews, and identify promising approaches quickly. Manually reading every paper is time-consuming and creates a bottleneck for decision-making.

# An automated AI Research Assistant that reads uploaded PDF papers and produces structured three-part summaries (Problem / Method / Findings) will accelerate literature review, improve knowledge discovery, and reduce time-to-insight for researchers.

# Problem Statement
# Build an automated Contract/Research Paper Summarizer that:

# Accepts a PDF (example filename: default.filename).

# Download the research paper from here >> research_paper.pdf

# Extracts readable text from the PDF and processes the content.

# Uses a prompt-driven LLM workflow to produce a structured summary with three sections:

# Problem Statement

# Proposed Method

# Key Findings

# Returns the summary in a predictable, machine-friendly format suitable for ingestion into a knowledge base.

# Works without using proprietary OpenAI APIs (use open-source LLMs).


# =====================================
# GUIDED PROJECT 2
# Academic Document Summarizer
# =====================================

# Import required modules
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_aws import ChatBedrockConverse

# Step 1: Define Chunking Parameters
CHUNK_SIZE = 1000
CHUNK_OVERLAP = 100

# Step 2: Load PDF File
loader = PyPDFLoader("research_paper.pdf")
pages = loader.load()

# Step 3: Split into Chunks
splitter = RecursiveCharacterTextSplitter(
    chunk_size=CHUNK_SIZE,
    chunk_overlap=CHUNK_OVERLAP
)
docs = splitter.split_documents(pages)

# Step 4: Initialize LLM
llm = ChatBedrockConverse(
    model='cohere.command-r-plus-v1:0',
    region_name='us-east-1',
    max_tokens=200
)

# Step 5: Prompt Template
template = """
You are an expert assistant for summarizing academic/legal documents.

### Document Chunk:
{document_chunk}

Extract:
1. Problem Statement
2. Proposed Method
3. Key Findings

Return JSON:
{
"problem_statement": "",
"proposed_method": "",
"key_findings": ""
}
"""

prompt = PromptTemplate.from_template(template)

# Step 6: Create Chain
chain = prompt | llm | StrOutputParser()

# Step 7: Process First 3 Chunks
print("Summarizing chunks...")
for i, doc in enumerate(docs[:3]):
    summary = chain.invoke({"document_chunk": doc.page_content})
    print(f"\n--- Summary {i+1} ---\n{summary}")
