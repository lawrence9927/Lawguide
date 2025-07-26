import streamlit as st
import requests

# ------------------ SETTINGS ------------------
st.set_page_config(page_title="LawGuide", layout="centered")
st.title("⚖️ LawGuide - Your Legal AI Assistant (India)")
st.markdown("💬 Ask your legal questions in **Hinglish** (Hindi + English mix).")

# Add CSS for better UI
st.markdown("""
    <style>
    .stChatMessage { background-color: #1e1e1e; padding: 10px; border-radius: 10px; margin-bottom: 10px; }
    .stTextInput > div > input { border: 1px solid red; }
    </style>
""", unsafe_allow_html=True)

# ------------------ OPENROUTER API CONFIG ------------------
OPENROUTER_API_KEY = "API_KEY"
MODEL = "mistralai/mistral-small-3.2-24b-instruct:free"
API_URL = "https://openrouter.ai/api/v1/chat/completions"

# ------------------ CHAT SESSION INIT ------------------
if "messages" not in st.session_state:
    st.session_state.messages = []

# ------------------ DISPLAY PREVIOUS MESSAGES ------------------
for msg in st.session_state.messages:
    role, content = msg["role"], msg["content"]
    with st.chat_message(role):
        st.markdown(content)

# ------------------ USER INPUT ------------------
user_input = st.chat_input("Ask your legal question here...")

if user_input:
    # Display user message
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    # Display loading spinner
    with st.chat_message("assistant"):
        with st.spinner("Thinking like a lawyer..."):
            # ------------------ API CALL ------------------
            headers = {
                "Authorization": f"Bearer {OPENROUTER_API_KEY}",
                "Content-Type": "application/json"
            }
            payload = {
                "model": MODEL,
                "messages": st.session_state.messages,
                "temperature": 0.7
            }

            response = requests.post(API_URL, headers=headers, json=payload)

            # ------------------ RESPONSE HANDLING ------------------
            if response.status_code == 200:
                reply = response.json()["choices"][0]["message"]["content"]
            else:
                reply = f"❌ Error {response.status_code}: {response.json().get('error', {}).get('message', 'Unknown error')}"

            st.markdown(reply)
            st.session_state.messages.append({"role": "assistant", "content": reply})
