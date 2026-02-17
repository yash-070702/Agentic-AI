# Exercise 2: Load Multiple PDF Files

# A company stores research reports in PDF format. You need to ingest them into LangChain.

# Steps:

# Save at least two sample PDFs (e.g., report1.pdf, report2.pdf).

# Use PyPDFLoader in LangChain to load all PDFs from a folder.

# Print the number of pages and preview the first page of each PDF.

# Combine all loaded pages into a single document list.

# Goal: Practice PDF ingestion and multi-file handling.

# AGI1.pdf

# AGI2.pdf
from langchain_community.document_loaders import PyPDFLoader
allDocuments=[]

loader1=PyPDFLoader("AGI1.pdf")
documents1=loader1.load()

print("loaded AG1.PDF")
print("NUmber of pages",len(documents1))
print("first page review of AGI1")
print(documents1[0].page_content[:300])

allDocuments.extend(documents1)

loader2=PyPDFLoader("AGI2.pdf")
documents2=loader2.load()

print("loaded AG2.PDF")
print("NUmber of pages",len(documents2))
print("first page review of AGI2")
print(documents2[0].page_content[:300])

allDocuments.extend(documents2)

print("total pages from all pdf ", len(allDocuments))

