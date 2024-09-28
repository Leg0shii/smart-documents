# AI-Powered Web Application for Document Search and Analysis

A project to develop a web application that allows users to upload documents and use AI methods to search and analyze them.

## Table of Contents

- [Features](#features)
- [Technology Stack](#technology-stack)
- [Installation](#installation)
  - [Prerequisites](#prerequisites)
  - [Steps](#steps)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)

## Features

- **Document Upload:** Users can upload various documents.
- **Semantic Search:** Search documents using AI and Large Language Models (LLMs).
- **Text Summarization:** Get summaries of document content.
- **User-Friendly Frontend:** Intuitive interface built with Svelte.
- **RESTful API:** Backend implemented with FastAPI.
- **AI Integration:** Utilizes LangChain for advanced AI functionalities.
- **Containerization:** Fully containerized using Docker and Docker Compose for seamless deployment.

## Technology Stack

- **Programming Languages:** Python (backend), JavaScript (frontend)
- **Backend:** FastAPI
- **Frontend:** Svelte
- **Database:** PostgreSQL
- **AI Libraries:** LangChain
- **Containerization:** Docker, Docker Compose
- **Version Control:** Git
- **Code Quality:** pre-commit
- **Development Tools:** Rollup, sirv-cli

## Installation

### Prerequisites

Before you begin, ensure you have the following installed on your system:

- **Git:** Version control system.
- **Docker:** Platform for developing, shipping, and running applications.
- **Docker Compose:** Tool for defining and running multi-container Docker applications.

### Steps

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/Leg0shii/smart-documents.git
   cd smart-documents
   ```

2. **Set Up Environment Variables:**

   The application uses environment variables for configuration. You can customize these settings by modifying the `.env` files.

   - **Backend Environment Variables:**

     ```bash
     cp backend/.env.example backend/.env
     ```

     Edit `backend/.env` as needed to configure database credentials and other settings.

   - **Frontend Environment Variables:**

     ```bash
     cp frontend/.env.example frontend/.env
     ```

     Edit `frontend/.env` if necessary to adjust frontend configurations.

3. **Start Docker Containers:**

   Build and start the Docker containers using Docker Compose.

   ```bash
   docker-compose up --build
   ```

   This command will:

   - Build the Docker images for the backend and frontend.
   - Start the PostgreSQL database.
   - Launch the FastAPI backend and Svelte frontend services.

4. **Access the Application:**

   - **Frontend Application:** [http://localhost:5000/](http://localhost:5000/)
   - **Backend API Documentation:** [http://localhost:8000/docs](http://localhost:8000/docs) TODO

## Usage

### Document Upload

1. **Navigate to the Upload Page:**

   Open your browser and go to [http://localhost:5000/](http://localhost:5000/).

2. **Upload a Document:**

   - Click on the "Upload Document" button.
   - Select the document you wish to upload from your local machine.
   - Submit the form to upload the document.

### Semantic Search

1. **Access the Search Feature:**

   - On the frontend application, navigate to the "Search" section.

2. **Perform a Search:**

   - Enter a search term or query related to the content of your uploaded documents.
   - Submit the search to receive relevant results powered by AI and LLMs.

### Text Summarization

1. **Select a Document:**

   - From the list of uploaded documents, select the one you wish to summarize.

2. **View Summary:**

   - Click on the "Summarize" button to generate and view a summary of the document's content.

## Project Structure

```
smart-documents
├── backend
│   ├── app
│   │   ├── __init__.py
│   │   ├── main.py
│   │   └── tests
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

- **`backend/app/`**
  - **`__init__.py`**: Marks the directory as a Python package.
  - **`main.py`**: Entry point for the FastAPI application.
  - **`tests/`**: Contains backend tests.
- **`backend/Dockerfile`**: Dockerfile for building the backend service.
- **`backend/requirements.txt`**: Python dependencies for the backend.
- **`backend/.env`**: Environment variables for the backend.

### Frontend

- **`frontend/public/`**
  - **`index.html`**: Main HTML file.
  - **`global.css`**: Global styles.
  - **`favicon.png`**: Favicon for the application.
- **`frontend/src/`**
  - **`App.svelte`**: Main Svelte component.
  - **`main.js`**: Entry point for the Svelte application.
- **`frontend/scripts/`**
  - **`setupTypeScript.js`**: Script for setting up TypeScript (if applicable).
- **`frontend/Dockerfile`**: Dockerfile for building the frontend service.
- **`frontend/package.json`**: NPM dependencies and scripts for the frontend.
- **`frontend/rollup.config.js`**: Rollup configuration for bundling the frontend.
- **`frontend/.env`**: Environment variables for the frontend.

### Root Directory

- **`docker-compose.yml`**: Docker Compose configuration to orchestrate the backend, frontend, and database services.
- **`.gitignore`**: Specifies files and directories to ignore in Git.
- **`LICENSE`**: License information.
- **`README.md`**: Project documentation.

## Contributing

Contributions are welcome! Please follow these steps to contribute to the project:

1. **Fork the Repository:**

   Click the "Fork" button at the top right of the repository page to create a copy of the project under your GitHub account.

2. **Clone Your Fork:**

   ```bash
   git clone https://github.com/Leg0shii/smart-documents.git
   cd smart-documents
   ```

3. **Create a Feature Branch:**

   ```bash
   git checkout -b feature/new-feature
   ```

4. **Commit Your Changes:**

   ```bash
   git commit -m 'Add new feature'
   ```

5. **Push to the Branch:**

   ```bash
   git push origin feature/new-feature
   ```

6. **Open a Pull Request:**

   - Navigate to your forked repository on GitHub.
   - Click the "Compare & pull request" button.
   - Provide a descriptive title and detailed description of your changes.
   - Submit the pull request for review.

## License

This project is licensed under the [MIT License](LICENSE).

---

**Note:** This project was created as part of a four-day development plan and serves demonstration purposes.
