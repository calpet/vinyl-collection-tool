"""API controller for albums."""

import os
from fastapi import APIRouter
from app.providers.discogs_provider import DiscogsProvider
from app.creators.collection_creator import CollectionCreator

router = APIRouter(prefix="/collection", tags=["collection"])

_discogs_provider = DiscogsProvider(agent="LPShuffler/1.0", api_token=os.getenv("DISCOGS_TOKEN"))
_collection_creator = CollectionCreator(_discogs_provider)
_collection = _collection_creator.create_collection()

# Routes
@router.get("/random")
def get_random_album():
    """Returns a random album from the user's collection."""
    return _collection.random