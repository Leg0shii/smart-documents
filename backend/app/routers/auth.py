# backend/app/routers/auth.py

from datetime import datetime, timedelta
from typing import Optional

from app.database import get_db
from app.models import User
from app.schemas import TokenWithUser, UserCreate, UserLogin, UserResponse
from app.utils import hash_password, verify_password
from fastapi import APIRouter, Depends, HTTPException
from jose import jwt
from sqlalchemy.orm import Session

# Secret key to encode JWT tokens
SECRET_KEY = "secret_key"  # Use a secure key in production
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

router = APIRouter(
    prefix="/auth",
    tags=["auth"],
)


def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


@router.post("/register/", response_model=UserResponse)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    db_user = db.query(User).filter_by(username=user.username).first()
    if db_user:
        raise HTTPException(
            status_code=400, detail="Username or email already registered"
        )
    hashed_pw = hash_password(user.password)
    new_user = User(username=user.username, email=user.email, hashed_password=hashed_pw)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


@router.post("/login/", response_model=TokenWithUser)
def login(user_login: UserLogin, db: Session = Depends(get_db)):
    user = db.query(User).filter_by(username=user_login.username).first()
    if not user:
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    if not verify_password(user_login.password, user.hashed_password):
        raise HTTPException(status_code=400, detail="Incorrect username or password")

    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return {
        "access_token": access_token,
        "token_type": "bearer",
        "user": UserResponse.from_orm(user),
    }
