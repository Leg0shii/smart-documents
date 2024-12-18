# backend/app/schemas.py
from datetime import datetime
from typing import List, Optional

from pydantic import BaseModel, ConfigDict, EmailStr, Field


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
    password: str


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


class DocumentDetailResponse(BaseModel):
    id: int
    user_id: int
    title: str
    description: Optional[str]
    summary: Optional[str] = None
    content: Optional[str]
    uploaded_at: datetime
    uploader: UserBase
    tags: List[str] = []

    model_config = ConfigDict(from_attributes=True)


class SearchIndexResponse(BaseModel):
    id: int
    document_id: int
    embedding_vector: str

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


# schemas.py
class ChunkSearchResult(BaseModel):
    document_id: int
    title: str
    chunk_id: int
    chunk_text: str
    relevance_score: float

    model_config = ConfigDict(from_attributes=True)


class Citation(BaseModel):
    source_id: int = Field(..., description="The ID of the source used.")
    quote: str = Field(..., description="The exact text from the source.")
    source_title: str = Field(..., description="The title of the source.")


class CitedAnswer(BaseModel):
    answer: str = Field(..., description="The assistant's answer.")
    citations: List[Citation] = Field(
        ..., description="List of citations used in the answer."
    )


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


class TokenWithUser(Token):
    user: UserResponse


class ChatMessage(BaseModel):
    sender: str
    text: str
    time: str


class ChatRequest(BaseModel):
    message: str
    history: List[ChatMessage]


class ChatResponse(BaseModel):
    reply: str
