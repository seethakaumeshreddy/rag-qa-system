from PyPDF2 import PdfReader
from sentence_transformers import SentenceTransformer
from app.vector_store import save_embeddings

model = SentenceTransformer("all-MiniLM-L6-v2")

def ingest_document(file):
    content = ""
    if file.filename.endswith(".pdf"):
        reader = PdfReader(file.file)
        for page in reader.pages:
            content += page.extract_text()
    else:
        content = file.file.read().decode()

    chunks = chunk_text(content)
    embeddings = model.encode(chunks)
    save_embeddings(chunks, embeddings)

def chunk_text(text, chunk_size=500, overlap=50):
    words = text.split()
    return [" ".join(words[i:i+chunk_size]) for i in range(0, len(words), chunk_size-overlap)]
