from fastapi import FastAPI, UploadFile, BackgroundTasks
from fastapi.responses import HTMLResponse

from app.ingestion import ingest_document
from app.retrieval import ask_question
from app.models import QueryRequest

app = FastAPI(title="RAG QA System")


@app.get("/", response_class=HTMLResponse)
def home():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>RAG QA System</title>
    </head>
    <body style="font-family: Arial; text-align:center; padding-top:60px;">
        <h1>✅ RAG Question Answering System</h1>
        <p>Server is running successfully</p>
        <p><a href="/docs">Open API Documentation</a></p>
    </body>
    </html>
    """


@app.post("/upload")
async def upload(file: UploadFile, background_tasks: BackgroundTasks):
    background_tasks.add_task(ingest_document, file)
    return {"message": "Document ingestion started"}


@app.post("/ask")
async def ask(query: QueryRequest):
    return {"answer": ask_question(query.question)}
