from pydantic import BaseModel
from typing import Optional
from datetime import date

class MedicationCreate(BaseModel):
    name: str
    dosage: str
    frequency: str
    time_slots: str
    start_date: date
    end_date: date

class MedicationUpdate(BaseModel):
    name: Optional[str] = None
    dosage: Optional[str] = None
    frequency: Optional[str] = None
    time_slots: Optional[str] = None
    start_date: Optional[date] = None
    end_date: Optional[date] = None
    taken: Optional[bool] = None

class MedicationOut(MedicationCreate):
    id: int
    taken: Optional[bool] = None

    class Config:
        from_attributes = True
