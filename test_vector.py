from utils.pdf_loader import load_pdf
from utils.vector_store import (
    split_documents,
    create_vector_store
)

docs = load_pdf("data/Activation Functions.pdf")

chunks = split_documents(docs)

db = create_vector_store(chunks)

print("Vector database created successfully!")
print("Total chunks:", len(chunks))