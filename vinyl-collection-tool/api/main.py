"""Main API entry point for the vinyl collection tool."""

from http import HTTPStatus

from fastapi import FastAPI
import os
from app.providers.discogs_provider import DiscogsProvider
from app.creators.collection_creator import DiscogsCollectionCreator

app = FastAPI()

@app.on_event("startup")
async def startup_event():
    proxy = DiscogsProvider('LPShuffler/0.1', os.getenv("DISCOGS_TOKEN"))
    collection_creator = DiscogsCollectionCreator(proxy)
    app.state.collection = collection_creator.create_collection()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/favicon.ico")
def read_favicon():
    return HTTPStatus.NO_CONTENT

@app.get("/random")
def get_random_album():
    random_album = app.state.collection.random
    return {"album": random_album}