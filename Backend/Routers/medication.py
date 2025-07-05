from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal
from models.medication import Medication
from schemas.medication import MedicationCreate, MedicationUpdate, MedicationOut

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
def get_medications(db: Session = Depends(get_db)):
    return db.query(Medication).all()

@router.put("/{medication_id}", response_model=MedicationOut)
def update_medication(medication_id: int, med_update: MedicationUpdate, db: Session = Depends(get_db)):
    med = db.query(Medication).get(medication_id)
    if not med:
        raise HTTPException(status_code=404, detail="Medication not found")
    for key, value in med_update.dict().items():
        setattr(med, key, value)
    db.commit()
    db.refresh(med)
    return med

@router.delete("/{medication_id}")
def delete_medication(medication_id: int, db: Session = Depends(get_db)):
    med = db.query(Medication).get(medication_id)
    if not med:
        raise HTTPException(status_code=404, detail="Medication not found")
    db.delete(med)
    db.commit()
    return {"message": "Medication deleted"}

@router.patch("/{medication_id}/toggle-taken", response_model=MedicationOut)
def toggle_taken(medication_id: int, db: Session = Depends(get_db)):
    med = db.query(Medication).get(medication_id)
    if not med:
        raise HTTPException(status_code=404, detail="Medication not found")
    med.taken = not med.taken
    db.commit()
    db.refresh(med)
    return med
