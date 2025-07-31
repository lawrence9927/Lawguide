import streamlit as st
import requests
import os

# ------------------ SETTINGS ------------------
st.set_page_config(page_title="LawGuide", layout="centered")
st.title("⚖️ LawGuide - Your Legal AI Assistant (India)")
st.markdown("💬 Ask your legal questions in **Hinglish** (Hindi + English mix).")

# ------------------ CUSTOM CSS ------------------
st.markdown("""
    <style>
    .stChatMessage { background-color: #1e1e1e; padding: 10px; border-radius: 10px; margin-bottom: 10px; }
    .stTextInput > div > input { border: 1px solid red; }
    </style>
""", unsafe_allow_html=True)

# ------------------ API CONFIG ------------------
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")  # Load key securely
MODEL = "mistralai/mistral-small-3.2-24b-instruct:free"
API_URL = "https://openrouter.ai/api/v1/chat/completions"

if not OPENROUTER_API_KEY:
    st.error("❌ API key not found. Please set the 'OPENROUTER_API_KEY' environment variable.")
    st.stop()

# ------------------ CHAT SESSION INIT ------------------
if "messages" not in st.session_state:
    st.session_state.messages = []

# ------------------ DISPLAY CHAT HISTORY ------------------
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# ------------------ USER INPUT ------------------
user_input = st.chat_input("Ask your legal question here...")

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    with st.chat_message("assistant"):
        with st.spinner("Thinking like a lawyer..."):
            headers = {
                "Authorization": f"Bearer {OPENROUTER_API_KEY}",
                "Content-Type": "application/json"
            }
            payload = {
                "model": MODEL,
                "messages": st.session_state.messages,
                "temperature": 0.7
            }

            try:
                response = requests.post(API_URL, headers=headers, json=payload)
                if response.status_code == 200:
                    reply = response.json()["choices"][0]["message"]["content"]
                else:
                    error_detail = response.json().get("error", {}).get("message", "Unknown error")
                    reply = f"❌ Error {response.status_code}: {error_detail}"
            except Exception as e:
                reply = f"❌ Failed to connect: {e}"

            st.markdown(reply)
            st.session_state.messages.append({"role": "assistant", "content": reply})
