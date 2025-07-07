from pydantic import BaseModel
from datetime import date
from typing import Optional

class SymptomBase(BaseModel):
    date: date
    symptom_type: str
    severity: str
    notes: Optional[str] = None

class SymptomCreate(SymptomBase):
    pass

class SymptomUpdate(SymptomBase):
    pass

class SymptomOut(SymptomBase):
    id: int
    class Config:
        orm_mode = True
