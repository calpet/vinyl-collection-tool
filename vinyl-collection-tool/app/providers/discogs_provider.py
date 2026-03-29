"""Defines the DiscogsProvider class that interacts with the Discogs API to retrieve the user's album collection."""

from discogs_client import Client
from app.utils import logger
from app.utils.singleton import Singleton


class DiscogsProvider(metaclass=Singleton):
    """Acts as a proxy to the Discogs API, handling authentication and data retrieval."""

    def __init__(self, agent=None, api_token=None) -> None:
        """Initializes the Discogs client and retrieves the user's identity."""
        self._client = Client(agent, user_token=api_token)
        self._user = self._client.identity()
        self._pages = []

    @property
    def pages(self) -> list:
        """Retrieves all pages of releases from the user's collection."""
        if len(self._pages) == 0:
            self._pages = self._load_pages()
        return self._pages

    def _load_pages(self) -> list:
        """Retrieves all pages of releases from the user's collection."""
        logger.debug("Retrieving pages of releases from Discogs...")
        pages = []
        releases = self._user.collection_folders[0].releases
        for i in range(releases.pages):
            pages.append(releases.page(i))
        return pages
