import streamlit as st
st.title("My Chatbot")
st.info("Welcome!")
user_msg = st.text_input("Enter your message:")
if st.button("Send"):
    if user_msg:
        st.success("Message sent successfully!")
        st.write("User message:", user_msg)
    else:
        st.warning("Please enter a message.")