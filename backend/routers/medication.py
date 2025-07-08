from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from backend.models.medication import Medication
from backend.schemas.medication import MedicationCreate, MedicationUpdate, MedicationOut
from backend.auth_helpers import get_db, get_current_user
from backend.models.user import User

router = APIRouter(prefix="/medications", tags=["Medications"])

@router.post("/", response_model=MedicationOut)
def create_medication(med: MedicationCreate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    new_med = Medication(**med.dict(), user_id=current_user.id)
    db.add(new_med)
    db.commit()
    db.refresh(new_med)
    return new_med

@router.get("/", response_model=list[MedicationOut])
def read_medications(db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    meds = db.query(Medication).filter(Medication.user_id == current_user.id).all()
    return meds

@router.put("/{medication_id}", response_model=MedicationOut)
def update_medication(medication_id: int, med_update: MedicationUpdate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    med = db.query(Medication).filter(Medication.id == medication_id, Medication.user_id == current_user.id).first()
    if not med:
        raise HTTPException(status_code=404, detail="Medication not found")
    for key, value in med_update.dict(exclude_unset=True).items():
        setattr(med, key, value)
    db.commit()
    db.refresh(med)
    return med

@router.delete("/{medication_id}")
def delete_medication(medication_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    med = db.query(Medication).filter(Medication.id == medication_id, Medication.user_id == current_user.id).first()
    if not med:
        raise HTTPException(status_code=404, detail="Medication not found")
    db.delete(med)
    db.commit()
    return {"message": "Medication deleted"}
