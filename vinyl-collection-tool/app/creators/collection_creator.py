"""Defines the CollectionCreator class responsible for creating a Collection instance from the data retrieved via the DiscogsProvider."""
from abc import ABC

from utils import logger

from models.album import Album
from models.collection import Collection
from providers.discogs_provider import DiscogsProvider

class CollectionCreator(ABC):
    """Abstract class for creating a Collection instance from the data retrieved."""
    
    def create_collection(self) -> Collection:
        """Creates and returns a Collection instance containing the albums from the user's collection."""
        pass


class DiscogsCollectionCreator(CollectionCreator):
    """Responsible for creating a Collection instance from the data retrieved via the DiscogsProvider."""

    def __init__(self, proxy: DiscogsProvider) -> None:
        """Initializes the CollectionCreator with a DiscogsProvider instance and retrieves the releases and pages."""
        self._releases = proxy.get_releases()
        self._all_pages = proxy.get_pages()

    def _create_album_list(self) -> list[Album]:
        """Creates a list of Album instances from the data retrieved from the Discogs API."""
        albums = []
        for page in self._all_pages:
            for item in page:
                album = Album(title=item.release.title,
                              artist=item.release.artists[0].name,
                              format=item.data["basic_information"]["formats"][0]["name"])
                logger.debug(f"Created album: {album.artist} - {album.title} ({album.format})")
                albums.append(album)
        return albums

    def create_collection(self) -> Collection:
        """Creates and returns a Collection instance containing the albums from the user's collection."""
        albums = self._create_album_list()
        return Collection(albums)