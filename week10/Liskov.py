
"""
LISKOV SUBSTITUTION PRINCIPLE

If we have a base class A and subclass B,
then we should be able to substitute the main class A with the subclass B without breaking the code.
"""

# we already have this class Album, let's copy it over
class Album:

    def __init__(self, name, artist, songs) -> None:
        self.name = name
        self.artist = artist
        self.songs = songs

    def add_song(self, song):
        self.songs.append(song)

    def remove_song(self, song):
        self.songs.remove(song)


# This subclass behave the same way as its parent class.
class BestOfCompilation(Album):

    def __init__(self, name, artist, songs):
        super().__init__(name, artist, songs)

