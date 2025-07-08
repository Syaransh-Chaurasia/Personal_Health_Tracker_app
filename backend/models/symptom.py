from sqlalchemy import Column, Integer, String, Date, Text, ForeignKey
from backend.database import Base

class Symptom(Base):
    __tablename__ = "symptoms"
    id = Column(Integer, primary_key=True, index=True)
    date = Column(Date, nullable=False)
    symptom_type = Column(String, nullable=False)
    severity = Column(String, nullable=False)
    notes = Column(Text, nullable=True)
    user_id = Column(Integer, ForeignKey('user.id'))
