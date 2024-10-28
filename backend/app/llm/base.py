from abc import ABC, abstractmethod


class LLMBase(ABC):
    @abstractmethod
    async def generate_summary(self, prompt: str) -> str:
        pass
