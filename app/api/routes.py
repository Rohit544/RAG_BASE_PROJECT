from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

rag_chain = None

class Query(BaseModel):
    question: str

@router.post("/ask")
def ask(query: Query):
    result = rag_chain(query.question)
    return {
        "answer": result["result"],
        "sources": [
            doc.metadata.get("source", "unknown")
            for doc in result["source_documents"]
        ]
    }

def set_chain(chain):
    global rag_chain
    rag_chain = chain
