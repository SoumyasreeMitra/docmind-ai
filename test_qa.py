from utils.vector_store import load_vector_store
from utils.chatbot import get_llm

db = load_vector_store()

question = input("Ask a question: ")

docs = db.similarity_search(question, k=3)

context = "\n\n".join(
    doc.page_content for doc in docs
)

prompt = f"""
Answer ONLY from the provided context.

Context:
{context}

Question:
{question}

Answer:
"""

llm = get_llm()

response = llm.invoke(prompt)

print("\nAnswer:\n")
print(response.content)