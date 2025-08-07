from fastapi import APIRouter, Depends, HTTPException, status, BackgroundTasks
from sqlalchemy.orm import Session
from pydantic import BaseModel, EmailStr
from datetime import timedelta
import os

from backend.dependencies import get_db
from backend.models.user import User
from backend.auth import get_password_hash, verify_password, create_access_token
from backend.email_utils import send_welcome_email  # Updated import

router = APIRouter(prefix="/user", tags=["User"])

class RegisterRequest(BaseModel):
    name: str
    email: EmailStr
    password: str

class LoginRequest(BaseModel):
    email: EmailStr
    password: str

@router.post("/register", status_code=status.HTTP_201_CREATED)
async def register_user(
        request: RegisterRequest,
        background_tasks: BackgroundTasks,
        db: Session = Depends(get_db)
):
    existing_user = db.query(User).filter(User.email == request.email).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")

    hashed_password = get_password_hash(request.password)
    new_user = User(name=request.name, email=request.email, password=hashed_password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    # Add email sending as background async task
    background_tasks.add_task(send_welcome_email, new_user.email, new_user.name)

    return {"message": "User registered successfully"}

@router.post("/login")
def login_user(request: LoginRequest, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.email == request.email).first()
    if not user or not verify_password(request.password, user.password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")

    token_data = {"sub": user.email}
    access_token_expires = timedelta(minutes=int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", 60)))
    access_token = create_access_token(data=token_data, expires_delta=access_token_expires)

    return {"access_token": access_token, "token_type": "bearer"}
