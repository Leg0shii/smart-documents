# backend/app/routers/tags.py
from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from ..database import get_db
from ..models import Tag
from ..schemas import TagCreate, TagResponse

router = APIRouter(
    prefix="/tags",
    tags=["tags"],
)


@router.post("/", response_model=TagResponse)
def create_tag(tag: TagCreate, db: Session = Depends(get_db)):
    db_tag = db.query(Tag).filter(Tag.name == tag.name).first()
    if db_tag:
        raise HTTPException(status_code=400, detail="Tag already exists")
    new_tag = Tag(name=tag.name)
    db.add(new_tag)
    db.commit()
    db.refresh(new_tag)
    return new_tag


@router.get("/", response_model=List[TagResponse])
def get_tags(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    tags = db.query(Tag).offset(skip).limit(limit).all()
    return tags
