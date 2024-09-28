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

WORKDIR /app

# dependencies
COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . .

# port FastAPI
EXPOSE ${BACKEND_PORT}

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "${BACKEND_PORT}", "--reload"]
