from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .database import Base, engine
from .routers import documents, tags, users

Base.metadata.create_all(bind=engine)
app = FastAPI()

app.include_router(users.router)
app.include_router(documents.router)
app.include_router(tags.router)

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
