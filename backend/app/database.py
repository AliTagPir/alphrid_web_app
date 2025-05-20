from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import os
from dotenv import load_dotenv

load_dotenv()

# Get the database URL from environment
DATABASE_URL = os.getenv("DATABASE_URL")

if not DATABASE_URL:
    raise RuntimeError("DATABASE_URL is not set in environment variables.")

# Create SQLalchemy engine
engine = create_engine(DATABASE_URL, echo=True)

# Create a configured session factory
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)

# Base class for declerative models
Base = declarative_base()

# Dependency function to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
