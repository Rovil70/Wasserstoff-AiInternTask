# Vector DB + Embeddings

from sentence_transformers import SentenceTransformer
import faiss
import numpy as np
import os
import pickle

# Load the sentence transformer model
embedder = SentenceTransformer('all-MiniLM-L6-v2')

# Path to save/load FAISS index
INDEX_FILE = "backend/app/faiss_index"

def create_or_load_index():
    if os.path.exists(INDEX_FILE + ".pkl"):
        with open(INDEX_FILE + ".pkl", "rb") as f:
            docs, index = pickle.load(f)
    else:
        docs, index = [], faiss.IndexFlatL2(384)  # 384 for MiniLM-L6
    return docs, index

def save_index(docs, index):
    with open(INDEX_FILE + ".pkl", "wb") as f:
        pickle.dump((docs, index), f)

def add_documents_to_index(texts, doc_ids):
    docs, index = create_or_load_index()
    for i, text in enumerate(texts):
        embedding = embedder.encode([text])[0]
        docs.append((doc_ids[i], text))
        index.add(np.array([embedding]))
    save_index(docs, index)

def search_similar_docs(query, top_k=5):
    docs, index = create_or_load_index()
    query_vec = embedder.encode([query])[0]
    D, I = index.search(np.array([query_vec]), top_k)
    results = []
    for idx in I[0]:
        if idx < len(docs):
            results.append(docs[idx])
    return results
