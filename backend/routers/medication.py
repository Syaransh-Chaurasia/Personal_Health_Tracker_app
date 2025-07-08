from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from backend.dependencies import get_db
from backend.auth import get_current_user
from backend.models.medication import Medication
from backend.schemas.medication import MedicationCreate, MedicationOut

router = APIRouter(prefix="/medications", tags=["Medications"])

@router.post("/", response_model=MedicationOut)
def create_med(med: MedicationCreate, db: Session = Depends(get_db), user=Depends(get_current_user)):
    db_med = Medication(**med.dict(), user_id=user.id)
    db.add(db_med)
    db.commit()
    db.refresh(db_med)
    return db_med

@router.get("/", response_model=list[MedicationOut])
def get_meds(db: Session = Depends(get_db), user=Depends(get_current_user)):
    return db.query(Medication).filter(Medication.user_id == user.id).all()

@router.delete("/{id}")
def delete_med(id: int, db: Session = Depends(get_db), user=Depends(get_current_user)):
    med = db.query(Medication).filter(Medication.id == id, Medication.user_id == user.id).first()
    if not med:
        raise HTTPException(status_code=404, detail="Medication not found")
    db.delete(med)
    db.commit()
    return {"detail": "Medication deleted"}
