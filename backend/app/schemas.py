# backend/app/schemas.py
from typing import Optional

from pydantic import BaseModel, ConfigDict


class ItemBase(BaseModel):
    name: str
    description: str
    price: Optional[float] = None


class ItemCreate(ItemBase):
    pass


class ItemResponse(ItemBase):
    id: int
    model_config = ConfigDict(from_attributes=True)
