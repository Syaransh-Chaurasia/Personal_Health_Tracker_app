from sqlalchemy import Column, Integer, String, DateTime
from database import Base

class Vitals(Base):
    __tablename__ = "vitals"

    id = Column(Integer, primary_key=True, index=True)
    type = Column(String, nullable=False)
    value = Column(String, nullable=False)
    unit = Column(String, nullable=False)
    recorded_at = Column(DateTime, nullable=False)
    notes = Column(String)
