from pydantic import BaseModel
from typing import Optional
from datetime import date

class VitalsCreate(BaseModel):
    blood_pressure: str
    heart_rate: str
    temperature: str
    date: date

class VitalsUpdate(BaseModel):
    blood_pressure: Optional[str] = None
    heart_rate: Optional[str] = None
    temperature: Optional[str] = None
    date: Optional[date] = None

class VitalsOut(VitalsCreate):
    id: int

    class Config:
        from_attributes = True
