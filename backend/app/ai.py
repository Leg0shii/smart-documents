# backend/app/ai.py

import asyncio
import json
import logging
from typing import List

from app.models import Document, SearchIndex
from app.schemas import SearchResult
from dotenv import load_dotenv
from fastapi import HTTPException
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.embeddings import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_openai.chat_models import ChatOpenAI
from openai import RateLimitError
from sqlalchemy.orm import Session

load_dotenv()

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


async def generate_summary(file_path: str) -> str:
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            text = f.read()

        prompt = (
            f"Please provide a concise summary of the following document:\n\n{text}"
        )

        chat_llm = ChatOpenAI(model_name="gpt-3.5-turbo")

        loop = asyncio.get_event_loop()
        summary_message = await loop.run_in_executor(
            None, lambda: chat_llm.invoke(prompt)
        )

        summary = summary_message.content

        logger.info("Summary generated successfully.")
        return summary

    except RateLimitError:
        logger.warning("Rate limit exceeded.")
        raise HTTPException(
            status_code=429,
            detail="Service is currently unavailable"
            " due to high demand. Please try again later.",
        )
    except FileNotFoundError:
        logger.error(f"File not found: {file_path}")
        raise HTTPException(status_code=404, detail="The specified file was not found.")
    except Exception as e:
        logger.error(f"Error generating summary: {e}")
        raise HTTPException(
            status_code=500,
            detail="An internal server error occurred while generating the summary.",
        )


async def generate_embeddings(file_path: str) -> str:
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            text = f.read()

        splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
        chunks = splitter.split_text(text)
        embeddings = OpenAIEmbeddings()
        document_embeddings = embeddings.embed_documents(chunks)
        embeddings_json = json.dumps(document_embeddings)
        logger.info("Embeddings generated successfully.")

        return embeddings_json
    except Exception as e:
        logger.error(f"Error generating embeddings: {e}")
        return "An error occurred while generating embeddings."


async def perform_semantic_search(
    query: str, top_k: int, db: Session
) -> List[SearchResult]:
    try:
        embeddings = OpenAIEmbeddings()
        search_indices = db.query(SearchIndex).all()

        texts = []
        for index in search_indices:
            document = db.query(Document).filter_by(id=index.document_id).first()
            if document:
                texts.append(document.description)

        if not texts:
            logger.warning("No texts available for semantic search.")
            return []

        vector_store = FAISS.from_texts(texts, embeddings)
        similar_docs = vector_store.similarity_search(query, k=top_k)

        results = []
        for doc in similar_docs:
            result = SearchResult(
                document_id=doc.metadata.get("id", 0),
                title=doc.metadata.get("title", ""),
                description=doc.page_content,
                summary=doc.metadata.get("summary", ""),
                relevance_score=0.0,  # FAISS's does not provide scores
            )
            results.append(result)

        logger.info(
            f"Semantic search completed successfully. Found {len(results)} results."
        )
        return results
    except Exception as e:
        logger.error(f"Error performing semantic search: {e}", exc_info=True)
        return []
