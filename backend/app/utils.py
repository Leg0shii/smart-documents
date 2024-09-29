import os
from datetime import datetime

from fastapi import UploadFile
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def hash_password(password: str) -> str:
    return pwd_context.hash(password)


def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)


def save_file(file: UploadFile, upload_dir: str) -> str:
    timestamp = datetime.utcnow().strftime("%Y%m%d%H%M%S")
    filename = f"{timestamp}_{file.filename}"
    file_path = os.path.join(upload_dir, filename)
    os.makedirs(upload_dir, exist_ok=True)
    with open(file_path, "wb") as buffer:
        buffer.write(file.file.read())
    return file_path
