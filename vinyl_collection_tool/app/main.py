"""LPShuffler is a simple application that allows you to shuffle your vinyl collection and discover new albums. It uses the Discogs API to access your collection and provides a random album each time you run it."""

import argparse

from app.utils import logger
from app.creators.collection_creator import CollectionCreator

subparser = argparse.ArgumentParser(description="vinyl collection shuffler")
subparser.add_argument(
    "-u",
    "--username",
    type=str,
    help="Your Discogs username to access your collection.",
)


if __name__ == "__main__":
    args = subparser.parse_args()
    collection_creator = CollectionCreator()
    coll = collection_creator.create_collection(args.username)
    random_album = coll.random
    logger.info(
        f"Random album:\n\
                {random_album.artist} - {random_album.title}\n\
                Format: {random_album.type}"
    )
