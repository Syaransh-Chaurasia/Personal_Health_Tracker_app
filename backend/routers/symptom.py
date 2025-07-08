from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from backend.models.symptom import Symptom
from backend.schemas.symptom import SymptomCreate, SymptomUpdate, SymptomOut
from backend.auth_helpers import get_db, get_current_user
from backend.models.user import User

router = APIRouter(prefix="/symptoms", tags=["Symptoms"])

@router.post("/", response_model=SymptomOut)
def create(sym: SymptomCreate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    item = Symptom(**sym.dict(), user_id=current_user.id)
    db.add(item)
    db.commit()
    db.refresh(item)
    return item

@router.get("/", response_model=list[SymptomOut])
def get_all(db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return db.query(Symptom).filter(Symptom.user_id == current_user.id).all()

@router.put("/{symptom_id}", response_model=SymptomOut)
def update(symptom_id: int, sym: SymptomUpdate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    item = db.query(Symptom).filter(Symptom.id == symptom_id, Symptom.user_id == current_user.id).first()
    if not item:
        raise HTTPException(status_code=404, detail="Not found")
    for key, value in sym.dict(exclude_unset=True).items():
        setattr(item, key, value)
    db.commit()
    db.refresh(item)
    return item

@router.delete("/{symptom_id}")
def delete(symptom_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    item = db.query(Symptom).filter(Symptom.id == symptom_id, Symptom.user_id == current_user.id).first()
    if not item:
        raise HTTPException(status_code=404, detail="Not found")
    db.delete(item)
    db.commit()
    return {"message": "Deleted"}
