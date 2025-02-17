import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000"  # Correct API URL

st.title("📄 AI Research Paper Summarizer")

# Summarization Section
st.header("Summarize a Research Paper")
text = st.text_area("Enter paper abstract or text")
if st.button("Summarize"):
    try:
        response = requests.post(f"{API_URL}/summarize/", json={"text": text})
        if response.status_code == 200:
            st.write("### Summary:")
            st.write(response.json().get("summary", "No summary returned."))
        else:
            st.error(f"API Error: {response.status_code} - {response.text}")
    except requests.exceptions.RequestException as e:
        st.error(f"Request failed: {e}")

# Paper Search Section
st.header("Search for Similar Papers")
query = st.text_input("Enter search query")
if st.button("Search"):
    response = requests.post(f"{API_URL}/search/", json={"text": query})
    st.write("### Best Match:")
    st.write(response.json()["best_match"])

# Citation Recommendation Section
st.header("Citation Recommendation")
citation_text = st.text_area("Enter paper content for citation analysis")
if st.button("Check Citation Score"):
    response = requests.post(f"{API_URL}/recommend/", json={"text": citation_text})
    st.write("### Citation Score:")
    st.write(response.json()["citation_score"])

st.write("🚀 AI-Powered Paper Summarization & Search System by 셜조드")
