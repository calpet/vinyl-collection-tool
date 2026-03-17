"""Defines the DiscogsProvider class that interacts with the Discogs API to retrieve the user's album collection."""

from discogs_client import Client
from utils import logger


class DiscogsProvider:
    """Acts as a proxy to the Discogs API, handling authentication and data retrieval."""

    def __init__(self, agent, api_token) -> None:
        """Initializes the Discogs client and retrieves the user's identity."""
        self.client = Client(agent, user_token=api_token)
        self.user = self.client.identity()

    def get_releases(self) -> list:
        """Retrieves the releases from the user's collection."""
        return self.user.collection_folders[0].releases

    def get_pages(self) -> list:
        """Retrieves all pages of releases from the user's collection."""
        logger.debug("Retrieving pages of releases from Discogs...")
        pages = []
        releases = self.get_releases()
        for i in range(releases.pages):
            pages.append(releases.page(i))
        return pages
