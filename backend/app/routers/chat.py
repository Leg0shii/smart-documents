# backend/app/routers/chat.py
from app.ai import perform_semantic_search_chunks
from app.database import get_db
from app.embeddings.openai_embeddings import OpenAIEmbeddingsAdapter
from app.schemas import ChatRequest, ChatResponse, CitedAnswer
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
    top_k = 5

    try:
        search_results = await perform_semantic_search_chunks(
            query=query,
            top_k=top_k,
            db=db,
            embeddings=embeddings_adapter,
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

    if not search_results:
        context = ""
        sources = {}
    else:
        context = "\n\n".join(
            [
                f"Source {idx}:\n{result.chunk_text}"
                for idx, result in enumerate(search_results)
            ]
        )
        sources = {idx: result.title for idx, result in enumerate(search_results)}

    # Limit conversation history to last 500 characters
    history = request.history[-10:]
    history_text_full = "\n".join([f"{msg.sender}: {msg.text}" for msg in history])
    history_text = history_text_full[-500:]

    # Set full_context to only the retrieved context
    full_context = context

    # Build the prompt
    prompt = (
        "You are an assistant for question-answering tasks. "
        "Use only the following pieces of retrieved context to answer the question. "
        "If the answer is not in the provided context, answer it "
        "without using the context.' "
        "Do not use the conversation history as a source of information. "
        "Do not make up any information or sources. "
        "Reference the sources by their IDs in your citations. "
        "Provide the answer and include citations in the specified format.\n\n"
    )

    if history_text:
        prompt += f"Conversation History:\n{history_text}\n\n"

    prompt += f"Question: {query}\n\nContext:\n{full_context}\n\nAnswer:"

    # Initialize the LLM with structured output
    llm = ChatOpenAI().with_structured_output(CitedAnswer)

    # Generate the response
    try:
        cited_answer = llm.invoke(prompt)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"LLM Error: {str(e)}")

    # Prepare the reply text
    reply_text = cited_answer.answer
    if cited_answer.citations:
        reply_text += "\n\nSources:\n"
        for citation in cited_answer.citations:
            source_title = sources.get(citation.source_id, "Unknown Source")
            reply_text += f'- {source_title}: "{citation.quote}"\n'

    return ChatResponse(reply=reply_text)
