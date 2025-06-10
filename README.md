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
- **Python** & **Streamlit** – frontend and backend logic
- **Groq API** – using **LLaMA3-70B-8192** model for summarization and question answering
- **SentenceTransformers** – for generating text embeddings (`all-MiniLM-L6-v2`)
- **FAISS** – for semantic vector search
- **Tesseract OCR** – for scanned document text extraction
- **pdf2image** & **PyPDF2** – for handling PDF files (scanned + digital)
- **LangChain (optional)** – for abstraction (not critical in this project)
- **Render** – for deployment of full app

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
