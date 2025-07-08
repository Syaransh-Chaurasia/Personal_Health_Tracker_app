from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Replace this with your actual Render Postgres URL
DATABASE_URL = "postgresql://healthtracker_db_ro1m_user:FwEWHi9HeuhhWoDBHd3dhccgXKYaWJQA@dpg-d1mlgnu3jp1c73dqpqa0-a.frankfurt-postgres.render.com/healthtracker_db_ro1m"

# Create the SQLAlchemy engine
engine = create_engine(DATABASE_URL)

# Create a base class
Base = declarative_base()

# Example table/model
class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)

# Create tables (run this only once, or use Alembic for migrations)
Base.metadata.create_all(bind=engine)

# Create session
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Example of using session
def get_users():
    db = SessionLocal()
    try:
        users = db.query(User).all()
        return users
    finally:
        db.close()
