"""Database connection boilerplate for SQLModel."""

import os
from pathlib import Path
from sqlmodel import SQLModel, create_engine, Session

from app.db import entities  # noqa: F401 - Ensure all models are imported for table creation

BASE_DIR = Path(__file__).resolve().parents[2]
DEFAULT_DATABASE_URL = f"sqlite:///{BASE_DIR / 'vinyl_collection.db'}"
DATABASE_URL = os.getenv("DATABASE_URL", DEFAULT_DATABASE_URL)
engine = create_engine(DATABASE_URL, echo=True)


def get_session():
    return Session(engine)


def init_db():
    SQLModel.metadata.create_all(engine)
