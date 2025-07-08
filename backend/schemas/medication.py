from pydantic import BaseModel
from datetime import date
from typing import Optional

class MedicationCreate(BaseModel):
    name: str
    dosage: str
    start_date: date
    end_date: Optional[date] = None
    instructions: Optional[str] = None

class MedicationUpdate(BaseModel):
    name: Optional[str] = None
    dosage: Optional[str] = None
    start_date: Optional[date] = None
    end_date: Optional[date] = None
    instructions: Optional[str] = None

class MedicationOut(MedicationCreate):
    id: int

    class Config:
        orm_mode = True
