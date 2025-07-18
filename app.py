import streamlit as st
import openai

openai.api_key = st.secrets["OPENAI_API_KEY"]

st.set_page_config(page_title="AI Lawyer Assistant", layout="centered")
st.title("AI Lawyer Assistant for Indian Law")

st.write("""
Welcome! Enter your legal question or case below to get AI-powered legal brainstorming, precedent search, and statute guidance.
""")

def ai_legal_guide(query):
    prompt = (
        "You are an expert Indian legal assistant. "
        "Given the following legal query, offer specific statutes, relevant case law, and clear guidance. "
        "Always base your answer on Indian law with short references.\n\n"
        f"Query: {query}\n\nAI Legal Answer:"
    )
    try:
        response = openai.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": prompt}
            ],
            max_tokens=512,
            temperature=0.2,
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"Error: {e}"

case_details = st.text_area(
    "Describe your legal case or question (e.g., 'Tenant was evicted without notice', or 'Murder case with sudden provocation'):"
)

if st.button("Get AI Legal Guidance"):
    if not case_details.strip():
        st.info("Please enter some details about your legal question or case.")
    else:
        with st.spinner("Consulting Legal AI assistant..."):
            answer = ai_legal_guide(case_details)
            st.subheader("AI-Suggested Guidance & Precedents")
            st.write(answer)

st.write("---")
st.info("Demo version powered by OpenAI. Always verify critical legal advice with a human lawyer before acting.")
