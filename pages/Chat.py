import streamlit as st

st.markdown("""
<h1 style="
font-size:60px;
margin-bottom:0px;
">
💬 AI Assistant
</h1>
""",unsafe_allow_html=True)

st.caption(
"Chat with your documents"
)

if "messages" not in st.session_state:
    st.session_state.messages=[]

for message in st.session_state.messages:

    with st.chat_message(message["role"]):
        st.markdown(message["content"])

prompt=st.chat_input(
    "Ask about your documents..."
)

if prompt:

    st.session_state.messages.append(
        {
            "role":"user",
            "content":prompt
        }
    )

    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        st.markdown(
            "Backend integration coming next..."
        )