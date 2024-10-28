import asyncio

from app.llm.base import LLMBase
from langchain_openai import ChatOpenAI


class OpenAILLMAdapter(LLMBase):
    def __init__(self, model_name: str = "gpt-3.5-turbo"):
        self.chat_llm = ChatOpenAI(model_name=model_name)

    async def generate_summary(self, prompt: str) -> str:
        loop = asyncio.get_event_loop()
        summary_message = await loop.run_in_executor(
            None, lambda: self.chat_llm.invoke(prompt)
        )
        return summary_message.content
