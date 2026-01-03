from langchain.chains import RetrievalQA
from langchain.chat_models import ChatOpenAI
from app.rag.prompt import RAG_PROMPT
from langchain.memory import ConversationBufferMemory



def create_rag_chain(vectorstore):
    retriever = vectorstore.as_retriever(search_kwargs={"k": 4})

    llm = ChatOpenAI(
        model="gpt-3.5-turbo",
        temperature=0
    )

    return RetrievalQA.from_chain_type(
        llm=llm,
        retriever=retriever,
        chain_type_kwargs={"prompt": RAG_PROMPT},
        memory = memory,
        return_source_documents=True
    )
memory = ConversationBufferMemory(
    memory_key="chat_history",
    return_messages=True
)