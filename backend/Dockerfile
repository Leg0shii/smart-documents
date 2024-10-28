# backend/Dockerfile

FROM python:3.11-slim

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        build-essential \
        libpq-dev \
        gcc \
        && rm -rf /var/lib/apt/lists/*

# env
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV PYTHONPATH=/app

WORKDIR /app

# dependencies
COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

RUN curl -fsSL https://ollama.com/install.sh | sh

RUN ollama serve & \
    # Wait for Ollama to be ready
    for i in {1..30}; do \
        if ollama status >/dev/null 2>&1; then \
            echo "Ollama is up"; \
            break; \
        fi; \
        echo "Waiting for Ollama to start... ($i/30)"; \
        sleep 1; \
    done && \
    ollama pull llama3.1:8b-instruct-q8_0 && \
    ollama pull nomic-embed-text

COPY . .

COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

# port FastAPI
EXPOSE ${BACKEND_PORT}

CMD ["/entrypoint.sh"]
