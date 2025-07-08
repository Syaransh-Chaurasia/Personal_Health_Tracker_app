from sqlalchemy import Column, Integer, String, Date, Text, ForeignKey
from backend.database import Base

class Medication(Base):
    __tablename__ = "medications"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    dosage = Column(String, nullable=False)
    start_date = Column(Date, nullable=False)
    end_date = Column(Date, nullable=True)
    instructions = Column(Text)
    user_id = Column(Integer, ForeignKey('user.id'))
