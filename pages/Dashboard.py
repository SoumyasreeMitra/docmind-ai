import streamlit as st

st.title("Dashboard")

st.caption(
    "Manage your AI knowledge base"
)

st.text_input(
    "",
    placeholder="🔍 Search documents..."
)

st.markdown("<br>", unsafe_allow_html=True)

c1,c2,c3,c4 = st.columns(4)

cards = [
    ("📄","Upload PDF","Add documents"),
    ("💬","New Chat","Ask questions"),
    ("📚","Library","Manage files"),
    ("⚡","Insights","Analyze PDFs")
]

for col,data in zip([c1,c2,c3,c4],cards):

    icon,title,desc = data

    with col:

        st.markdown(f"""
        <div class="action-card">

        <h1>{icon}</h1>

        <h3>{title}</h3>

        <p>{desc}</p>

        </div>
        """, unsafe_allow_html=True)

st.markdown("<br><br>", unsafe_allow_html=True)

st.subheader("Analytics")

c1,c2,c3,c4 = st.columns(4)

stats = [
    ("Documents","12"),
    ("Questions","156"),
    ("Chats","27"),
    ("Pages","340")
]

for col,data in zip([c1,c2,c3,c4],stats):

    title,value = data

    with col:

        st.markdown(f"""
        <div class="stat-card">

        <h4>{title}</h4>

        <div class="stat-value">
        {value}
        </div>

        </div>
        """, unsafe_allow_html=True)

st.markdown("<br><br>", unsafe_allow_html=True)

st.subheader("Recent Documents")

docs = [
    "Operating Systems Notes.pdf",
    "DBMS Complete Guide.pdf",
    "Software Engineering.pdf"
]

for doc in docs:

    st.markdown(f"""
    <div class="doc-card">

    <h4>📘 {doc}</h4>

    <p>Recently uploaded</p>

    </div>
    """, unsafe_allow_html=True)