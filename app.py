import streamlit as st
from utils import load_faq, find_best_match
from groq_handler import ask_groq

st.set_page_config(page_title="Campus Chatbot", page_icon="🎓")
st.title("🎓 Campus Query Chatbot")
st.write("Ask me anything related to your university campus!")

faq = load_faq()

user_input = st.text_input("📨 Your Question:")

if st.button("Submit") and user_input.strip():
    matched_q = find_best_match(user_input, faq)

    if matched_q:
        # Found a close FAQ match, pass it as context to Groq
        response = ask_groq(user_input, context=f"{matched_q}: {faq[matched_q]}")
        st.success(f"🤖 {response}")
    else:
        # No close match, fallback to Groq with generic context
        st.warning("Couldn't match with any FAQ. Trying AI for a smart answer...")
        response = ask_groq(user_input)
        st.success(f"🤖 {response}")
