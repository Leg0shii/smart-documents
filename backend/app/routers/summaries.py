# backend/app/routers/summaries.py
from app.database import get_db
from app.models import Document
from app.schemas import SummaryResponse
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

router = APIRouter(
    prefix="/summaries",
    tags=["summaries"],
)


@router.get("/{document_id}", response_model=SummaryResponse)  # Add this GET method
async def get_summary(document_id: int, db: Session = Depends(get_db)):
    document = db.query(Document).filter(Document.id == document_id).first()
    if not document:
        raise HTTPException(status_code=404, detail="Document not found")

    return {"document_id": document.id, "summary": document.summary}
