from utils.vector_store import load_vector_store

db = load_vector_store()

query = "What is the main topic of this document?"

docs = db.similarity_search(query, k=3)

print("\nRetrieved Chunks:\n")

for i, doc in enumerate(docs, start=1):
    print(f"\n----- Chunk {i} -----\n")
    print(doc.page_content[:500])