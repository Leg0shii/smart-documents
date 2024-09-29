from app.database import Base, engine
from app.routers import auth, documents, search, summaries, tags, users
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

Base.metadata.create_all(bind=engine)
app = FastAPI()

app.include_router(users.router)
app.include_router(documents.router)
app.include_router(tags.router)
app.include_router(search.router)
app.include_router(summaries.router)
app.include_router(auth.router)

origins = [
    "http://localhost:5000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/api/message")
async def api_message():
    return {"message": "Moin from FastAPI!"}
