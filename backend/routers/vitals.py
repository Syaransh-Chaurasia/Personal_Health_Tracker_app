from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from backend.models.vitals import Vitals
from backend.schemas.vitals import VitalsCreate, VitalsUpdate, VitalsOut
from backend.auth_helpers import get_db, get_current_user
from backend.models.user import User

router = APIRouter(prefix="/vitals", tags=["Vitals"])

@router.post("/", response_model=VitalsOut)
def create_vitals(vitals: VitalsCreate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    new_vitals = Vitals(**vitals.dict(), user_id=current_user.id)
    db.add(new_vitals)
    db.commit()
    db.refresh(new_vitals)
    return new_vitals

@router.get("/", response_model=list[VitalsOut])
def read_vitals(db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    vitals = db.query(Vitals).filter(Vitals.user_id == current_user.id).all()
    return vitals

@router.put("/{vitals_id}", response_model=VitalsOut)
def update_vitals(vitals_id: int, vitals_update: VitalsUpdate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    vitals = db.query(Vitals).filter(Vitals.id == vitals_id, Vitals.user_id == current_user.id).first()
    if not vitals:
        raise HTTPException(status_code=404, detail="Vitals record not found")
    for key, value in vitals_update.dict(exclude_unset=True).items():
        setattr(vitals, key, value)
    db.commit()
    db.refresh(vitals)
    return vitals

@router.delete("/{vitals_id}")
def delete_vitals(vitals_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    vitals = db.query(Vitals).filter(Vitals.id == vitals_id, Vitals.user_id == current_user.id).first()
    if not vitals:
        raise HTTPException(status_code=404, detail="Vitals record not found")
    db.delete(vitals)
    db.commit()
    return {"message": "Vitals record deleted"}
