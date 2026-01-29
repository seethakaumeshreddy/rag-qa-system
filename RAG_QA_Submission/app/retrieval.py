from sentence_transformers import SentenceTransformer
from app.vector_store import search
from app.llm import generate_answer

model = SentenceTransformer("all-MiniLM-L6-v2")

def ask_question(question):
    q_emb = model.encode([question])
    contexts = search(q_emb)
    return generate_answer(question, contexts)
