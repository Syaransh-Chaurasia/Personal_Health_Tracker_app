from pydantic import BaseModel
from datetime import date

class MedicationCreate(BaseModel):
    name: str
    dosage: str
    start_date: date
    end_date: date | None = None
    instructions: str = ""

class MedicationUpdate(BaseModel):
    name: str | None = None
    dosage: str | None = None
    start_date: date | None = None
    end_date: date | None = None
    instructions: str | None = None

class MedicationOut(MedicationCreate):
    id: int

    class Config:
        orm_mode = True
