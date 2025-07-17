import streamlit as st

# Example statutes and cases for demonstration
EXAMPLE_STATUTES = {
    "Section 302, IPC": "Punishment for murder: Whoever commits murder shall be punished with death or imprisonment for life.",
    "Article 21, Constitution": "Protection of life and personal liberty: No person shall be deprived of his life or personal liberty except according to procedure established by law.",
}

EXAMPLE_CASES = [
    {
        "title": "K.M. Nanavati v. State of Maharashtra (1962)",
        "court": "Supreme Court of India",
        "summary": "Landmark case on the distinction between murder and culpable homicide."
    },
    {
        "title": "Maneka Gandhi v. Union of India (1978)",
        "court": "Supreme Court of India",
        "summary": "Expanded interpretation of Article 21 — Right to life and personal liberty."
    }
]

def search_statutes(query):
    results = []
    for name, text in EXAMPLE_STATUTES.items():
        if query.lower() in name.lower() or query.lower() in text.lower():
            results.append(f"**{name}:** {text}")
    if not results:
        results.append("No direct statute found, but AI will attempt to generate a relevant answer.")
    return results

def similar_cases(query):
    results = []
    for case in EXAMPLE_CASES:
        if query.lower() in case["title"].lower() or query.lower() in case["summary"].lower():
            results.append(f"- **{case['title']}** ({case['court']}): {case['summary']}")
    if not results:
        results.append("No exact matching cases found, but see below for general guidance.")
    return results

def ai_legal_guide(query):
    # Placeholder for real AI backend; this demo responds to a few keywords
    if "murder" in query.lower():
        return (
            "Possible legal arguments:\n"
            "- Was the act premeditated or sudden provocation?\n"
            "- Refer to Section 302 (Punishment for murder) of IPC.\n"
            "- Review precedent: K.M. Nanavati v. State of Maharashtra (1962).\n"
            "Legal direction: Establish intent, circumstances, and evidence."
        )
    elif "right to life" in query.lower() or "personal liberty" in query.lower():
        return (
            "Possible legal arguments:\n"
            "- Refer to Article 21 of the Indian Constitution.\n"
            "- Use landmark case: Maneka Gandhi v. Union of India (1978) for broader interpretation.\n"
            "Legal direction: Argue on procedures established by law affecting liberty."
        )
    else:
        return "AI unable to find detailed guidance specifically, but recommends reviewing constitutional articles and relevant codes."

# Streamlit App
st.set_page_config(page_title="AI Lawyer Assistant", layout="centered")

st.title("AI Lawyer Assistant for Indian Law")

st.write("""
Enter your legal question, case summary, or upload a document for AI-driven brainstorming, precedent search, and statute guidance.
""")

case_details = st.text_area("Describe your case/question (e.g., 'Tenant was evicted without notice', or 'Murder case with sudden provocation'):")

if st.button("Get AI Legal Guidance"):
    if not case_details.strip():
        st.info("Please enter some details about your legal question or case.")
    else:
        st.subheader("AI-Suggested Arguments & Strategy")
        st.write(ai_legal_guide(case_details))

        st.subheader("Statutes/Sections Referenced")
        for line in search_statutes(case_details):
            st.write(line)

        st.subheader("Similar Past Cases")
        for case in similar_cases(case_details):
            st.write(case)

st.write("---")
st.info("Demo version. For advanced answers, connect to a real AI backend or email your queries to the developer.")
