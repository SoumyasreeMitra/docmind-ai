import streamlit as st

st.set_page_config(
    page_title="DocMind AI",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Load CSS
with open("assets/styles.css") as f:
    st.markdown(
        f"<style>{f.read()}</style>",
        unsafe_allow_html=True
    )

# ==========================
# SIDEBAR
# ==========================

with st.sidebar:

    st.title("🧠 DocMind AI")

    st.caption(
        "Personal Document Intelligence Platform"
    )

    st.divider()

    st.page_link(
        "pages/Dashboard.py",
        label="Dashboard",
        icon="🏠"
    )

    st.page_link(
        "pages/Chat.py",
        label="AI Chat",
        icon="💬"
    )

    st.page_link(
        "pages/Documents.py",
        label="Documents",
        icon="📄"
    )

    st.page_link(
        "pages/Settings.py",
        label="Settings",
        icon="⚙️"
    )

    st.divider()

    st.info(
        """
        👤 **Soumyasree**

        AI Engineer
        """
    )

# HOME PAGE

st.markdown("# 🧠 DocMind AI")

st.markdown(
    """
    Welcome to your AI-powered document assistant.

    Upload PDFs, build a knowledge base,
    and chat with your documents using Gemini.
    """
)

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