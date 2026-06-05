"""SQLModel entities and junctions for the vinyl collection tool."""

from typing import Optional, List
from sqlalchemy import Column, JSON

from sqlmodel import SQLModel, Field, Relationship


class AlbumGenreLink(SQLModel, table=True):
    album_id: Optional[int] = Field(
        default=None, foreign_key="album.id", primary_key=True
    )
    genre_id: Optional[int] = Field(
        default=None, foreign_key="genre.id", primary_key=True
    )


class AlbumStyleLink(SQLModel, table=True):
    album_id: Optional[int] = Field(
        default=None, foreign_key="album.id", primary_key=True
    )
    style_id: Optional[int] = Field(
        default=None, foreign_key="style.id", primary_key=True
    )


class AlbumArtistLink(SQLModel, table=True):
    album_id: Optional[int] = Field(
        default=None, foreign_key="album.id", primary_key=True
    )
    artist_id: Optional[int] = Field(
        default=None, foreign_key="artist.id", primary_key=True
    )


class AlbumInCollectionLink(SQLModel, table=True):
    album_id: Optional[int] = Field(
        default=None, foreign_key="album.id", primary_key=True
    )
    collection_id: Optional[int] = Field(
        default=None, foreign_key="collection.id", primary_key=True
    )


class CollectionOwnerLink(SQLModel, table=True):
    collection_id: Optional[int] = Field(
        default=None, foreign_key="collection.id", primary_key=True
    )
    user_id: Optional[int] = Field(
        default=None, foreign_key="user.id", primary_key=True
    )


class Album(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    image: Optional[str] = None
    release_year: Optional[int] = None
    format: Optional[str] = None

    genres: List["Genre"] = Relationship(
        back_populates="albums", link_model=AlbumGenreLink
    )
    styles: List["Style"] = Relationship(
        back_populates="albums", link_model=AlbumStyleLink
    )
    artists: List["Artist"] = Relationship(
        back_populates="albums", link_model=AlbumArtistLink
    )
    collections: List["Collection"] = Relationship(
        back_populates="albums", link_model=AlbumInCollectionLink
    )
    vectors: List["AlbumVector"] = Relationship(back_populates="album")


class VectorSchema(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    style_weight: Optional[int] = None
    genre_weight: Optional[int] = None
    release_year_weight: Optional[int] = None
    album_vectors: List["AlbumVector"] = Relationship(back_populates="vector_schema")


class AlbumVector(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    album_id: Optional[int] = Field(default=None, foreign_key="album.id")
    vector_schema_id: Optional[int] = Field(default=None, foreign_key="vector_schema.id")
    vector: Optional[List[float]] = Field(default=None, sa_column=Column(JSON))
    album: Optional["Album"] = Relationship(back_populates="vectors")
    vector_schema: Optional["VectorSchema"] = Relationship(back_populates="album_vectors")


class Genre(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    albums: List[Album] = Relationship(
        back_populates="genres", link_model=AlbumGenreLink
    )


class Style(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    albums: List[Album] = Relationship(
        back_populates="styles", link_model=AlbumStyleLink
    )


class Collection(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    platform: str
    albums: List[Album] = Relationship(
        back_populates="collections", link_model=AlbumInCollectionLink
    )
    owners: List["User"] = Relationship(
        back_populates="collections", link_model=CollectionOwnerLink
    )


class Artist(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    albums: List[Album] = Relationship(
        back_populates="artists", link_model=AlbumArtistLink
    )


class User(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    collections: List[Collection] = Relationship(
        back_populates="owners", link_model=CollectionOwnerLink
    )
