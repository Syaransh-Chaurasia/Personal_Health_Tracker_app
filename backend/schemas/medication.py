from pydantic import BaseModel
from datetime import date

class MedicationCreate(BaseModel):
    name: str
    dosage: str
    frequency: str
    time_slots: str
    start_date: date
    end_date: date

class MedicationOut(MedicationCreate):
    id: int
    class Config:
        orm_mode = True
