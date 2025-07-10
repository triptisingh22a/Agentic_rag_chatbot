# === core/embeddings.py ===

from sentence_transformers import SentenceTransformer

# ✅ Load the SentenceTransformer model once
# You can replace this with another model like "all-mpnet-base-v2" or any local model
model = SentenceTransformer('all-MiniLM-L6-v2')

def get_embeddings(texts):
    """
    Given a list of strings, return a list of dense vector embeddings.
    """
    if isinstance(texts, str):
        texts = [texts]
    return model.encode(texts)
