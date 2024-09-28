# AI-Powered Web Application for Document Search and Analysis

A project to develop a web application that allows users to upload documents and use AI methods to search and analyze them.

## Table of Contents

- [Features](#features)
- [Technology Stack](#technology-stack)
- [Installation](#installation)
  - [Prerequisites](#prerequisites)
  - [Steps](#steps)
    - [Clone the Repository](#clone-the-repository)
    - [Set Up Environment Variables](#set-up-environment-variables)
    - [Run Database Migrations](#run-database-migrations)
    - [Start Docker Containers](#start-docker-containers)
- [Usage](#usage)
  - [Document Upload](#document-upload)
  - [Semantic Search](#semantic-search)
  - [Text Summarization](#text-summarization)
- [Project Structure](#project-structure)
  - [Backend](#backend)
  - [Frontend](#frontend)
  - [Root Directory](#root-directory)
- [Database Migrations](#database-migrations)
  - [Generating a New Migration](#generating-a-new-migration)
  - [Applying Migrations](#applying-migrations)
- [Contributing](#contributing)
- [License](#license)

---

## Features

- **Document Upload**: Users can upload various documents.
- **Semantic Search**: Search documents using AI and Large Language Models (LLMs).
- **Text Summarization**: Get summaries of document content.
- **User-Friendly Frontend**: Intuitive interface built with Svelte.
- **RESTful API**: Backend implemented with FastAPI.
- **AI Integration**: Utilizes LangChain for advanced AI functionalities.
- **Containerization**: Fully containerized using Docker and Docker Compose for seamless deployment.
- **Database Migrations**: Manage database schema changes effortlessly with Alembic.

## Technology Stack

- **Programming Languages**: Python (backend), JavaScript (frontend)
- **Backend**: FastAPI
- **Frontend**: Svelte
- **Database**: PostgreSQL
- **AI Libraries**: LangChain
- **Database Migrations**: Alembic
- **Containerization**: Docker, Docker Compose
- **Version Control**: Git
- **Code Quality**: pre-commit
- **Development Tools**: Rollup, sirv-cli

## Installation

### Prerequisites

Before you begin, ensure you have the following installed on your system:

- **Git**: Version control system.
- **Docker**: Platform for developing, shipping, and running applications.
- **Docker Compose**: Tool for defining and running multi-container Docker applications.

### Steps

#### Clone the Repository

```bash
git clone https://github.com/Leg0shii/smart-documents.git
cd smart-documents
```

#### Set Up Environment Variables

The application uses environment variables for configuration. You can customize these settings by modifying the `.env` files.

##### Environment Variable:

```bash
cp .env
```

- **Edit `.env`** as needed to configure database credentials and other settings.

#### Run Database Migrations

Alembic is integrated to manage database schema changes. Follow these steps to apply migrations:

1. **Generate Migration Scripts** (if you've made changes to the models):

   ```bash
   docker-compose run backend alembic revision --autogenerate -m "Your migration message"
   ```

   - Replace `"Your migration message"` with a descriptive message about the changes.

2. **Apply Migrations**:

   ```bash
   docker-compose run backend alembic upgrade head
   ```

   - This command applies all pending migrations to the PostgreSQL database.

> **Note:** The Docker setup automatically runs migrations on startup. However, manually running migrations ensures that your database schema is up-to-date, especially during development.

#### Start Docker Containers

Build and start the Docker containers using Docker Compose.

```bash
docker-compose up --build -d
```

This command will:

- **Build** the Docker images for the backend and frontend.
- **Start** the PostgreSQL database.
- **Launch** the FastAPI backend and Svelte frontend services.
- **Apply** any pending database migrations.

#### Access the Application

- **Frontend Application**: [http://localhost:5000/](http://localhost:5000/)
- **Backend API Documentation**: [http://localhost:8000/docs](http://localhost:8000/docs) TODO

## Usage

### Document Upload

1. **Navigate to the Upload Page**:

   Open your browser and go to [http://localhost:5000/](http://localhost:5000/).

2. **Upload a Document**:

   - Click on the "Upload Document" button.
   - Select the document you wish to upload from your local machine.
   - Submit the form to upload the document.

### Semantic Search

1. **Access the Search Feature**:

   On the frontend application, navigate to the "Search" section.

2. **Perform a Search**:

   - Enter a search term or query related to the content of your uploaded documents.
   - Submit the search to receive relevant results powered by AI and LLMs.

### Text Summarization

1. **Select a Document**:

   From the list of uploaded documents, select the one you wish to summarize.

2. **View Summary**:

   Click on the "Summarize" button to generate and view a summary of the document's content.

## Project Structure

```
smart-documents
├── backend
│   ├── app
│   │   ├── __init__.py
│   │   ├── main.py
│   │   ├── models.py
│   │   ├── database.py
│   │   ├── routers
│   │   │   └── ... (router modules)
│   │   ├── schemas.py
│   │   └── tests
│   ├── alembic
│   │   ├── env.py
│   │   ├── README
│   │   ├── script.py.mako
│   │   └── versions
│   ├── .dockerignore
│   ├── .env
│   ├── Dockerfile
│   └── requirements.txt
├── frontend
│   ├── public
│   │   ├── favicon.png
│   │   ├── global.css
│   │   └── index.html
│   ├── scripts
│   │   └── setupTypeScript.js
│   └── src
│       ├── App.svelte
│       └── main.js
│   ├── .dockerignore
│   ├── Dockerfile
│   ├── package.json
│   ├── package-lock.json
│   ├── README.md
│   └── rollup.config.js
├── .gitignore
├── docker-compose.yml
├── LICENSE
└── README.md
```

### Backend

- **backend/app/**:
  - `__init__.py`: Marks the directory as a Python package.
  - `main.py`: Entry point for the FastAPI application.
  - `models.py`: SQLAlchemy models defining the database schema.
  - `database.py`: Database connection and session management.
  - `routers/`: Contains API route modules.
  - `schemas.py`: Pydantic models for request and response validation.
  - `tests/`: Contains backend tests.
- **backend/alembic/**:
  - `env.py`: Alembic environment configuration.
  - `README`: Information about Alembic setup.
  - `script.py.mako`: Template for migration scripts.
  - `versions/`: Directory where migration scripts are stored.
- **backend/Dockerfile**: Dockerfile for building the backend service.
- **backend/requirements.txt**: Python dependencies for the backend.
- **backend/.env**: Environment variables for the backend.
- **backend/.dockerignore**: Specifies files and directories to ignore in Docker builds.

### Frontend

- **frontend/public/**:
  - `index.html`: Main HTML file.
  - `global.css`: Global styles.
  - `favicon.png`: Favicon for the application.
- **frontend/src/**:
  - `App.svelte`: Main Svelte component.
  - `main.js`: Entry point for the Svelte application.
- **frontend/scripts/**:
  - `setupTypeScript.js`: Script for setting up TypeScript (if applicable).
- **frontend/Dockerfile**: Dockerfile for building the frontend service.
- **frontend/package.json**: NPM dependencies and scripts for the frontend.
- **frontend/rollup.config.js**: Rollup configuration for bundling the frontend.
- **frontend/.env**: Environment variables for the frontend.
- **frontend/.dockerignore**: Specifies files and directories to ignore in Docker builds.

### Root Directory

- **docker-compose.yml**: Docker Compose configuration to orchestrate the backend, frontend, and database services.
- **.gitignore**: Specifies files and directories to ignore in Git.
- **LICENSE**: License information.
- **README.md**: Project documentation.

## Database Migrations

Alembic is used to manage database schema changes. Follow these steps to handle migrations:

### Generating a New Migration

1. **Ensure Your Models Are Updated**:

   Modify your SQLAlchemy models as needed. For example, adding a new field to a model.

2. **Generate the Migration Script**:

   ```bash
   docker-compose run backend alembic revision --autogenerate -m "Add price to items table"
   ```

   - **`--autogenerate`**: Alembic detects changes in the models and generates the corresponding migration operations.
   - **`-m "Add price to items table"`**: Descriptive message for the migration.

3. **Review the Migration Script**:

   Navigate to `./backend/alembic/versions/` and open the newly created migration file to ensure it accurately reflects your changes.

### Applying Migrations

Apply all pending migrations to update the database schema.

```bash
docker-compose run backend alembic upgrade head
```

- **`upgrade head`**: Applies all migrations up to the latest one.

> **Note:** In the Docker setup, migrations are automatically applied on container startup. However, running migrations manually ensures that your database is up-to-date, especially during development.

## Contributing

Contributions are welcome! Please follow these steps to contribute to the project:

1. **Fork the Repository**:

   Click the "Fork" button at the top right of the repository page to create a copy of the project under your GitHub account.

2. **Clone Your Fork**:

   ```bash
   git clone https://github.com/Leg0shii/smart-documents.git
   cd smart-documents
   ```

3. **Create a Feature Branch**:

   ```bash
   git checkout -b feature/new-feature
   ```

4. **Commit Your Changes**:

   ```bash
   git commit -m 'Add new feature'
   ```

5. **Push to the Branch**:

   ```bash
   git push origin feature/new-feature
   ```

6. **Open a Pull Request**:

   - Navigate to your forked repository on GitHub.
   - Click the "Compare & pull request" button.
   - Provide a descriptive title and detailed description of your changes.
   - Submit the pull request for review.

## License

This project is licensed under the MIT License.

> **Note:** This project was created as part of a four-day development plan and serves demonstration purposes.
