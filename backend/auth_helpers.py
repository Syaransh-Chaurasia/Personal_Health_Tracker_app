from fastapi import Depends, HTTPException, Header
from sqlalchemy.orm import Session
from jose import jwt
from .auth import SECRET_KEY, ALGORITHM
from backend.database import SessionLocal
from backend.models.user import User

# Dependency: DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Dependency: Get current user from JWT
def get_current_user(authorization: str = Header(...), db: Session = Depends(get_db)):
    credentials_exception = HTTPException(status_code=401, detail="Invalid or missing token")
    if not authorization.startswith("Bearer "):
        raise credentials_exception

    token = authorization.split(" ")[1]

    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        email = payload.get("sub")
        if email is None:
            raise credentials_exception
        user = db.query(User).filter(User.email == email).first()
        if user is None:
            raise credentials_exception
        return user
    except:
        raise credentials_exception
