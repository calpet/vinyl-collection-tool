"""Random picker strategy for selecting albums from a collection."""
from app.strategies.album_picker import AlbumPickerStrategy
from app.models.album import Album


class RandomAlbum(AlbumPickerStrategy):
    """Class for handling random album picking strategy."""
    
    def pick_album(self) -> Album:
        """Picks a random album from the collection."""
        return self._collection.random
