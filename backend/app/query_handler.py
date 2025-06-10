# user query lo → search FAISS → answers + citations do

from dotenv import load_dotenv
load_dotenv()

from backend.app.vector_store import search_similar_docs
from groq import Groq
import os

# Set Groq API Key
api_key = os.getenv("GROQ_API_KEY") 
client = Groq(api_key=api_key)

def ask_question_from_docs(query):
    docs = search_similar_docs(query, top_k=5)
    combined_context = ""
    for doc_id, text in docs:
        if len(text) > 1500:
            text = text[:1500]
        combined_context += f"Document ID: {doc_id}\n{text}\n\n"

    prompt = f"""
You are a helpful assistant. Based on the below documents, answer the user's query.

Query: {query}

Documents:
{combined_context}

Give a concise answer.
"""

    response = client.chat.completions.create(
        model="llama3-70b-8192",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.3
    )
    return response.choices[0].message.content


def get_doc_level_answers(query):
    docs = search_similar_docs(query, top_k=5)
    results = []

    for doc_id, text in docs:
        if len(text) > 1500:
            text = text[:1500]

        prompt = f"""
You are a legal document analysis assistant. Extract a short and clear answer to the following question based only on this document.

Document ID: {doc_id}
Content:
{text}

Question: {query}

Answer in 1-2 lines. Also mention page and paragraph number if detectable. Format output as:

Answer: ...
Citation: Page X, Para Y
"""

        response = client.chat.completions.create(
            model="llama3-70b-8192",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.3
        )

        content = response.choices[0].message.content
        try:
            answer_part = content.split("Answer:")[1].split("Citation:")[0].strip()
            citation_part = content.split("Citation:")[1].strip()
        except:
            answer_part = content.strip()
            citation_part = "Not detected"

        results.append({
            "Document ID": doc_id,
            "Extracted Answer": answer_part,
            "Citation": citation_part
        })

    return results
