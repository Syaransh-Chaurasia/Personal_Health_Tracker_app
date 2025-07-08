from pydantic import BaseModel
from datetime import date
from typing import Optional

class SymptomCreate(BaseModel):
    date: date
    symptom_type: str
    severity: str
    notes: Optional[str] = ""

class SymptomUpdate(BaseModel):
    date: Optional[date] = None
    symptom_type: Optional[str] = None
    severity: Optional[str] = None
    notes: Optional[str] = None

class SymptomOut(SymptomCreate):
    id: int

    class Config:
        orm_mode = True  # Keep this, works fine in both Pydantic V1 and V2
