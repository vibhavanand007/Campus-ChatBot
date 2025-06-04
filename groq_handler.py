import streamlit as st
from groq import Groq

client = Groq(api_key="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")

def ask_groq(question, context="You are a helpful campus assistant."):
    try:
        response = client.chat.completions.create(
            model="llama3-8b-8192",
            messages=[
                {"role": "system", "content": context},
                {"role": "user", "content": question}
            ],
            temperature=0.3
        )
        return response.choices[0].message.content.strip()

    except Exception as e:
        return f"⚠️ Error: {e}"