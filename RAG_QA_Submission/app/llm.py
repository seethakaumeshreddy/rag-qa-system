def generate_answer(question, contexts):
    context = "\n".join(contexts)
    return f"Answer based on documents:\n{context[:500]}"
