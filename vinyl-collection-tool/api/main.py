"""Main API entry point for the vinyl collection tool."""

from http import HTTPStatus

from fastapi import FastAPI
import os
from app.providers.discogs_provider import DiscogsProvider
from app.creators.collection_creator import CollectionCreator

app = FastAPI()

@app.on_event("startup")
async def startup_event():
    app.state.proxy = DiscogsProvider('LPShuffler/0.1', os.getenv("DISCOGS_TOKEN"))

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/favicon.ico")
def read_favicon():
    return HTTPStatus.NO_CONTENT

@app.get("/random")
def get_random_album():
    collection = None
    if collection is None:
        collection_creator = CollectionCreator(app.state.proxy)
        collection = collection_creator.create_collection()
    random_album = collection.random
    return {"album": random_album}