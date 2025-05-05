import faiss
import json
import numpy as np
from sentence_transformers import SentenceTransformer

def load_documents():
    with open("data/career_articles.json", "r") as f:
        documents = json.load(f)
    return documents

def load_faiss_index():
    return faiss.read_index("embeddings/career_index.faiss")

def embed_query(query, model):
    return model.encode([query])

def hybrid_retrieve(query, k=5):
    model = SentenceTransformer('all-MiniLM-L6-v2')
    index = load_faiss_index()
    documents = load_documents()

    query_vec = embed_query(query, model)
    _, indices = index.search(np.array(query_vec), k)

    retrieved_docs = [documents[i] for i in indices[0]]

    keywords = query.lower().split()
    boosted_docs = []
    for doc in retrieved_docs:
        match_score = sum(word in doc["content"].lower() for word in keywords)
        boosted_docs.append((match_score, doc))

    boosted_docs.sort(key=lambda x: x[0], reverse=True)
    top_docs = [doc for _, doc in boosted_docs[:k]]

    return top_docs
