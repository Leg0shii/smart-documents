# backend/app/routers/summaries.py
from app.ai import generate_summary
from app.database import get_db
from app.models import Document
from app.schemas import SummaryRequest, SummaryResponse
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

router = APIRouter(
    prefix="/summaries",
    tags=["summaries"],
)


@router.post("/", response_model=SummaryResponse)
async def generate_document_summary(
    summary_request: SummaryRequest, db: Session = Depends(get_db)
):
    document = db.query(Document).filter_by(id=summary_request.document_id).first()
    if not document:
        raise HTTPException(status_code=404, detail="Document not found")

    if not document.file_path:
        raise HTTPException(status_code=400, detail="Document file path is missing")

    summary = await generate_summary(document.file_path)
    document.summary = summary
    db.commit()
    db.refresh(document)

    return SummaryResponse(document_id=document.id, summary=summary)
