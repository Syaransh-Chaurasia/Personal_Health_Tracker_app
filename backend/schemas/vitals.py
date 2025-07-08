from pydantic import BaseModel
from datetime import date

class VitalsCreate(BaseModel):
    date: date
    temperature: float | None = None
    blood_pressure: str | None = None
    heart_rate: int | None = None

class VitalsUpdate(BaseModel):
    temperature: float | None = None
    blood_pressure: str | None = None
    heart_rate: int | None = None

class VitalsOut(VitalsCreate):
    id: int

    class Config:
        orm_mode = True
