"""API controller for albums."""

import os
from fastapi import APIRouter
from app.providers.discogs_provider import DiscogsProvider
from app.sessions.session import PlaybackOrchestrator

router = APIRouter(prefix="/collections", tags=["collections"])

_proxy = DiscogsProvider(agent="LPShuffler/1.0", api_token=os.getenv("DISCOGS_TOKEN"))
_playback_session = PlaybackOrchestrator()

# Routes
@router.get("/random")
def get_random_album():
    """Returns a random album from the user's collection."""
    return _playback_session.random_album()