from utils.pdf_loader import load_pdf
from utils.vector_store import (
    split_documents,
    create_vector_store
)

def build_database(pdf_path):

    docs = load_pdf(pdf_path)

    chunks = split_documents(docs)

    create_vector_store(chunks)

    return True