#  Streamlit Frontend

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import streamlit as st
import pandas as pd

from backend.app.document_loader import process_document
from backend.app.vector_store import add_documents_to_index
from backend.app.query_handler import get_doc_level_answers
from backend.app.summarizer import summarize_themes_from_docs

st.set_page_config(page_title="Wasserstoff Doc Chatbot", layout="wide")
st.title("📄 Wasserstoff Gen-AI Chatbot")
st.caption("Upload documents and ask questions to get answers with citations and theme-based insights.")

# Upload Section
uploaded_files = st.file_uploader("📤 Upload PDFs or Images", type=["pdf", "png", "jpg", "jpeg"], accept_multiple_files=True)

if uploaded_files:
    texts, doc_ids = [], []
    for file in uploaded_files:
        file_path = os.path.join("data", file.name)
        with open(file_path, "wb") as f:
            f.write(file.read())
        st.success(f"✅ Uploaded: {file.name}")
        
        extracted_text = process_document(file_path)
        if extracted_text.strip():
            texts.append(extracted_text)
            doc_ids.append(file.name)
    
    if texts:
        add_documents_to_index(texts, doc_ids)
        st.success("📚 Documents added to knowledge base!")

# Query Section
query = st.text_input("🔍 Ask a question about the documents:")

if st.button("Get Answer") and query:
    with st.spinner("Thinking..."):
        # Get tabular doc-level results
        doc_results = get_doc_level_answers(query)
        st.markdown("### 📊 Document-wise Answer")
        st.dataframe(pd.DataFrame(doc_results))

        # Synthesized Theme Summary
        st.markdown("### 💬 Synthesized Theme Summary")
        themes = summarize_themes_from_docs(query)
        st.write(themes)
