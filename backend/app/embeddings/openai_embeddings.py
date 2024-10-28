from typing import List

from app.embeddings.base import EmbeddingsBase
from langchain_openai import OpenAIEmbeddings


class OpenAIEmbeddingsAdapter(EmbeddingsBase):
    def __init__(self):
        self.embeddings = OpenAIEmbeddings()

    def embed_documents(self, texts: List[str]) -> List[List[float]]:
        return self.embeddings.embed_documents(texts)

    def embed_query(self, query: str) -> List[float]:
        return self.embeddings.embed_query(query)
