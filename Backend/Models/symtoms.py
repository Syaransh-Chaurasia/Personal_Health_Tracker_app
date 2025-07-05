from sqlalchemy import Column, Integer, String, Date
from database import Base

class Symptom(Base):
    __tablename__ = "symptoms"

    id = Column(Integer, primary_key=True, index=True)
    symptom_type = Column(String, nullable=False)
    severity = Column(Integer, nullable=False)
    notes = Column(String)
    date = Column(Date, nullable=False)
