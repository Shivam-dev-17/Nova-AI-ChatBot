import streamlit as st

from chatbot import ChatBot

bot = ChatBot()

st.set_page_config(
    page_title="Nova AI Assistant",
    page_icon="🤖"
)

st.title("🤖 Nova AI Assistant")
st.write(
    "A rule-based AI chatbot built using Python <Created by Shivam>"
)

if "messages" not in st.session_state:

    st.session_state.messages = []

for message in st.session_state.messages:

    with st.chat_message(message["role"]):
        st.write(message["content"])

user_input = st.chat_input(
    "Type your message..."
)

if user_input:

    st.session_state.messages.append(
        {
            "role":"user",
            "content":user_input
        }
    )

    response = bot.get_response(
        user_input
    )

    st.session_state.messages.append(
        {
            "role":"assistant",
            "content":response
        }
    )

    st.rerun()
