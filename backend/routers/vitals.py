from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from backend.dependencies import get_db
from backend.auth import get_current_user
from backend.models.vitals import Vitals
from backend.schemas.vitals import VitalsCreate, VitalsOut, VitalsUpdate

router = APIRouter(prefix="/vitals", tags=["Vitals"])

@router.post("/", response_model=VitalsOut)
def create_vitals(vitals: VitalsCreate, db: Session = Depends(get_db), user=Depends(get_current_user)):
    db_vitals = Vitals(**vitals.dict(), user_id=user.id)
    db.add(db_vitals)
    db.commit()
    db.refresh(db_vitals)
    return db_vitals

@router.get("/", response_model=list[VitalsOut])
def read_vitals(db: Session = Depends(get_db), user=Depends(get_current_user)):
    return db.query(Vitals).filter(Vitals.user_id == user.id).all()

@router.put("/{vitals_id}", response_model=VitalsOut)
def update_vitals(vitals_id: int, vitals_update: VitalsUpdate, db: Session = Depends(get_db), user=Depends(get_current_user)):
    vitals = db.query(Vitals).filter(Vitals.id == vitals_id, Vitals.user_id == user.id).first()
    if not vitals:
        raise HTTPException(status_code=404, detail="Vitals not found")
    for key, value in vitals_update.dict(exclude_unset=True).items():
        setattr(vitals, key, value)
    db.commit()
    db.refresh(vitals)
    return vitals

@router.delete("/{vitals_id}")
def delete_vitals(vitals_id: int, db: Session = Depends(get_db), user=Depends(get_current_user)):
    vitals = db.query(Vitals).filter(Vitals.id == vitals_id, Vitals.user_id == user.id).first()
    if not vitals:
        raise HTTPException(status_code=404, detail="Vitals not found")
    db.delete(vitals)
    db.commit()
    return {"detail": "Vitals deleted"}
