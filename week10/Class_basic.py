"""
EXERCISE 1  --> CREATE & INSTANTIATE A CLASS

1. The self Parameter
The self parameter is a reference to the current instance of the class, and is used to access variables that belongs to the class.

It does not have to be named self , you can call it whatever you like, but it has to be the first parameter of any function in the class:


2. The __init__() Function
All classes have a function called __init__(), which is always executed when the class is being initiated.

Use the __init__() function to assign values to object properties, or other operations that are necessary to do
when the object is being created:

The __init__() function is called automatically every time the class is being used to create a new object.

By using the “self”  we can access the attributes and methods of the class in python.
It binds the attributes with the given arguments.
"""

# # HOW TO CREATE A CLASS
# #
# # 1.  ADD ATTRIBUTES TO A CLASS
# class Cat:
#
#     def __init__(self, name, age, breed):
#         self.name = name
#         self.age = age
#         self.breed = breed
#
#
# # create new objects
#
# jake = Cat('Jake', 5, 'Persian')
# print(jake.name)
# print(jake.age)
#
# print(jake.name + " is " + str(jake.age) + " years old.")

#
#



# # 2. DEFINE METHODS IN CLASS
# class Cat:
#
#     def __init__(self, name, age, breed):
#         self.name = name
#         self.age = age
#         self.breed = breed
#
#     def meow(self):
#         print('Mrr meow meow!')
#
#     def get_info(self):
#         print(self.name + " is " + str(self.age) + " years old " + self.breed + " cat.")
#
#
# # create new objects
# jake = Cat('Jake', 5, 'Persian')
# jake.meow()
#
#
# # create more new objects
# pippa = Cat('Pippa', 3, 'Bengal')
# snowy = Cat('Snowy', 8, 'Siamese')
# sparky = Cat('Sparky', 2, 'Ragdoll')
#
# pippa.get_info()
# snowy.get_info()
# sparky.get_info()
#
#



# # 3. ASSIGN NEW VALUE TO THE ATTRIBUTE IN CLASS
class Cat:

    def __init__(self, name, age, breed):
        self.name = name
        self.age = age
        self.breed = breed

    def meow(self):
        print('Mrr meow meow!')

    def get_info(self):
        print(self.name + " is " + str(self.age) + " years old " + self.breed + " cat.")

    def birthday(self, friend):
        """
        add one year to cat's age
        """
        self.friend= friend
        self.age += 1


# create a new object
jake = Cat('Jake', 5, 'Persian')
print(jake.age)

# call age method
jake.birthday("Twink")
print(jake.age)
print(jake.friend)
#
#



# #4.  PASSING ARGUMENTS TO METHODS
# class Cat:
#
#     def __init__(self, name, age, breed):
#         self.name = name
#         self.age = age
#         self.breed = breed
#
#     def meow(self):
#         print('Mrr meow meow!')
#
#     def get_info(self):
#         print(self.name + " is " + str(self.age) + " years old " + self.breed + " cat.")
#
#     def birthday(self):
#         """
#         add one year to cat's age
#         """
#         self.age += 1
#
#     def set_friend(self, friend):
#         """
#         link a friend to this cat and the cat to a friend
#         """
#         self.friend = friend
#         friend.friend = self
#
#
# # create new objects
# snowy = Cat('Snowy', 8, 'Siamese')
# sparky = Cat('Sparky', 2, 'Ragdoll')
#
# snowy.set_friend(sparky)
#
# # Let's check snowy's friend settings
# print(snowy.friend.name)
# print(snowy.friend.age)
#
#
# # same can be done for sparky
# print(sparky.friend.name)
# print(sparky.friend.age)