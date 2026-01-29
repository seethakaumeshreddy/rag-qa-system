import faiss, numpy as np

index = faiss.IndexFlatL2(384)
documents = []

def save_embeddings(chunks, embeddings):
    index.add(np.array(embeddings))
    documents.extend(chunks)

def search(query_embedding, top_k=3):
    _, indices = index.search(query_embedding, top_k)
    return [documents[i] for i in indices[0]]
