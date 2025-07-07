from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from backend.database import SessionLocal
from backend.models.symptom import Symptom
from backend.schemas.symptom import SymptomCreate, SymptomOut, SymptomUpdate

router = APIRouter(prefix="/symptoms", tags=["Symptoms"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=SymptomOut)
def create_symptom(sym: SymptomCreate, db: Session = Depends(get_db)):
    db_sym = Symptom(**sym.dict())
    db.add(db_sym)
    db.commit()
    db.refresh(db_sym)
    return db_sym

@router.get("/", response_model=list[SymptomOut])
def read_symptoms(symptom_type: str = None, db: Session = Depends(get_db)):
    query = db.query(Symptom)
    if symptom_type:
        query = query.filter(Symptom.symptom_type == symptom_type)
    return query.all()

@router.put("/{symptom_id}", response_model=SymptomOut)
def update_symptom(symptom_id: int, sym_update: SymptomUpdate, db: Session = Depends(get_db)):
    sym = db.query(Symptom).get(symptom_id)
    if not sym:
        raise HTTPException(status_code=404, detail="Symptom not found")
    for key, value in sym_update.dict(exclude_unset=True).items():
        setattr(sym, key, value)
    db.commit()
    db.refresh(sym)
    return sym

@router.delete("/{symptom_id}")
def delete_symptom(symptom_id: int, db: Session = Depends(get_db)):
    sym = db.query(Symptom).get(symptom_id)
    if not sym:
        raise HTTPException(status_code=404, detail="Symptom not found")
    db.delete(sym)
    db.commit()
    return {"message": "Symptom deleted"}
