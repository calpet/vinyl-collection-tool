"""Defines the Album class representing an album in the collection."""

from enum import Enum


class AlbumType(Enum):
    """Enumeration of possible album types."""
    NONE = "NONE"
    VINYL = "VINYL"
    CD = "CD"

class Album:
    """Represents an album in the collection."""

    def __init__(self, title: str, artist: str, type: AlbumType, image: str) -> None:
        """Initializes an Album instance."""
        self.title = title
        self.artist = artist
        self.type = type
        self.image = image
        
    def __eq__(self, other) -> bool:
        if not isinstance(other, Album):
            return False
        return (
            self.title == other.title and
            self.artist == other.artist and
            self.type == other.type
        )

    def __hash__(self) -> int:
        return hash((self.title, self.artist, self.type))
