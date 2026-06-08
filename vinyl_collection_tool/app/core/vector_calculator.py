from vinyl_collection_tool.app.db.entities import Album, Genre, Style


class VectorCalculator:
    """Class for calculating vectors for albums."""
    
    def __init__(
        self, 
        style_weight: int = 1, 
        genre_weight: int = 1, 
        release_year_weight: int = 1
    ) -> None:
        """Initializes the VectorCalculator."""
        self.style_weight = style_weight
        self.genre_weight = genre_weight
        self.release_year_weight = release_year_weight
        
    def calculate_vector(self, album: Album) -> list[float]:
        """Calculates the vector for a given album.
        
        :param album: The album for which to calculate the vector.

        :return: A list of floats representing the album's vector."""
        style_vector = self._calculate_style_vector(album.styles)
        genre_vector = self._calculate_genre_vector(album.genres)
        release_year_vector = self._calculate_release_year_vector(album.release_year)

        combined_vector = [
            self.style_weight * style_vector[i] + 
            self.genre_weight * genre_vector[i] + 
            self.release_year_weight * release_year_vector[i]
            for i in range(len(style_vector))
        ]
        
        return combined_vector
    
    def _calculate_style_vector(self, styles: list[Style]) -> list[float]:
        """Calculates the style vector for the album."""
        # Placeholder implementation - replace with actual logic
        return [1.0 if style else 0.0 for style in styles]

    def _calculate_genre_vector(self, genres: list[Genre]) -> list[float]:
        """Calculates the genre vector for the album."""
        # Placeholder implementation - replace with actual logic
        return [1.0 if genre else 0.0 for genre in genres]

    def _calculate_release_year_vector(self, release_year: int) -> list[float]:
        """Calculates the release year vector for the album."""
        # Placeholder implementation - replace with actual logic
        return [1.0 if release_year else 0.0]