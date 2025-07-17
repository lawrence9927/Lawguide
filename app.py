import openai
import os
# Set your API key securely (recommended for Streamlit)
openai.api_key = st.secrets["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"]

def ai_legal_guide(question):
    prompt = f"You are an expert Indian legal assistant. Given the following query, provide specific statutes, relevant case law, and clear advice.\n\nQuery: {question}\n\nAnswer:"
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # or "gpt-4" if available
            messages=[{"role": "user", "content": prompt}],
            max_tokens=500,
            temperature=0.2,
        )
        return response["choices"][0]["message"]["content"].strip()
    except Exception as e:
        return f"AI error: {e}"
