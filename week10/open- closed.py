
"""
OPEN-CLOSED PRINCIPLE

Classes, modules, functions, etc. should be open for extension, but closed for modification.

Modification means changing the code of an existing class, and extension means adding new functionality.
"""

# BEFORE


class AlbumBrowser:

    def search_album_by_artist(self, albums, artist):
        return [album for album in albums if album.artist == artist]

    def search_album_by_genre(self, albums, genre):
        return [album for album in albums if album.genre == genre]

    # Now what happens if we want to search by artist or by genre?
    # What if we add release year?
    # We will have to write a new function every time modifying the class!


# INSTEAD

class SearchBy:
    def is_matched(self, album):
        pass


class SearchByGenre(SearchBy):
    def __init__(self, genre):
        self.genre = genre

    def is_matched(self, album):
        return album.genre == self.genre


class SearchByArtist(SearchBy):
    def __init__(self, artist):
        self.artist = artist

    def is_matched(self, album):
        return album.artist == self.artist


class AlbumBrowser:

    # Note we pass one of the classes as searchby arg
    def browse(self, albums, searchby):
        return [album for album in albums if searchby.is_matched(album)]
