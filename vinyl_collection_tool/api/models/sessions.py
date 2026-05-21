"""Models for sessions."""

from pydantic import BaseModel


class CreateSessionRequest(BaseModel):
    """Request model for creating a session."""

    username: str