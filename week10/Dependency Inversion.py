
"""
DEPENDENCY INVERSION PRINCIPLE

High-level modules should not depend on low-level modules.
Both should depend on abstractions (e.g. interfaces).
"""
from abc import ABC, abstractmethod

class AlbumShop:
    albums = []

    def add_album(self, name, artist, genre):
        self.albums.append((name, artist, genre))


class ViewRockAlbums:

    def __init__(self, album_shop):
        for album in album_shop.albums:
            if album[2] == "Rock":
                print("We have {} in our shop.".format(album[0]))

    # IMPORTANT
    # ViewRockAlbums explicitly depends on the fact that albums are stored in a tuple in a certain order inside AlbumShop.
    # It should have no knowledge of the internal structure of AlbumShop.
    # Now if we change the ordering in the tuples in the album, our code would break.


# INSTEAD

class GeneralAlbumShop:

    @abstractmethod
    def filter_by_genre(self, genre):
        pass


class MyAlbumShop(GeneralAlbumShop):
    albums = []

    def add_album(self, name, artist, genre):
        self.albums.append((name, artist, genre))

    def filter_by_genre(self, genre):
        for album in self.albums:
            if album[2] == genre:
                yield album[0]


class ViewRockAlbums:
    def __init__(self, album_store):
        for album_name in album_store.filter_by_genre("Rock"):
            print("We have {} in our shop.".format(album_name))

    # NOTE: if we had another type of AlbumShop, that decides to store the album differently,
    # it would need to implement the same interface for filter_by_genre to make ViewRockAlbums work.
