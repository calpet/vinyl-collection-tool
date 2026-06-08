"""Class for handling sessions."""

from app.models.collection import Collection
from app.core.collection_importer import CollectionImporter
from app.models.album import Album
from app.utils import logger


class MusicSession:
    """Class for handling music sessions."""

    def __init__(self, username: str) -> None:
        """Initializes the MusicSession."""
        self._collection: Collection = CollectionImporter().import_collection(username)
        self._played_albums: set[Album] = set()

    def clear(self) -> None:
        """Clears the played albums set."""
        self._played_albums.clear()

    def random_album(self) -> Album:
        """Returns a random album from the collection."""
        album = self._collection.random
        if album in self._played_albums:
            logger.info(
                f"Album: {album.title} by {album.artist} has already been played. Skipping."
            )
            return self.random_album()

        self._played_albums.add(album)
        logger.info(f"Random album selected: {album.artist} - {album.title}.")
        return album
