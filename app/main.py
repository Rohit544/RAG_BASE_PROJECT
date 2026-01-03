from fastapi import FastAPI
from app.api.routes import router, set_chain
from app.ingestion.loader import load_pdf
from app.ingestion.chunker import chunk_documents
from app.embeddings.embedding import get_embeddings
from app.vectorstore.faiss_store import create_vectorstore
from app.rag.chain import create_rag_chain
from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app = FastAPI()

docs = load_pdf("data/policy.pdf")
chunks = chunk_documents(docs)
embeddings = get_embeddings()
vectorstore = create_vectorstore(chunks, embeddings)
rag_chain = create_rag_chain(vectorstore)

set_chain(rag_chain)
app.include_router(router)
