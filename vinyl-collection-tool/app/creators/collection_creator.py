"""Defines the CollectionCreator class responsible for creating a Collection instance from the data retrieved via the DiscogsProvider."""

from app.models.album import Album, AlbumType
from app.models.collection import Collection
from app.providers.discogs_provider import DiscogsProvider


class CollectionCreator:
    """Responsible for creating a Collection instance from the data retrieved."""

    def __init__(self, proxy: DiscogsProvider) -> None:
        """Initializes the CollectionCreator."""
        self._proxy = proxy

    def create_collection(self) -> Collection:
        """Creates and returns a Collection instance containing the albums from the user's collection."""
        albums = self._process_pages()
        return Collection(albums)
    
    def _process_pages(self) -> list[Album]:
        """Processes the pages retrieved from the API, dedplicating albums and returning a list of unique albums."""
        unique_albums = set()
        for page in self._proxy.pages:
            for item in page:
                album_type_str = str(item.data["basic_information"]["formats"][0]["name"]).strip().upper()
                album = Album(title=item.data["basic_information"]["title"],
                              artist=item.data["basic_information"]["artists"][0]["name"],
                              type=AlbumType(album_type_str),
                              image=item.data["basic_information"]["cover_image"])
                unique_albums.add(album)
        return list(unique_albums)
        