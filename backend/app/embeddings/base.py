from abc import abstractmethod
from typing import List

from langchain_core.embeddings import Embeddings


class EmbeddingsBase(Embeddings):
    @abstractmethod
    def embed_documents(self, texts: List[str]) -> List[List[float]]:
        pass

    @abstractmethod
    def embed_query(self, query: str) -> List[float]:
        pass
