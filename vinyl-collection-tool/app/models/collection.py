"""Defines the Collection class representing the user's album collection."""

import random

from models.album import Album


class Collection:
    """Represents the user's album collection, providing methods to access and manipulate it."""

    def __init__(self, albums: list[Album]) -> None:
        """Initializes a Collection instance with a list of albums."""
        self._albums = albums

    @property
    def albums(self) -> list[Album]:
        """Returns the list of albums in the collection."""
        return self._albums
    
    @property
    def random(self) -> Album:
        """Returns a random album from the collection."""
        return random.choice(self._albums)

    def sorted_by_artist(self) -> list[Album]:
        """Returns the albums sorted by artist name."""
        return sorted(self._albums, key=lambda a: a.artist)
    
    def sorted_by_title(self) -> list[Album]:
        """Returns the albums sorted by title."""
        return sorted(self._albums, key=lambda a: a.title)
