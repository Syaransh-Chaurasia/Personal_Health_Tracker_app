from sqlalchemy import Column, Integer, Float, Date, ForeignKey
from backend.database import Base

class Vitals(Base):
    __tablename__ = "vitals"
    id = Column(Integer, primary_key=True, index=True)
    date = Column(Date, nullable=False)
    temperature = Column(Float, nullable=True)
    blood_pressure = Column(String, nullable=True)
    heart_rate = Column(Integer, nullable=True)
    user_id = Column(Integer, ForeignKey('user.id'))
