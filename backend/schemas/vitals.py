from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class VitalsBase(BaseModel):
    type: str
    value: float
    unit: str
    recorded_at: datetime
    notes: Optional[str] = None

class VitalsCreate(VitalsBase):
    pass

class VitalsUpdate(VitalsBase):
    pass

class VitalsOut(VitalsBase):
    id: int
    class Config:
        orm_mode = True
