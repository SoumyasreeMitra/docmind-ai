from langchain_google_genai import ChatGoogleGenerativeAI
from utils.vector_store import load_vector_store


def ask_question(question):

    db = load_vector_store()

    docs = db.similarity_search(
        question,
        k=4
    )

    if not docs:
        return {
            "answer": "No relevant information found in the uploaded documents.",
            "sources": []
        }

    context = "\n\n".join(
        doc.page_content
        for doc in docs
    )

    sources = []

    for doc in docs:

        page = doc.metadata.get("page", "Unknown")

        source = {
            "page": page
        }

        if source not in sources:
            sources.append(source)

    llm = ChatGoogleGenerativeAI(
        model="gemini-2.5-flash",
        temperature=0
    )

    prompt = f"""
You are a PDF Question Answering Assistant.

Rules:
1. Answer ONLY using the provided context.
2. If the answer is not present in the context, say:
   "I could not find this information in the uploaded documents."
3. Keep answers clear and concise.
4. Do not make up information.

Context:
{context}

Question:
{question}

Answer:
"""

    response = llm.invoke(prompt)

    return {
        "answer": response.content,
        "sources": sources
    }