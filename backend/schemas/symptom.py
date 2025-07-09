from pydantic import BaseModel
from typing import Optional
from datetime import date

class SymptomCreate(BaseModel):
    date: date
    symptom_type: str
    severity: str
    notes: Optional[str] = None

class SymptomUpdate(BaseModel):
    date: Optional[date] = None
    symptom_type: Optional[str] = None
    severity: Optional[str] = None
    notes: Optional[str] = None

class SymptomOut(SymptomCreate):
    id: int

    class Config:
        from_attributes = True
