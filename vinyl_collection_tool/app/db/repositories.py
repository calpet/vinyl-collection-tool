from app.db.conversions import api_album_to_db
from app.db.database import get_session
from app.db.entities import Collection
from app.utils.logger import Logger

logger = Logger()


class CollectionRepository:
    def __init__(self) -> None:
        """Initializes the CollectionRepository."""

    def save_collection(self, collection: Collection) -> None:
        """Saves the given Collection instance to the database.

        :param collection: The Collection instance to be saved."""
        num_albums = len(collection.albums) if hasattr(collection, "albums") else 0
        logger.info(f"Attempting to save {num_albums} albums to DB")
        try:
            with get_session() as session:
                albums = [api_album_to_db(album) for album in collection.albums]
                for album in albums:
                    session.add(album)
                session.commit()
            logger.info(f"Successfully saved {num_albums} albums to DB")
        except Exception as e:
            logger.error(f"Failed to save collection: {e}")
            raise