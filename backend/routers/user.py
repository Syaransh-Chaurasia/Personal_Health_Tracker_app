from fastapi import APIRouter, Depends, HTTPException, BackgroundTasks
from sqlalchemy.orm import Session
from backend.dependencies import get_db
from backend.models.user import User
from backend.schemas.user import UserCreate, UserOut
from backend.auth import get_password_hash, verify_password, create_access_token
from backend.utils.email import send_welcome_email

router = APIRouter(prefix="/user", tags=["User"])

@router.post("/register", response_model=UserOut)
def register(user: UserCreate, background_tasks: BackgroundTasks, db: Session = Depends(get_db)):
    existing_user = db.query(User).filter_by(email=user.email).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")

    hashed_password = get_password_hash(user.password)
    new_user = User(email=user.email, password=hashed_password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    background_tasks.add_task(send_welcome_email, user.email)

    return new_user

@router.post("/login")
def login(user: UserCreate, db: Session = Depends(get_db)):
    db_user = db.query(User).filter_by(email=user.email).first()
    if not db_user or not verify_password(user.password, db_user.password):
        raise HTTPException(status_code=401, detail="Invalid email or password")
    token = create_access_token({"sub": db_user.email})
    return {
        "access_token": token,
        "token_type": "bearer",
        "user_id": db_user.id
    }
