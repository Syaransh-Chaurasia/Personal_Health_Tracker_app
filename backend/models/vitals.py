from sqlalchemy import Column, Integer, String, Date, ForeignKey
from backend.database import Base

class Vitals(Base):
    __tablename__ = 'vitals'
    id = Column(Integer, primary_key=True, index=True)
    blood_pressure = Column(String, nullable=False)
    heart_rate = Column(String, nullable=False)
    temperature = Column(String, nullable=False)
    date = Column(Date, nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
