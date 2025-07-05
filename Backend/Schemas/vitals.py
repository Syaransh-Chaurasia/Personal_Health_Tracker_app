from pydantic import BaseModel
from datetime import datetime

class VitalsBase(BaseModel):
    type: str
    value: str
    unit: str
    recorded_at: datetime
    notes: str = ""

class VitalsCreate(VitalsBase):
    pass

class VitalsUpdate(VitalsBase):
    pass

class VitalsOut(VitalsBase):
    id: int

    class Config:
        orm_mode = True
