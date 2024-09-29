# backend/app/schemas.py
from datetime import datetime
from typing import List, Optional

from pydantic import BaseModel, ConfigDict, EmailStr


class TagBase(BaseModel):
    name: str


class TagCreate(TagBase):
    pass


class TagResponse(TagBase):
    id: int

    model_config = ConfigDict(from_attributes=True)


class UserBase(BaseModel):
    username: str
    email: EmailStr


class UserCreate(UserBase):
    password: str  # Plain password; will be hashed in the backend


class UserResponse(UserBase):
    id: int
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)


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

    model_config = ConfigDict(from_attributes=True)


class DocumentUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    tags: Optional[List[str]] = []

    model_config = ConfigDict(from_attributes=True)


class DocumentVersionResponse(BaseModel):
    id: int
    document_id: int
    version_number: int
    file_path: str
    uploaded_at: datetime

    model_config = ConfigDict(from_attributes=True)


class SearchIndexResponse(BaseModel):
    id: int
    document_id: int
    embedding_vector: str  # Adjust type as needed

    model_config = ConfigDict(from_attributes=True)


class SearchRequest(BaseModel):
    query: str
    top_k: Optional[int] = 5

    model_config = ConfigDict(from_attributes=True)


class SearchResult(BaseModel):
    document_id: int
    title: str
    description: Optional[str]
    summary: Optional[str]
    relevance_score: float

    model_config = ConfigDict(from_attributes=True)


class SummaryRequest(BaseModel):
    document_id: int

    model_config = ConfigDict(from_attributes=True)


class SummaryResponse(BaseModel):
    document_id: int
    summary: Optional[str]

    model_config = ConfigDict(from_attributes=True)


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: Optional[str] = None


class UserLogin(BaseModel):
    username: str
    password: str
