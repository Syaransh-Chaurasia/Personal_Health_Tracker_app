from pydantic import BaseModel
from typing import Optional

class MedicationBase(BaseModel):
    name: Optional[str] = None
    dosage: Optional[str] = None
    frequency: Optional[str] = None
    time_slots: Optional[str] = None
    start_date: Optional[str] = None
    end_date: Optional[str] = None
    taken: Optional[bool] = False  # ✅ Include this

class MedicationCreate(MedicationBase):
    name: str
    dosage: str
    frequency: str
    time_slots: str
    start_date: str
    end_date: str

class MedicationUpdate(BaseModel):
    taken: bool  # ✅ Only used for toggling status

class MedicationOut(MedicationBase):
    id: int
    user_id: int

    class Config:
        from_attributes = True  # ✅ Required for FastAPI v2+
