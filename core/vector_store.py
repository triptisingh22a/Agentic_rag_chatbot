# === core/vector_store.py ===
import faiss
import numpy as np
from core.embeddings import get_embeddings

def store_chunks(chunks):
    if not chunks:
        raise ValueError("❌ No text chunks found to embed.")
    
    vectors = get_embeddings(chunks)
    if len(vectors) == 0:
        raise ValueError("❌ Embedding failed: no valid vectors created.")
    
    vectors = np.array(vectors).astype('float32')
    index = faiss.IndexFlatL2(vectors.shape[1])
    index.add(vectors)

    # Return both index and associated chunks
    return {
        "index": index,
        "chunks": chunks,
        "vectors": vectors
    }

def retrieve_top_k(vector_store, query, k=5):
    q_vector = get_embeddings([query])
    q_vector = np.array(q_vector).astype('float32')

    index = vector_store["index"]
    chunks = vector_store["chunks"]

    D, I = index.search(q_vector, k)

    top_chunks = []
    for idx in I[0]:
        if idx < len(chunks):
            top_chunks.append(chunks[idx])
    
    return top_chunks
