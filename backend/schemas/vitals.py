from pydantic import BaseModel
from datetime import date

class VitalsCreate(BaseModel):
    blood_pressure: str
    heart_rate: str
    temperature: str
    date: date

class VitalsOut(VitalsCreate):
    id: int
    class Config:
        orm_mode = True
