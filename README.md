# AI-Powered Document Search and Analysis

This is an AI-powered web application that allows users to upload documents, perform semantic searches using large language models (LLMs), and generate document summaries.

## Features

- **Document Upload**: Upload documents for search and analysis.
- **Semantic Search**: Perform AI-based contextual searches using LLMs.
- **Chat with Documents**: Chat with your documents using LLMs.
- **Text Summarization**: Generate concise summaries of document content.
- **User Authentication**: Secure login and registration with JWT tokens.

## Tech Stack

- **Backend**: Python (FastAPI)
- **Frontend**: Svelte
- **Database**: PostgreSQL
- **AI Libraries**: LangChain, OpenAI
- **Containerization**: Docker, Docker Compose

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/Leg0shii/smart-documents.git
   cd smart-documents
   ```

2. **Set up the environment variables** in `backend/.env`:
   ```env
   FRONTEND_PORT=5000
   BACKEND_PORT=8000
   SECRET_KEY=your_secret_key
   OPENAI_API_KEY=your_openai_api_key
   POSTGRES_USER=postgres
   POSTGRES_PASSWORD=postgres
   POSTGRES_DB=smart_documents
   POSTGRES_HOST=db
   POSTGRES_PORT=5432
   DATABASE_URL=postgresql://${POSTGRES_USER}:${POSTGRES_PASSWORD}@${POSTGRES_HOST}:${POSTGRES_PORT}/${POSTGRES_DB}
   ```

3. **Run the application with Docker**:
   ```bash
   docker-compose up --build
   ```

4. **Access the application**:
   - Frontend: `http://localhost:5000`
   - Backend: `http://localhost:8000`

## Usage

- **Register/Login**: Create an account or log in.
- **Upload Documents**: Upload your documents for search.
- **Perform Search**: Use the search bar to find documents with custom top K results.
- **Get Summaries**: Retrieve summaries of the search results.

## Development

To run locally without Docker:

- **Backend**:
  ```bash
  cd backend
  pip install -r requirements.txt
  uvicorn app.main:app --reload
  ```

- **Frontend**:
  ```bash
  cd frontend
  npm install
  npm run dev
  ```

## License

This project is licensed under the MIT License.
