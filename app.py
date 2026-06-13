import streamlit as st

st.set_page_config(
    page_title="DocMind AI",
    page_icon="🧠",
    layout="wide"
)

with open("assets/styles.css") as f:
    st.markdown(
        f"<style>{f.read()}</style>",
        unsafe_allow_html=True
    )

with st.sidebar:

    st.markdown("""
    <div class="sidebar-title">
    🧠 DocMind AI
    </div>

    <div class="sidebar-sub">
    Document Intelligence Platform
    </div>
    """, unsafe_allow_html=True)

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

    st.markdown("""
    <div class="profile-card">
    👤 Soumyasree<br>
    AI Engineer
    </div>
    """, unsafe_allow_html=True)

st.switch_page("pages/Dashboard.py")