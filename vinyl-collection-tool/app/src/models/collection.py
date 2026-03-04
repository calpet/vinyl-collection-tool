"""Defines the Collection class representing the user's album collection."""

import random


class Collection:
    """Represents the user's album collection, providing methods to access and manipulate it."""

    def __init__(self, albums):
        """Initializes a Collection instance with a list of albums."""
        self._albums = albums

    @property
    def albums(self):
        """Returns the list of albums in the collection."""
        return self._albums

    def sorted_by_artist(self):
        """Returns the albums sorted by artist name."""
        return sorted(self._albums, key=lambda a: a.artist)

    def random(self):
        """Returns a random album from the collection."""
        return random.choice(self._albums) if self._albums else None
