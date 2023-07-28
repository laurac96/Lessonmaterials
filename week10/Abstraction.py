
"""
ABSTRACTION

In Python, abstraction is the process of hiding implementation details from the user
"""

# 'Old' way


class Shape(object):
    def calc_perimeter(self):
        raise NotImplementedError("Please Implement this method")


class Triangle(Shape):

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def calc_perimeter(self):
        perim = self.a + self.b + self.c
        print("Consider me implemented", perim)
        return perim


# 'New' way using abc library

###Example 1

from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

### Example 2
# import abc
#
#
# class Shape1(object):
#     __metaclass__ = abc.ABCMeta
#
#     @abc.abstractmethod
#     def calc_perimeter(self, input):
#         """Method documentation"""
#         return
#
#
# class Triangle1(Shape):
#
#     def __init__(self, a, b, c):
#         self.a = a
#         self.b = b
#         self.c = c
#
#     def calc_perimeter(self):
#         perim = self.a + self.b + self.c
#         print("Consider me implemented", perim)
#         return perim

