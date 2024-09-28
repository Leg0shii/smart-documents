# backend/app/routers/items.py

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from ..database import get_db
from ..models import Item
from ..schemas import ItemCreate, ItemResponse

router = APIRouter(
    prefix="/items",
    tags=["items"],
)

@router.post("/", response_model=ItemResponse)
def create_item(item: ItemCreate, db: Session = Depends(get_db)):
    db_item = Item(**item.model_dump())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item