from fastapi import FastAPI, Request
from fastapi.responses import FileResponse, HTMLResponse
from fastapi.staticfiles import StaticFiles
import os

app = FastAPI()

frontend_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../frontend'))
static_dir = os.path.join(frontend_dir, 'public')
app.mount("/static", StaticFiles(directory=static_dir), name="static")

@app.get("/", response_class=HTMLResponse)
async def read_index():
    index_file = os.path.join(static_dir, 'index.html')
    return FileResponse(index_file)

@app.get("/api/message")
async def api_message():
    return {"message": "Moin from FastAPI!"}

@app.get("/{full_path:path}", response_class=HTMLResponse)
async def catch_all(full_path: str, request: Request):
    file_path = os.path.join(static_dir, full_path)
    if os.path.isfile(file_path):
        return FileResponse(file_path)
    else:
        index_file = os.path.join(static_dir, 'index.html')
        return FileResponse(index_file)
