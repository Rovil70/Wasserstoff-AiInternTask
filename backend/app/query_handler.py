# user query lo → search FAISS → answers + citations do

from dotenv import load_dotenv
load_dotenv()

from .vector_store import search_similar_docs
from groq import Groq
import os

# Use Groq client (no billing needed)
client = Groq(api_key=os.getenv("GROQ_API_KEY"))


def format_context_for_prompt(results, max_characters=8000):
    formatted = ""
    total_chars = 0

    for i, (doc_id, text) in enumerate(results):
        if total_chars + len(text) > max_characters:
            break
        snippet = f"[{i+1}] Document: {doc_id}\n{text}\n\n"
        formatted += snippet
        total_chars += len(snippet)

    return formatted

def ask_question_from_docs(user_query):
    # Step 1: Search similar docs
    top_docs = search_similar_docs(user_query, top_k=5)
    context = format_context_for_prompt(top_docs)

    # Step 2: Groq prompt to LLaMA 3
    prompt = f"""
You are an AI assistant helping users find accurate information from uploaded documents.

Context:
{context}

Question: {user_query}

Answer concisely using the above context only. Also mention which documents the answers were found in.
"""

    response = client.chat.completions.create(
        model="llama3-70b-8192",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.4,
    )

    return response.choices[0].message.content
