# Theme Identification & Summarization

from dotenv import load_dotenv
load_dotenv()

from backend.app.vector_store import search_similar_docs
import os
from groq import Groq

# Set Groq API Key
groq_api_key = os.getenv("GROQ_API_KEY")

client = Groq(api_key=groq_api_key)

def summarize_themes_from_docs(query):
    # 🔽 LIMIT number of documents for summarization
    docs = search_similar_docs(query, top_k=2)

    context = ""
    for i, (doc_id, text) in enumerate(docs):
        # ✂️ Truncate each doc's text to avoid token overflow
        if len(text) > 1500:
            text = text[:1500]
        context += f"[{i+1}] Document: {doc_id}\n{text}\n\n"

    # ✅ Prompt for LLaMA / Groq to extract themes
    prompt = f"""
You are an expert AI assistant helping to summarize themes across documents.

User Query:
{query}

Below are relevant document excerpts from research papers:

{context}

Please:
- Identify 1 to 3 key themes based on the query
- For each theme, give a short summary and mention supporting documents

Output format:
Theme 1 – [Title]
Summary...
Supported by: DOC001, DOC003

Theme 2 – ...
"""

    response = client.chat.completions.create(
        model="llama3-70b-8192",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.3
    )

    return response.choices[0].message.content
