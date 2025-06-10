#  Streamlit Frontend


import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))



import streamlit as st
from backend.app.document_loader import process_document
from backend.app.vector_store import add_documents_to_index
from backend.app.query_handler import ask_question_from_docs

st.set_page_config(page_title="Wasserstoff Doc Chatbot", layout="wide")
st.title("📄 Wasserstoff Gen-AI Chatbot")
st.caption("Upload documents and ask questions to get answers with citations.")

# Upload Section
uploaded_files = st.file_uploader("Upload PDFs or Images", type=["pdf", "png", "jpg", "jpeg"], accept_multiple_files=True)

if uploaded_files:
    texts, doc_ids = [], []
    for file in uploaded_files:
        file_path = os.path.join("data", file.name)
        with open(file_path, "wb") as f:
            f.write(file.read())
        st.success(f"✅ Uploaded: {file.name}")
        
        # Extract text
        extracted_text = process_document(file_path)
        if extracted_text.strip():
            texts.append(extracted_text)
            doc_ids.append(file.name)
    
    if texts:
        add_documents_to_index(texts, doc_ids)
        st.success("📚 Documents added to knowledge base!")

# Query Section
query = st.text_input("🔍 Ask a question about the documents:", key="user_query")

if st.button("Get Answer"):
    with st.spinner("Thinking..."):
        answer = ask_question_from_docs(st.session_state.user_query)
        st.session_state.answer = answer  # Save in session
if "answer" in st.session_state:
    st.markdown("### 📬 Answer")
    st.write(st.session_state.answer)



# 🎯 Add Theme Summarization Block Right After This
    from backend.app.summarizer import summarize_themes_from_docs

    with st.expander("🧠 Show Synthesized Theme Summary"):
        if st.button("Summarize Themes"):
            with st.spinner("Analyzing themes..."):
                themes = summarize_themes_from_docs(query)
                st.markdown("### 🎯 Themes")
                st.write(themes)
