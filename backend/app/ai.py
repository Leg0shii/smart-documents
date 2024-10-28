# backend/app/ai.py
import json
import logging
from typing import List

from app.embeddings.base import EmbeddingsBase
from app.llm.base import LLMBase
from app.models import Document, SearchIndex
from app.schemas import SearchResult
from dotenv import load_dotenv
from fastapi import HTTPException
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from openai import RateLimitError
from sqlalchemy.orm import Session

load_dotenv()

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


async def generate_summary(
    file_path: str, llm: LLMBase = None
) -> dict[str, str | list[str | dict]]:
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            text = f.read()

        prompt = (
            f"Please provide a concise summary of the following document:\n\n{text}"
        )

        summary_message = await llm.generate_summary(prompt)

        summary = {"summary": summary_message, "full_text": text}
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


# generate numerical representations of the text, capture semantic information
async def generate_embeddings(file_path: str, embeddings: EmbeddingsBase = None) -> str:
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            text = f.read()

        splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
        chunks = splitter.split_text(text)
        document_embeddings = embeddings.embed_documents(chunks)
        embeddings_json = json.dumps(document_embeddings)
        logger.info("Embeddings generated successfully.")

        return embeddings_json
    except Exception as e:
        logger.error(f"Error generating embeddings: {e}")
        return "An error occurred while generating embeddings."


async def perform_semantic_search(
    query: str, top_k: int, db: Session, embeddings: EmbeddingsBase = None
) -> List[SearchResult]:
    try:
        search_indices = db.query(SearchIndex).all()

        texts = []
        metadatas = []
        for index in search_indices:
            document = db.query(Document).filter_by(id=index.document_id).first()
            if document:
                # Use the document's main content for semantic search
                text = document.description  # Use the appropriate field
                texts.append(text)

                # Collect metadata
                metadatas.append(
                    {
                        "id": document.id,
                        "title": document.title,
                        "summary": document.summary,
                    }
                )

        if not texts:
            logger.warning("No texts available for semantic search.")
            return []

        # create a vector store from the collected texts and their embeddings
        # vector store does efficient similarity searches by indexing the embeddings
        vector_store = FAISS.from_texts(texts, embeddings, metadatas=metadatas)
        similar_docs = vector_store.similarity_search(query, k=top_k)

        results = []
        for doc in similar_docs:
            result = SearchResult(
                document_id=int(doc.metadata.get("id", 0)),
                title=doc.metadata.get("title", ""),
                description=doc.page_content,
                summary=doc.metadata.get("summary", ""),
                relevance_score=0.0,
            )
            results.append(result)

        logger.info(
            f"Semantic search completed successfully. Found {len(results)} results."
        )
        return results
    except Exception as e:
        logger.error(f"Error performing semantic search: {e}", exc_info=True)
        return []
