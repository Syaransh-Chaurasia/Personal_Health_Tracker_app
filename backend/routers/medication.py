from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from backend.schemas import medication as schemas
from backend.models.medication import Medication
from backend.models.user import User
from backend.database import get_db
from backend.auth import get_current_user

router = APIRouter(prefix="/medications", tags=["Medications"])

@router.get("/", response_model=list[schemas.MedicationOut])
def get_medications(db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    meds = db.query(Medication).filter(Medication.user_id == current_user.id).all()
    return meds

@router.post("/", response_model=schemas.MedicationOut)
def create_medication(medication: schemas.MedicationCreate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    new_med = Medication(**medication.dict(), user_id=current_user.id, taken=False)  # ✅ Ensured default
    db.add(new_med)
    db.commit()
    db.refresh(new_med)
    return new_med

@router.delete("/{med_id}")
def delete_medication(med_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    med = db.query(Medication).filter(Medication.id == med_id, Medication.user_id == current_user.id).first()
    if not med:
        raise HTTPException(status_code=404, detail="Medication not found")
    db.delete(med)
    db.commit()
    return {"detail": "Deleted"}

@router.put("/{med_id}", response_model=schemas.MedicationOut)
def update_medication_status(med_id: int, medication: schemas.MedicationUpdate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    med = db.query(Medication).filter(Medication.id == med_id, Medication.user_id == current_user.id).first()
    if not med:
        raise HTTPException(status_code=404, detail="Medication not found")
    med.taken = medication.taken
    db.commit()
    db.refresh(med)
    return med
