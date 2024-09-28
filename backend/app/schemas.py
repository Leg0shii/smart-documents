from datetime import datetime
from typing import List, Optional

from pydantic import BaseModel, EmailStr


class TagBase(BaseModel):
    name: str


class TagCreate(TagBase):
    pass


class TagResponse(TagBase):
    id: int

    class Config:
        orm_mode = True


class UserBase(BaseModel):
    username: str
    email: EmailStr


class UserCreate(UserBase):
    password: str  # Plain password; will be hashed in the backend


class UserResponse(UserBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True


class DocumentBase(BaseModel):
    title: str
    description: Optional[str] = None


class DocumentCreate(DocumentBase):
    tags: Optional[List[str]] = []  # List of tag names


class DocumentResponse(DocumentBase):
    id: int
    user_id: int
    file_path: str
    uploaded_at: datetime
    summary: Optional[str] = None
    tags: List[TagResponse] = []

    class Config:
        orm_mode = True


class DocumentVersionResponse(BaseModel):
    id: int
    document_id: int
    version_number: int
    file_path: str
    uploaded_at: datetime

    class Config:
        orm_mode = True


class SearchIndexResponse(BaseModel):
    id: int
    document_id: int
    embedding_vector: str  # Adjust type as needed

    class Config:
        orm_mode = True
