"""API controller for albums."""

import os
from fastapi import APIRouter
from app.providers.discogs_provider import DiscogsProvider
from app.sessions.session import MusicSession

router = APIRouter(prefix="/collections", tags=["collections"])

_proxy = DiscogsProvider(agent="LPShuffler/1.0", api_token=os.getenv("DISCOGS_TOKEN"))
_music_session = MusicSession()

# Routes
@router.get("/random")
def get_random_album():
    """Returns a random album from the user's collection."""
    return _music_session.random_album()