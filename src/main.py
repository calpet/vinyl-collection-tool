"""LPShuffler is a simple application that allows you to shuffle your vinyl collection and discover new albums. It uses the Discogs API to access your collection and provides a random album each time you run it."""
import os
import random

from discogs_client import Client


class Album:
    """Represents an album in the collection."""
    def __init__(self, title: str, artist: str, format: str) -> None:
        """Initializes an Album instance."""
        self.title = title
        self.artist = artist
        self.format = format


class DiscogsProxy:
    """Acts as a proxy to the Discogs API, handling authentication and data retrieval."""

    def __init__(self, agent, api_token) -> None:
        """Initializes the Discogs client and retrieves the user's identity."""
        self.client = Client(agent, user_token=api_token)
        self.user = self.client.identity()

    def get_releases(self):
        """Retrieves the releases from the user's collection."""
        return self.user.collection_folders[0].releases

    def get_pages(self):
        """Retrieves all pages of releases from the user's collection."""
        pages = []
        releases = self.get_releases()
        for i in range(releases.pages):
            pages.append(releases.page(i))
        return pages


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


class CollectionCreator:
    """Responsible for creating a Collection instance from the data retrieved via the DiscogsProxy."""

    def __init__(self, proxy: DiscogsProxy) -> None:
        """Initializes the CollectionCreator with a DiscogsProxy instance and retrieves the releases and pages."""
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


if __name__ == "__main__":
    proxy = DiscogsProxy('LPShuffler/0.1', os.getenv("DISCOGS_TOKEN"))
    collection_creator = CollectionCreator(proxy)
    coll = collection_creator.create_collection()
    random_album = coll.random()
    print(f"Random album: {random_album.artist} - {random_album.title}")
