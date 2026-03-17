"""LPShuffler is a simple application that allows you to shuffle your vinyl collection and discover new albums. It uses the Discogs API to access your collection and provides a random album each time you run it."""
import os

from app.src.utils import logger
from app.src.creators.collection_creator import DiscogsCollectionCreator
from app.src.providers.discogs_provider import DiscogsProvider


if __name__ == "__main__":
    proxy = DiscogsProvider('LPShuffler/0.1', os.getenv("DISCOGS_TOKEN"))
    collection_creator = DiscogsCollectionCreator(proxy)
    coll = collection_creator.create_collection()
    random_album = coll.random
    logger.info(f"Random album:\n\
                {random_album.artist} - {random_album.title}\n\
                Format: {random_album.format}")
