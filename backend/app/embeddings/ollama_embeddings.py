from typing import List

from app.embeddings.base import EmbeddingsBase
from langchain_ollama import OllamaEmbeddings


class OllamaEmbeddingsAdapter(EmbeddingsBase):
    def __init__(self):
        self.embeddings = OllamaEmbeddings(model="nomic-embed-text")

    def embed_documents(self, texts: List[str]) -> List[List[float]]:
        return self.embeddings.embed_documents(texts)

    def embed_query(self, query: str) -> List[float]:
        return self.embeddings.embed_query(query)
