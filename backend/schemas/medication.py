from pydantic import BaseModel
from datetime import date

class MedicationBase(BaseModel):
    name: str
    dosage: str
    frequency: str
    time_slots: str
    start_date: date
    end_date: date

class MedicationCreate(MedicationBase):
    pass

class MedicationUpdate(BaseModel):
    taken: bool

class MedicationOut(MedicationBase):
    id: int
    taken: bool

    class Config:
        from_attributes = True  # Pydantic v2
