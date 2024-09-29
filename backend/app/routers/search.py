# backend/app/routers/search.py
from typing import List

from app.ai import perform_semantic_search
from app.database import get_db
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

    # Perform semantic search using LangChain
    results = await perform_semantic_search(query, top_k, db)

    try:
        # Perform semantic search using LangChain
        results = await perform_semantic_search(query, top_k, db)
        return results
    except ValueError as ve:
        raise HTTPException(status_code=400, detail=str(ve))
    except Exception:
        raise HTTPException(status_code=500, detail="Internal Server Error")
