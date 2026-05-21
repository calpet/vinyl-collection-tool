# """API controller for sessions."""

from fastapi import APIRouter
from app.sessions.session import MusicSession
from api.models.sessions import CreateSessionRequest


router = APIRouter(prefix="/sessions", tags=["sessions"])

@router.post("/create", status_code=201)
def create_session(request: CreateSessionRequest):
    """Creates a session for the given username.
    
    :param request: The request containing the username."""
    music_session = MusicSession(request.username)
    return {"message": f"Session created for user {request.username}."}

@router.get("/random-album")
def get_random_album(request: CreateSessionRequest):
    """Returns a random album from the user's collection.
    
    :param request: The request containing the username."""
    music_session = MusicSession(request.username)
    album = music_session.random_album()
    return {"artist": album.artist, "title": album.title, "type": album.type.value, "image": album.image}
