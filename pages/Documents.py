import streamlit as st
with open("assets/styles.css") as f:
    st.markdown(
        f"<style>{f.read()}</style>",
        unsafe_allow_html=True
    )
import os

from utils.rag_pipeline import build_database

UPLOAD_DIR = "uploads"

st.markdown("""
<div class="docs-hero">

<h1>
📄 Document Library
</h1>

<p>
Upload PDFs and build your AI knowledge base.
</p>

</div>
""", unsafe_allow_html=True)

uploaded_files = st.file_uploader(
    "Upload PDF Files",
    type=["pdf"],
    accept_multiple_files=True
)

if uploaded_files:

    for file in uploaded_files:

        save_path = os.path.join(
            UPLOAD_DIR,
            file.name
        )

        with open(save_path, "wb") as f:
            f.write(file.getbuffer())

        with st.spinner(
            f"Indexing {file.name}..."
        ):
            build_database(save_path)

    st.success(
        "Documents indexed successfully!"
    )

st.markdown("---")

st.subheader("Document Library")

if os.path.exists(UPLOAD_DIR):

    files = os.listdir(UPLOAD_DIR)

    if files:

        for file in files:

            st.markdown(f"""
<div class="doc-card">

<h4>📘 {file}</h4>

<p>
Indexed and ready for chat
</p>

</div>
""", unsafe_allow_html=True)

    else:
        st.warning(
            "No documents uploaded."
        )