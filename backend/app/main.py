from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .database import Base, engine
from .routers import items  # Ensure this is correct

Base.metadata.create_all(bind=engine)
app = FastAPI()
app.include_router(items.router)

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
