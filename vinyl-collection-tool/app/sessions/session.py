"""Class for handling sessions."""
from app.models.collection import Collection
from app.creators.collection_creator import CollectionCreator
from app.models.album import Album
from app.utils import logger
from app.strategies.random_picker import RandomAlbum


class MusicSession:
    """Class for handling music sessions."""

    def __init__(self) -> None:
        """Initializes the MusicSession."""
        self._collection: Collection = CollectionCreator().create_collection()
        self._played_albums: set[Album] = set()
        
    def random_album(self) -> Album:
        """Returns a random album from the collection."""
        rand = RandomAlbum(self._collection)
        album = rand.pick_album()
        if album in self._played_albums:
            logger.info(f"Album: {album.title} by {album.artist} has already been played. Skipping.")
            return self.random_album()

        self._played_albums.add(album)
        logger.info(f"Added album: {album.title} by {album.artist} to the collection.")
        return album
