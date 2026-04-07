"""LPShuffler is a simple application that allows you to shuffle your vinyl collection and discover new albums. It uses the Discogs API to access your collection and provides a random album each time you run it."""
from app.utils import logger
from app.creators.collection_creator import CollectionCreator


if __name__ == "__main__":
    collection_creator = CollectionCreator()
    coll = collection_creator.create_collection()
    random_album = coll.random
    logger.info(f"Random album:\n\
                {random_album.artist} - {random_album.title}\n\
                Format: {random_album.type}")
