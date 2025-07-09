from pydantic import BaseModel
from typing import Optional
from datetime import date

class MedicationBase(BaseModel):
    name: str
    dosage: str
    frequency: str
    time_slots: str
    start_date: date
    end_date: date
    taken: Optional[bool] = False

class MedicationCreate(MedicationBase):
    pass

class MedicationUpdate(MedicationBase):
    pass

class MedicationOut(MedicationBase):
    id: int

    class Config:
        from_attributes = True  # Use this for Pydantic v2+
