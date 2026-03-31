"""Class for handling sessions."""
from app.models.collection import Collection
from app.creators.collection_creator import CollectionCreator
from app.models.album import Album
from app.utils import logger
from app.strategies.random_picker import RandomAlbum


class PlaybackOrchestrator:
    """Class for handling playback orchestration."""

    def __init__(self) -> None:
        """Initializes the PlaybackOrchestrator."""
        self._collection: Collection = CollectionCreator().create_collection()
        self._played_albums: set[Album] = set()
        
    def clear(self) -> None:
        """Clears the played albums set."""
        self._played_albums.clear()
        
    def random_album(self) -> Album:
        """Returns a random album from the collection."""
        rand = RandomAlbum(self._collection)
        album = rand.pick_album()
        if album in self._played_albums:
            logger.info(f"Album: {album.title} by {album.artist} has already been played. Skipping.")
            return self.random_album()

        self._played_albums.add(album)
        logger.info(f"Enqueuing album: {album.title} by {album.artist}.")
        return album
