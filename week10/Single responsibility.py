"""
SINGLE RESPONSIBILITY PRINCIPLE

The Single Responsibility Principle states that a class should do one thing and
therefore it should have only a single reason to change.
"""


class Album:
#take this as album 1
    def __init__(self, name, artist, songs) -> None:
        self.name = name
        self.artist = artist
        self.songs = songs

    def add_song(self, song):
        self.songs.append(song)

    def remove_song(self, song):
        self.songs.remove(song)

    # breaks the SRP !!! as this would want to search within album 2
    def search_album_by_artist(self):
        """ Searching the database for other albums by same artist """
        pass


# INSTEAD CREATE ANOTHER CLASS

class AlbumBrowser:
    """ Class for browsing the Albums database"""

    def search_album_by_artist(self, albums, artist):
        pass

    def search_album_starting_with_letter(self, albums, letter):
        pass
