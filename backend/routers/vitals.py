from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from backend.dependencies import get_db
from backend.auth_helpers import get_current_user
from backend.models.vitals import Vitals
from backend.schemas.vitals import VitalsCreate, VitalsUpdate, VitalsOut

router = APIRouter(prefix="/vitals", tags=["Vitals"])

@router.post("/", response_model=VitalsOut)
def create_vitals(vital: VitalsCreate, db: Session = Depends(get_db), user=Depends(get_current_user)):
    db_vital = Vitals(**vital.dict(), user_id=user.id)
    db.add(db_vital)
    db.commit()
    db.refresh(db_vital)
    return db_vital

@router.get("/", response_model=list[VitalsOut])
def read_vitals(db: Session = Depends(get_db), user=Depends(get_current_user)):
    return db.query(Vitals).filter(Vitals.user_id == user.id).all()

@router.put("/{vitals_id}", response_model=VitalsOut)
def update_vitals(vitals_id: int, vitals_update: VitalsUpdate, db: Session = Depends(get_db), user=Depends(get_current_user)):
    vit = db.query(Vitals).filter(Vitals.id == vitals_id, Vitals.user_id == user.id).first()
    if not vit:
        raise HTTPException(status_code=404, detail="Vitals not found")
    for key, value in vitals_update.dict(exclude_unset=True).items():
        setattr(vit, key, value)
    db.commit()
    db.refresh(vit)
    return vit

@router.delete("/{vitals_id}")
def delete_vitals(vitals_id: int, db: Session = Depends(get_db), user=Depends(get_current_user)):
    vit = db.query(Vitals).filter(Vitals.id == vitals_id, Vitals.user_id == user.id).first()
    if not vit:
        raise HTTPException(status_code=404, detail="Vitals not found")
    db.delete(vit)
    db.commit()
    return {"message": "Vitals deleted"}
