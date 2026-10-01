
import streamlit as st
import ollama

st.set_page_config(
    page_title="AI Chatbot",
    page_icon="🤖"
)

st.title("My AI Chatbot")
st.caption("Powered by Ollama + Streamlit")

# 1. Initialization
if "messages" not in st.session_state:
    st.session_state.messages = []

# 2. Display previous messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# 3. User interaction
prompt = st.chat_input("Type your message...")

if prompt:

    # Store user message
    st.session_state.messages.append({
        "role": "user",
        "content": prompt
    })

    with st.chat_message("user"):
        st.write(prompt)

    # 4. Generate response
    response = ollama.chat(
        model="llama3.2",
        messages=st.session_state.messages
    )

    answer = response["message"]["content"]

    # Store assistant response
    st.session_state.messages.append({
        "role": "assistant",
        "content": answer
    })

    # 5. Display response
    with st.chat_message("assistant"):
        st.write(answer)