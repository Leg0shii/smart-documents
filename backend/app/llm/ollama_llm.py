import asyncio

from app.llm.base import LLMBase
from langchain_ollama import ChatOllama


class OllamaLLMAdapter(LLMBase):
    def __init__(self, model_name: str = "llama3.1:8b-instruct-q8_0"):
        self.chat_llm = ChatOllama(model=model_name)

    async def generate_summary(self, prompt: str) -> str:
        loop = asyncio.get_event_loop()
        summary_message = await loop.run_in_executor(
            None, lambda: self.chat_llm.invoke(prompt)
        )
        return summary_message.content
