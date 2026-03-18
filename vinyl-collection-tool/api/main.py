"""Main API entry point for the vinyl collection tool."""

from fastapi import FastAPI
import os
from app.providers.discogs_provider import DiscogsProvider
from app.creators.collection_creator import DiscogsCollectionCreator

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/random")
def get_random_album():
    proxy = DiscogsProvider('LPShuffler/0.1', os.getenv("DISCOGS_TOKEN"))
    collection_creator = DiscogsCollectionCreator(proxy)
    coll = collection_creator.create_collection()
    random_album = coll.random
    return {"album": random_album}