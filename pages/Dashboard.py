import streamlit as st

with open("assets/styles.css") as f:
    st.markdown(
        f"<style>{f.read()}</style>",
        unsafe_allow_html=True
    )
st.markdown("""
<div class="dashboard-hero">

<div class="hero-badge">
🚀 Gemini + LangChain + FAISS
</div>

<h1 class="dashboard-title">
🧠 DocMind AI
</h1>

<p class="dashboard-subtitle">
Your AI-Powered Research Assistant
</p>

<p class="dashboard-desc">
Upload PDFs, build vector embeddings, perform semantic search and chat with documents using Gemini AI.
</p>

<div class="hero-glow"></div>

</div>
""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

st.text_input(
    "",
    placeholder="🔍 Search documents, topics, concepts..."
)

st.markdown("<br>", unsafe_allow_html=True)

col1,col2,col3,col4 = st.columns(4)

cards = [
    ("📄","Upload PDFs","Build your knowledge base"),
    ("💬","AI Chat","Ask questions instantly"),
    ("📚","Library","Manage documents"),
    ("⚡","Insights","Generate AI summaries")
]

for col,data in zip([col1,col2,col3,col4],cards):

    icon,title,desc = data

    with col:

        st.markdown(f"""
        <div class="action-card">

        <div class="card-icon">{icon}</div>

        <h3>{title}</h3>

        <p>{desc}</p>

        </div>
        """, unsafe_allow_html=True)

st.markdown("<br><br>", unsafe_allow_html=True)

st.markdown("## 📊 Analytics Overview")

c1, c2, c3, c4 = st.columns(4)

stats = [
    ("Documents", "12"),
    ("Questions", "156"),
    ("Chats", "27"),
    ("Pages Indexed", "340")
]

for col, (title, value) in zip([c1, c2, c3, c4], stats):

    with col:

        st.markdown(
            f"""
<div class="stat-card">
    <div class="stat-value">{value}</div>
    <div class="stat-title">{title}</div>
</div>
""",
            unsafe_allow_html=True
        )

st.markdown("<br><br>", unsafe_allow_html=True)

st.markdown("<br><br>", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

st.markdown("""
<h2 class="section-title">
📚 Recent Documents
</h2>
""", unsafe_allow_html=True)

docs = [
    "Activation Functions.pdf",
    "Operating Systems.pdf",
    "DBMS Notes.pdf"
]

for doc in docs:

    st.markdown(
        f"""
<div class="doc-card">
    <h4>📘 {doc}</h4>
    <p>Indexed • Ready for AI Chat</p>
</div>
        """,
        unsafe_allow_html=True
    )