import streamlit as st
with open("assets/styles.css") as f:
    st.markdown(
        f"<style>{f.read()}</style>",
        unsafe_allow_html=True
    )
from utils.qa_chain import ask_question
st.markdown("""
<div class="chat-hero">

<h1>
💬 AI Research Assistant
</h1>

<p>
Ask questions from uploaded PDFs using Gemini, LangChain and Semantic Search.
</p>

</div>
""", unsafe_allow_html=True)
st.caption(
    "Chat with your uploaded documents"
)

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:

    with st.chat_message(
        message["role"]
    ):
        st.markdown(
            message["content"]
        )

prompt = st.chat_input(
    "Ask about your documents..."
)

if prompt:

    # User Message
    st.session_state.messages.append(
        {
            "role": "user",
            "content": prompt
        }
    )

    with st.chat_message("user"):
        st.markdown(prompt)

    # Assistant Response
    with st.chat_message("assistant"):

        with st.spinner(
            "Searching documents..."
        ):

            result = ask_question(
                prompt
            )

            answer = result["answer"]

            st.markdown(answer)

            if result["sources"]:

                st.markdown("---")
                st.markdown("#### 📚 Sources")

                for source in result["sources"]:

                    st.markdown(
                        f"📄 Page {source['page']}"
                    )

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": answer
        }
    )