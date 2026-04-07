"""Defines the DiscogsProvider class that interacts with the Discogs API to retrieve the user's album collection."""

from multiprocessing import AuthenticationError
from typing import ClassVar

from discogs_client import Client
from app.utils import logger


class DiscogsProvider:
    """Acts as a proxy to the Discogs API, handling authentication and data retrieval."""
    
    _AGENT = ClassVar[str]("LPShuffler/1.0")

    def __init__(self, username: str) -> None:
        """Initializes the Discogs client and retrieves the user's identity."""
        self._client = Client(self._AGENT, user_token=None)
        self._user = self._set_user(username)
        self._pages = self._load_pages()
        
    @property
    def pages(self) -> list:
        """Retrieves all pages of releases from the user's collection."""
        return self._pages
        
    def _set_user(self, username: str) -> None:
        """Sets the user for the Discogs client and retrieves the user's collection.
        
        :param username: The username of the Discogs user whose collection is to be retrieved."""
        try:
            self._user = self._client.user(username)
        except Exception as e:
            logger.error(f"Failed to set user '{username}': {e}")
            raise AuthenticationError(f"Failed to set user '{username}': {e}")

    def _load_pages(self) -> list:
        """Retrieves all pages of releases from the user's collection."""
        logger.debug("Retrieving pages of releases from Discogs...")
        pages = []
        user = self._client.user("calpet")
        releases = user.collection_folders[0].releases
        for i in range(releases.pages):
            pages.append(releases.page(i))
        return pages
