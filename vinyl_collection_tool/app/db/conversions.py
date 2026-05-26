"""Conversion utilities between API models and SQLModel ORM entities."""
from typing import List
from vinyl_collection_tool.app.models.album import Album as ApiAlbum, AlbumType
from vinyl_collection_tool.app.db.entities import Album, Genre, Style, Artist

# API Album -> DB Album

def api_album_to_db(api_album: ApiAlbum, genres: List[Genre], styles: List[Style], artists: List[Artist]) -> Album:
    return Album(
        name=api_album.title,
        image=api_album.image,
        release_year=api_album.year,
        format=api_album.type.value,
        genres=genres,
        styles=styles,
        artists=artists
    )

# DB Album -> API Album

def db_album_to_api(db_album: Album) -> ApiAlbum:
    return ApiAlbum(
        title=db_album.name,
        artist=db_album.artists[0].name if db_album.artists else '',
        type=AlbumType(db_album.format) if db_album.format in AlbumType._value2member_map_ else AlbumType.NONE,
        image=db_album.image,
        year=db_album.release_year,
        genres=[g.name for g in db_album.genres],
        styles=[s.name for s in db_album.styles]
    )
