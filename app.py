import openai
import os
# Set your API key securely (recommended for
openai.api_key = st.secrets["OPENAI_API_KEY"]

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
