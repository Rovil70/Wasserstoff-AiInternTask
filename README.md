# Wasserstoff Gen-AI Internship Task

An AI-powered document chatbot that supports 75+ PDF/Image/Text files, extracts context-aware answers, and generates theme-based summaries.

## 📌 Features
- Upload scanned PDFs/images or text documents
- OCR-based text extraction
- Query answering with doc-level citation (DocID, Page, Para)
- Theme-based summarization from multiple docs
- Clean Streamlit UI
- FAISS-based vector search

## 🚀 Tech Stack
- Python, Streamlit
- OpenAI (GPT-3.5-turbo)
- SentenceTransformers
- FAISS for vector search
- Tesseract OCR
- Langchain (optional)

## 📁 Project Structure
📦 AiInternTask
┣ 📂 backend
┃ ┣ 📂 app
┃ ┃ ┣ 📜 document_loader.py
┃ ┃ ┣ 📜 vector_store.py
┃ ┃ ┣ 📜 query_handler.py
┃ ┃ ┣ 📜 summarizer.py
┣ 📂 frontend
┃ ┗ 📜 app.py
┣ 📂 data
┗ 📜 requirements.txt




## ✅ How to Run

```bash
pip install -r requirements.txt
streamlit run frontend/app.py
