# RAG-Based Question Answering System

## Objective
Build a Retrieval-Augmented Generation (RAG) system where users upload documents and ask questions based on them.

## Tech Stack
- FastAPI
- Sentence Transformers
- FAISS
- PyPDF2

## Setup
```bash
pip install -r requirements.txt
uvicorn app.main:app --reload
```

## API Endpoints
- POST /upload : Upload PDF or TXT
- POST /ask : Ask questions

## Example
```json
{"question": "What is AI?"}
```
