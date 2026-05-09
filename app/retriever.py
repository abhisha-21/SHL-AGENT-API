import faiss
import pickle
import numpy as np

from sentence_transformers import SentenceTransformer

model = SentenceTransformer('all-MiniLM-L6-v2')

index = faiss.read_index("vectorstore/index.faiss")

with open("vectorstore/metadata.pkl", "rb") as f:
    metadata = pickle.load(f)

def search_catalog(query, top_k=10):
    embedding = model.encode([query])

    distances, indices = index.search(
        np.array(embedding).astype("float32"),
        top_k
    )

    results = []

    for idx in indices[0]:
        if idx < len(metadata):
            results.append(metadata[idx])

    return results