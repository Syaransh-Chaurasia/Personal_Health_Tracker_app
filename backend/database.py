import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = os.getenv('DATABASE_URL')  # This reads from environment variables

# Fallback if DATABASE_URL not set (used by Alembic)
if not DATABASE_URL:
    from alembic.config import Config
    alembic_cfg = Config("alembic.ini")
    DATABASE_URL = alembic_cfg.get_main_option("sqlalchemy.url")

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)
Base = declarative_base()
