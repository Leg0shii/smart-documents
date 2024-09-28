import os
from datetime import datetime
from typing import List, Optional

from fastapi import APIRouter, Depends, File, HTTPException, UploadFile
from sqlalchemy.orm import Session

from ..database import get_db
from ..models import Document, Tag
from ..schemas import DocumentResponse

router = APIRouter(
    prefix="/documents",
    tags=["documents"],
)

UPLOAD_DIR = "uploads/documents/"


@router.post("/", response_model=DocumentResponse)
def upload_document(
    title: str,
    description: Optional[str] = None,
    tags: Optional[List[str]] = [],
    file: UploadFile = File(...),
    db: Session = Depends(get_db),
    user_id: int = 1,  # Placeholder for authenticated user
):
    # Save the uploaded file
    timestamp = datetime.utcnow().strftime("%Y%m%d%H%M%S")
    filename = f"{timestamp}_{file.filename}"
    file_path = os.path.join(UPLOAD_DIR, filename)
    os.makedirs(UPLOAD_DIR, exist_ok=True)
    with open(file_path, "wb") as buffer:
        buffer.write(file.file.read())

    # Create Document entry
    document = Document(
        user_id=user_id,
        title=title,
        description=description,
        file_path=file_path,
        uploaded_at=datetime.utcnow(),
    )

    # Handle tags
    for tag_name in tags:
        tag = db.query(Tag).filter(Tag.name == tag_name).first()
        if not tag:
            tag = Tag(name=tag_name)
        document.tags.append(tag)

    db.add(document)
    db.commit()
    db.refresh(document)
    return document


@router.get("/", response_model=List[DocumentResponse])
def get_documents(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    documents = db.query(Document).offset(skip).limit(limit).all()
    return documents


@router.get("/{document_id}", response_model=DocumentResponse)
def get_document(document_id: int, db: Session = Depends(get_db)):
    document = db.query(Document).filter(Document.id == document_id).first()
    if not document:
        raise HTTPException(status_code=404, detail="Document not found")
    return document
