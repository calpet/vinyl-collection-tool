"""Defines the Album class representing an album in the collection."""


class Album:
    """Represents an album in the collection."""

    def __init__(self, title: str, artist: str, type: str) -> None:
        """Initializes an Album instance."""
        self.title = title
        self.artist = artist
        self.type = type
