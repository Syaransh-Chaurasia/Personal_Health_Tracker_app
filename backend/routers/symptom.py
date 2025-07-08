from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from backend.dependencies import get_db
from backend.auth import get_current_user
from backend.models.symptom import Symptom
from backend.schemas.symptom import SymptomCreate, SymptomOut, SymptomUpdate

router = APIRouter(prefix="/symptoms", tags=["Symptoms"])

@router.post("/", response_model=SymptomOut)
def create_symptom(sym: SymptomCreate, db: Session = Depends(get_db), user=Depends(get_current_user)):
    db_sym = Symptom(**sym.dict(), user_id=user.id)
    db.add(db_sym)
    db.commit()
    db.refresh(db_sym)
    return db_sym

@router.get("/", response_model=list[SymptomOut])
def read_symptoms(db: Session = Depends(get_db), user=Depends(get_current_user)):
    return db.query(Symptom).filter(Symptom.user_id == user.id).all()

@router.put("/{symptom_id}", response_model=SymptomOut)
def update_symptom(symptom_id: int, sym_update: SymptomUpdate, db: Session = Depends(get_db), user=Depends(get_current_user)):
    sym = db.query(Symptom).filter(Symptom.id == symptom_id, Symptom.user_id == user.id).first()
    if not sym:
        raise HTTPException(status_code=404, detail="Symptom not found")
    for key, value in sym_update.dict(exclude_unset=True).items():
        setattr(sym, key, value)
    db.commit()
    db.refresh(sym)
    return sym

@router.delete("/{symptom_id}")
def delete_symptom(symptom_id: int, db: Session = Depends(get_db), user=Depends(get_current_user)):
    sym = db.query(Symptom).filter(Symptom.id == symptom_id, Symptom.user_id == user.id).first()
    if not sym:
        raise HTTPException(status_code=404, detail="Symptom not found")
    db.delete(sym)
    db.commit()
    return {"detail": "Symptom deleted"}
