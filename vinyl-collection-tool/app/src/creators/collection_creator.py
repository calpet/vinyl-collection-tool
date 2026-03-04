"""Defines the CollectionCreator class responsible for creating a Collection instance from the data retrieved via the DiscogsProvider."""
from app.src.models.album import Album
from app.src.models.collection import Collection
from app.src.providers.discogs_provider import DiscogsProvider


class CollectionCreator:
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
                albums.append(album)
        return albums

    def create_collection(self) -> Collection:
        """Creates and returns a Collection instance containing the albums from the user's collection."""
        albums = self._create_album_list()
        return Collection(albums)