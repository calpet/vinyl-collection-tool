"""Album picker strategy for selecting albums from a collection."""

from abc import ABC, abstractmethod
from app.models.collection import Collection
from app.models.album import Album


class AlbumPickerStrategy(ABC):
    """Class for handling album picking strategies."""
    
    def __init__(self, collection: Collection) -> None:
        """Initializes the AlbumPickerStrategy.
        
        :param collection: The collection to pick albums from.
        """
        self._collection = collection
        
    @abstractmethod
    def pick_album(self) -> Album:
        """Picks an album from the collection."""
        pass
