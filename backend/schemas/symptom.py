from pydantic import BaseModel
from datetime import date

class SymptomCreate(BaseModel):
    date: date
    symptom_type: str
    severity: str
    notes: str = ""

class SymptomUpdate(BaseModel):
    date: date | None = None
    symptom_type: str | None = None
    severity: str | None = None
    notes: str | None = None

class SymptomOut(SymptomCreate):
    id: int

    class Config:
        orm_mode = True
