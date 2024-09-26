# **AI-Powered Web Application for Document Search and Analysis**

A project to develop a web application that allows users to upload documents and use AI methods to search and analyze them.

## **Table of Contents**

- [Features](#features)
- [Technology Stack](#technology-stack)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)

## **Features**

- **Document Upload:** Users can upload various documents.
- **Semantic Search:** Search documents using AI and LLMs.
- **Text Summarization:** Get summaries of document content.
- **User-Friendly Frontend:** Intuitive interface with Svelte.
- **RESTful API:** Backend implemented with FastAPI.

## **Technology Stack**

- **Programming Languages:** Python (backend), JavaScript (frontend)
- **Backend:** FastAPI
- **Frontend:** Svelte
- **Database:** PostgreSQL
- **AI Libraries:** LangChain
- **Containerization:** Docker, Docker Compose
- **Version Control:** Git
- **Code Quality:** pre-commit

## **Installation**

### **Prerequisites**

- **Git**
- **Docker and Docker Compose**

### **Steps**

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/your-username/your-repo.git
   cd your-repo
   ```

2. **Adjust Environment Files:**

   - Copy the example files and adjust them if necessary.

     ```bash
     cp backend/.env.example backend/.env
     cp frontend/.env.example frontend/.env
     ```

3. **Start Docker Containers:**

   ```bash
   docker-compose up --build
   ```

4. **Access the Application:**

   - Frontend: `http://localhost:3000`
   - Backend API Documentation: `http://localhost:8000/docs`

## **Usage**

1. **Document Upload:**

   - Navigate to the upload page and upload a document.

2. **Semantic Search:**

   - Enter a search term to receive relevant results.

3. **Text Summarization:**

   - Select a document to get a summary of its content.

## **Project Structure**

```
├── backend
│   ├── app
│   │   ├── main.py
│   │   ├── models.py
│   │   ├── routes.py
│   │   └── ...
│   ├── tests
│   └── Dockerfile
├── frontend
│   ├── src
│   │   ├── App.svelte
│   │   ├── components
│   │   └── ...
│   ├── public
│   ├── tests
│   └── Dockerfile
├── docker-compose.yml
└── README.md
```

## **Contributing**

Contributions are welcome! Please fork the repository and open a pull request.

1. **Fork it**
2. **Create your feature branch:**

   ```bash
   git checkout -b feature/new-feature
   ```

3. **Commit your changes:**

   ```bash
   git commit -m 'Add new feature'
   ```

4. **Push to the branch:**

   ```bash
   git push origin feature/new-feature
   ```

5. **Open a pull request**

## **License**

This project is licensed under the [MIT License](LICENSE).

---

**Note:** This project was created as part of a four-day development plan and serves demonstration purposes.
