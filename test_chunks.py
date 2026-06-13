from utils.pdf_loader import load_pdf
from utils.vector_store import split_documents

docs = load_pdf("data/Activation Functions.pdf")

chunks = split_documents(docs)

print("Total chunks:", len(chunks))

print("\nFirst chunk:\n")
print(chunks[0].page_content)