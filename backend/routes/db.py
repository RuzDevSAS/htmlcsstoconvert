from sqlmodel import create_engine, Session
from pydantic_settings import BaseSettings
import os
from dotenv import load_dotenv

load_dotenv()

class Settings(BaseSettings):
    DATABASE_URL: str = os.getenv("DATABASE_URL", "sqlite:///./backend.db")

settings = Settings()

# Ensure we use the correct driver for PostgreSQL if not specified
database_url = settings.DATABASE_URL
if database_url and database_url.startswith("postgres://"):
    database_url = database_url.replace("postgres://", "postgresql://", 1)

engine = create_engine(database_url, echo=True)

def get_session():
    with Session(engine) as session:
        yield session
