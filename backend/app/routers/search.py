# backend/app/routers/search.py
from typing import List

from app.ai import perform_semantic_search
from app.database import get_db
from app.embeddings.ollama_embeddings import OllamaEmbeddingsAdapter
from app.schemas import SearchRequest, SearchResult
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

router = APIRouter(
    prefix="/search",
    tags=["search"],
)


@router.post("/", response_model=List[SearchResult])
async def semantic_search(search_request: SearchRequest, db: Session = Depends(get_db)):
    query = search_request.query
    top_k = search_request.top_k
    embeddings = OllamaEmbeddingsAdapter()

    try:
        results = await perform_semantic_search(query, top_k, db, embeddings)
        return results
    except ValueError as ve:
        raise HTTPException(status_code=400, detail=str(ve))
    except Exception:
        raise HTTPException(status_code=500, detail="Internal Server Error")
