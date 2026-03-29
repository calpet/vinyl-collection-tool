"""Class for handling sessions."""

from app.models.collection import Collection
from app.creators.collection_creator import CollectionCreator
from app.models.album import Album
from app.utils import logger


class MusicSession:
    """Class for handling music sessions."""

    def __init__(self) -> None:
        """Initializes the MusicSession."""
        self._collection: Collection = CollectionCreator().create_collection()
        self._played_albums: set[Album] = set()
        
    def get_random_album(self) -> Album:
        """Gets a random album from the collection, moves it to the played albums, and returns it."""
        album = self._collection.random
        if album in self._played_albums:
            logger.info(f"Album {album.title} has already been played. Selecting another album.")
            return self.get_random_album()
        
        self._played_albums.add(album)
        return album
     