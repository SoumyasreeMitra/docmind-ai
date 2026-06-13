import streamlit as st

st.title("📄 Documents")

st.caption(
    "Upload and manage PDFs"
)

uploaded_files = st.file_uploader(
    "Upload PDF Files",
    type=["pdf"],
    accept_multiple_files=True
)

if uploaded_files:

    st.success(
        f"{len(uploaded_files)} file(s) uploaded"
    )

st.markdown("---")

st.subheader("Document Library")

docs = [
    "Operating Systems.pdf",
    "DBMS Notes.pdf",
    "Software Engineering.pdf"
]

for doc in docs:

    col1,col2 = st.columns([8,1])

    with col1:
        st.info(f"📘 {doc}")

    with col2:
        st.button(
            "🗑️",
            key=doc
        )