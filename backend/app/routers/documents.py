# backend/app/routers/documents.py
import os
from datetime import datetime
from typing import List, Optional

from app.ai import generate_embeddings, generate_summary
from app.database import get_db
from app.dependencies import get_current_user
from app.models import Document, DocumentVersion, SearchIndex, Tag, User
from app.schemas import DocumentResponse, DocumentUpdate
from app.utils import save_file
from fastapi import APIRouter, Depends, File, Form, HTTPException, UploadFile
from sqlalchemy.orm import Session

router = APIRouter(
    prefix="/documents",
    tags=["documents"],
)

UPLOAD_DIR = "uploads/documents/"


@router.post("/", response_model=DocumentResponse)
async def upload_document(
    title: str = Form(...),
    description: Optional[str] = Form(None),
    tags: Optional[List[str]] = Form([]),
    file: UploadFile = File(...),
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    user_id = current_user.id

    file_path = save_file(file, UPLOAD_DIR)
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

    # initial DocumentVersion
    version = DocumentVersion(
        document_id=document.id,
        version_number=1,
        file_path=file_path,
        uploaded_at=document.uploaded_at,
    )
    db.add(version)
    db.commit()
    db.refresh(version)

    summary = await generate_summary(file_path)
    embeddings = await generate_embeddings(file_path)

    # Update Document with summary
    document.summary = summary
    db.commit()
    db.refresh(document)

    # Create SearchIndex entry
    search_index = SearchIndex(
        document_id=document.id,
        embedding_vector=embeddings,
    )
    db.add(search_index)
    db.commit()
    db.refresh(search_index)

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


@router.put("/{document_id}", response_model=DocumentResponse)
def update_document(
    document_id: int, document_update: DocumentUpdate, db: Session = Depends(get_db)
):
    document = db.query(Document).filter(Document.id == document_id).first()
    if not document:
        raise HTTPException(status_code=404, detail="Document not found")

    if document_update.title:
        document.title = document_update.title
    if document_update.description:
        document.description = document_update.description

    if document_update.tags:
        # Clear existing tags
        document.tags = []
        for tag_name in document_update.tags:
            tag = db.query(Tag).filter_by(name=tag_name).first()
            if not tag:
                tag = Tag(name=tag_name)
            document.tags.append(tag)

    db.commit()
    db.refresh(document)
    return document


@router.delete("/{document_id}", response_model=dict)
def delete_document(document_id: int, db: Session = Depends(get_db)):
    document = db.query(Document).filter(Document.id == document_id).first()
    if not document:
        raise HTTPException(status_code=404, detail="Document not found")

    # Delete associated files
    try:
        os.remove(document.file_path)
        for version in document.versions:
            os.remove(version.file_path)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error deleting files: {e}")

    db.delete(document)
    db.commit()
    return {"detail": "Document deleted successfully"}
