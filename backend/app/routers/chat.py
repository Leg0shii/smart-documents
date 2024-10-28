# backend/app/routers/chat.py
from app.ai import perform_semantic_search_chunks
from app.database import get_db
from app.embeddings.openai_embeddings import OpenAIEmbeddingsAdapter
from app.schemas import ChatRequest, ChatResponse
from dotenv import load_dotenv
from fastapi import APIRouter, Depends, HTTPException
from langchain_openai import ChatOpenAI
from requests import Session

load_dotenv()

router = APIRouter(
    prefix="/chat",
    tags=["chat"],
)


@router.post("/", response_model=ChatResponse)
async def chat(request: ChatRequest, db: Session = Depends(get_db)):
    query = request.message
    embeddings_adapter = OpenAIEmbeddingsAdapter()
    top_k = 2

    try:
        search_results = await perform_semantic_search_chunks(
            query=query,
            top_k=top_k,
            db=db,
            embeddings=embeddings_adapter,
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

    sources = [result.title for result in search_results]
    context = "\n\n".join(
        [
            f"Quelle: {result.title}\nText: {result.chunk_text}"
            for result in search_results
        ]
    )

    history = request.history[-10:]
    history_text_full = "\n".join([f"{msg.sender}: {msg.text}" for msg in history])
    history_text = history_text_full[-500:]

    full_context = f"{history_text}\n\n{context}" if history_text else context

    prompt = (
        "Du bist ein hilfreicher Assistent. Beantworte die folgende Frage "
        "basierend auf dem bereitgestellten Kontext. "
        f"Frage: {query}\n\nKontext:\n{full_context}\n\nAntwort:"
    )

    llm = ChatOpenAI()
    reply = llm.invoke(prompt)

    reply_text = f"{reply.content}\n\nVerwendete Quellen: {', '.join(set(sources))}"

    return ChatResponse(reply=reply_text, sources=sources)
