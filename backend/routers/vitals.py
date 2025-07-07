from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from backend.database import SessionLocal
from backend.models.vitals import Vitals
from backend.schemas.vitals import VitalsCreate, VitalsOut, VitalsUpdate

router = APIRouter(prefix="/vitals", tags=["Vitals"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=VitalsOut)
def create_vital(vital: VitalsCreate, db: Session = Depends(get_db)):
    db_vital = Vitals(**vital.dict())
    db.add(db_vital)
    db.commit()
    db.refresh(db_vital)
    return db_vital

@router.get("/", response_model=list[VitalsOut])
def read_vitals(type: str = None, db: Session = Depends(get_db)):
    query = db.query(Vitals)
    if type:
        query = query.filter(Vitals.type == type)
    return query.all()

@router.put("/{vital_id}", response_model=VitalsOut)
def update_vital(vital_id: int, vital_update: VitalsUpdate, db: Session = Depends(get_db)):
    vital = db.query(Vitals).get(vital_id)
    if not vital:
        raise HTTPException(status_code=404, detail="Vital not found")
    for key, value in vital_update.dict(exclude_unset=True).items():
        setattr(vital, key, value)
    db.commit()
    db.refresh(vital)
    return vital

@router.delete("/{vital_id}")
def delete_vital(vital_id: int, db: Session = Depends(get_db)):
    vital = db.query(Vitals).get(vital_id)
    if not vital:
        raise HTTPException(status_code=404, detail="Vital not found")
    db.delete(vital)
    db.commit()
    return {"message": "Vital deleted"}
