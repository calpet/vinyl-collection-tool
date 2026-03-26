"""Defines the CollectionCreator class responsible for creating a Collection instance from the data retrieved via the DiscogsProvider."""

from app.utils import logger

from app.models.album import Album
from app.models.collection import Collection
from app.providers.discogs_provider import DiscogsProvider


class CollectionCreator:
    """Responsible for creating a Collection instance from the data retrieved."""

    def __init__(self, proxy: DiscogsProvider) -> None:
        """Initializes the CollectionCreator."""
        self._proxy = proxy

    def create_collection(self) -> Collection:
        """Creates and returns a Collection instance containing the albums from the user's collection."""
        albums = []
        for page in self._proxy.pages:
            for item in page:
                album = Album(title=item.data["basic_information"]["title"],
                              artist=item.data["basic_information"]["artists"][0]["name"],
                              type=item.data["basic_information"]["formats"][0]["name"],
                              image=item.data["basic_information"]["cover_image"])
                logger.debug(f"Created album: {album.artist} - {album.title} ({album.type})")
                albums.append(album)
        return Collection(albums)