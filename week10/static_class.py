
"""
STATIC & CLASS METHODS

Class methods are used for factory purposes, in the below code @classmethod details() is used to create a class object
 from a birth year instead of age.
Static methods are utility functions and work on data provided to them in arguments (NOTE: no 'self' passed in).
"""

#### Example 1

####If you want to call non-static methods, you’ll have to create an object.
####The code below does not work because an object is not created:
class Music:
    @staticmethod
    def play():
        print("*playing music*")

    def stop(self):
        print("stop playing")

Music.play()
Music.stop()

### If you create an object, we can call non-static methods. But you can also call the static method without creating the object.

# class Music:
#     @staticmethod
#     def play():
#         print("*playing music*")
#
#     def stop(self):
#         print("stop playing")
#
# Music.play()
#
# obj = Music()
# obj.stop()



### Example 2
#
# from datetime import date
#
#
# class Person:
#
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     @classmethod
#     def details(cls, name, year):
#         return cls(name, date.today().year - year)
#
#     @staticmethod
#     def check_age(age):
#         return age > 18
#
#
# person1 = Person('Jenny', 20)
# person2 = Person.details('Fatima', 1992)
#
#
# print(person1.name, person1.age)
# print(person2.name, person2.age)
#
# print(Person.check_age(33))
