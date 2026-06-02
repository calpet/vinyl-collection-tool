"""Database connection boilerplate for SQLModel."""

from sqlmodel import SQLModel, create_engine, Session

from app.db import entities  # noqa: F401 - Ensure all models are imported for table creation

DATABASE_URL = "sqlite:///./vinyl_collection.db"  # Change to your preferred DB
engine = create_engine(DATABASE_URL, echo=True)


def get_session():
    return Session(engine)


def init_db():
    SQLModel.metadata.create_all(engine)
