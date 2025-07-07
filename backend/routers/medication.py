from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from backend.database import SessionLocal
from backend.models.medication import Medication
from backend.schemas.medication import MedicationCreate, MedicationOut, MedicationUpdate

router = APIRouter(prefix="/medications", tags=["Medications"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=MedicationOut)
def create_medication(med: MedicationCreate, db: Session = Depends(get_db)):
    db_med = Medication(**med.dict())
    db.add(db_med)
    db.commit()
    db.refresh(db_med)
    return db_med

@router.get("/", response_model=list[MedicationOut])
def read_medications(db: Session = Depends(get_db)):
    return db.query(Medication).all()

@router.put("/{med_id}", response_model=MedicationOut)
def update_medication(med_id: int, med: MedicationUpdate, db: Session = Depends(get_db)):
    db_med = db.query(Medication).get(med_id)
    if not db_med:
        raise HTTPException(status_code=404, detail="Medication not found")
    for key, value in med.dict(exclude_unset=True).items():
        setattr(db_med, key, value)
    db.commit()
    db.refresh(db_med)
    return db_med

@router.delete("/{med_id}")
def delete_medication(med_id: int, db: Session = Depends(get_db)):
    med = db.query(Medication).get(med_id)
    if not med:
        raise HTTPException(status_code=404, detail="Medication not found")
    db.delete(med)
    db.commit()
    return {"message": "Medication deleted"}

@router.patch("/{med_id}/toggle-taken")
def toggle_medication(med_id: int, db: Session = Depends(get_db)):
    med = db.query(Medication).get(med_id)
    if not med:
        raise HTTPException(status_code=404, detail="Medication not found")
    med.taken = not med.taken
    db.commit()
    db.refresh(med)
    return med
