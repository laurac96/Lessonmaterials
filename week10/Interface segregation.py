
"""
INTERFACE SEGREGATION PRINCIPLE

“Clients should not be forced to depend upon interfaces that they do not use.”

An interface is a description of behaviors that an object can do.
For example, when you press the power button on the TV remote control, it turns the TV on, and you don’t need to care how.

In object-oriented programming, an interface is a set of methods an object must-have.
 The purpose of interfaces is to allow clients to request the correct methods of an object via its interface.
"""
### Example 1

### First, define a Vehicle abstract class that has two abstract methods, go() and fly():

from abc import ABC, abstractmethod


class Vehicle(ABC):
    @abstractmethod
    def go(self):
        pass

    @abstractmethod
    def fly(self):
        pass

### Second, define the Aircraft class that inherits
# from the Vehicle class and implement both go() and fly() methods:

class Aircraft(Vehicle):
    def go(self):
        print("Taxiing")

    def fly(self):
        print("Flying")

### Third, define the Car class that inherits from the Vehicle class.
# Since a car cannot fly, we raise an exception in the fly() method:

class Car(Vehicle):
    def go(self):
        print("Going")

    def fly(self):
        raise Exception('The car cannot fly')
### In this design the Car class must implement the fly() method from the Vehicle class that the Car class doesn’t use.
# Therefore, this design violates the interface segregation principle.
### To fix this, you need to split the Vehicle class into small ones
# and inherits from these classes from the Aircraft and Car classes:
### 1. First, split the Vehicle interface into two smaller interfaces:
# Movable and Flyable, and inherits the Movable class from the Flyable class:

class Movable(ABC):
    @abstractmethod
    def go(self):
        pass


class Flyable(Movable):
    @abstractmethod
    def fly(self):
        pass

### 2. Second, inherits from the Flyable class from the Aircraft class:
class Aircraft(Flyable):
    def go(self):
        print("Taxiing")

    def fly(self):
        print("Flying")

### 3. Third, inherit the Movable class from the Car class:

class Car(Movable):
    def go(self):
        print("Going")


#### Example 2

class PlaySongs:

    def __init__(self, title):
        self.title = title

    def play_drums(self):
        print("Bum-bum-bum")

    def play_guitar(self):
        print("Some guitar solo*")

    def sing_lyrics(self):
        print("Lalalalala")


# This class is fine, just changing the guitar and lyrics
class PlayRockSongs(PlaySongs):

    def play_guitar(self):
        print("Heavy metal guitar solo*")

    def sing_lyrics(self):
        print("We will, we will rock you!")


# This breaks the ISP, we don't have lyrics!!!!!
class PlayInstrumentalSongs(PlaySongs):
    def sing_lyrics(self):
        raise Exception("No lyrics for instrumental songs")


# INSTEAD

from abc import abstractmethod


class PlaySongsLyrics:

    @abstractmethod
    def sing_lyrics(self):
        pass


class PlaySongsMusic:

    @abstractmethod
    def play_guitar(self):
        pass

    @abstractmethod
    def play_drums(self):
        pass


class PlayInstrumentalSong(PlaySongsMusic):

    def play_drums(self):
        print("Bum-bum-bum")

    def play_guitar(self):
        print("Some guitar solo*")


class PlayRockSong(PlaySongsMusic, PlaySongsLyrics):

    def play_guitar(self):
        print("Heavy metal guitar solo*")

    def sing_lyrics(self):
        print("We will, we will rock you")

    def play_drums(self):
        print("Bum-bum-bum")

