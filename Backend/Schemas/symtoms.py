from pydantic import BaseModel
from datetime import date

class SymptomBase(BaseModel):
    symptom_type: str
    severity: int
    notes: str = ""
    date: date

class SymptomCreate(SymptomBase):
    pass

class SymptomUpdate(SymptomBase):
    pass

class SymptomOut(SymptomBase):
    id: int

    class Config:
        orm_mode = True
