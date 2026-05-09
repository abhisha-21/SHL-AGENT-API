import json
import faiss
import numpy as np
import pickle

from sentence_transformers import SentenceTransformer

print("Loading model...")

model = SentenceTransformer("all-MiniLM-L6-v2")

print("Loading catalog...")

with open("app/catalog.json", "r", encoding="utf-8") as f:
    catalog = json.load(f)

documents = []

for item in catalog:

    text = f"""
    Name: {item['name']}
    Description: {item['description']}
    Type: {item['test_type']}
    """

    documents.append(text)

print("Creating embeddings...")

embeddings = model.encode(documents)

embeddings = np.array(embeddings).astype("float32")

dimension = embeddings.shape[1]

print("Building FAISS index...")

index = faiss.IndexFlatL2(dimension)

index.add(embeddings)

faiss.write_index(index, "vectorstore/index.faiss")

with open("vectorstore/metadata.pkl", "wb") as f:
    pickle.dump(catalog, f)

print("FAISS index built successfully")