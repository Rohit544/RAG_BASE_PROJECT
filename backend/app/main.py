import os
from app.ingestion.loader import load_pdf

def ingest_all_pdfs():
    docs = []
    for file in os.listdir("data/uploads"):
        if file.endswith(".pdf"):
            docs.extend(load_pdf(f"data/uploads/{file}"))
    return docs
