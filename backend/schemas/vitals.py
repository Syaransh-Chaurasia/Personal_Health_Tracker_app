from pydantic import BaseModel
from datetime import date
from typing import Optional

class VitalsCreate(BaseModel):
    date: date
    temperature: Optional[float] = None
    blood_pressure: Optional[str] = None
    heart_rate: Optional[int] = None

class VitalsUpdate(BaseModel):
    temperature: Optional[float] = None
    blood_pressure: Optional[str] = None
    heart_rate: Optional[int] = None

class VitalsOut(VitalsCreate):
    id: int

    class Config:
        orm_mode = True
