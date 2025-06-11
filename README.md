# Wasserstoff Gen-AI Internship Task

An AI-powered document chatbot that supports 75+ PDF/Image/Text files, extracts context-aware answers, and generates theme-based summaries.

## Demo Link (Hugging Face)
🔗 https://huggingface.co/spaces/Rovil70/wasserstoff-genai-chatbot

## Features
- Upload and process 75+ documents (PDF/Image/Text)
- Natural language question answering with document citations
- Summarized themes across multiple docs
- OCR support via Tesseract
- Streamlit-based frontend, FAISS-backed vector store
- Deployed on Hugging Face + public GitHub repo

## 🚀 Tech Stack
- **Python** & **Streamlit** – frontend and backend logic
- **Groq API** – using **LLaMA3-70B-8192** model for summarization and question answering
- **SentenceTransformers** – for generating text embeddings (`all-MiniLM-L6-v2`)
- **FAISS** – for semantic vector search
- **Tesseract OCR** – for scanned document text extraction
- **pdf2image** & **PyPDF2** – for handling PDF files (scanned + digital)
- **LangChain (optional)** – for abstraction (not critical in this project)
- **Hugging Face** - Deployed on Hugging Face

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
