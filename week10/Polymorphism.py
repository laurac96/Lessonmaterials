
"""
POLYMORPHISM

 In programming, polymorphism means the same function name (but different signatures) being used for different types.

In OOP polymorphism refers to the ability of an object to behave in multiple ways.
It is implemented via method-overloading and method overriding.

"""
# ### Example 1
# # len() being used for a string
# print(len("geeks"))
#
# # len() being used for a list
# print(len([10, 20, 30]))


### Example 2

# METHOD OVERRIDING - a method with the same name in the child class as in the parent class.
# The definition of the method differs in parent and child classes but the name remains the same.

#
# class Vehicle:
#     def print_details(self):
#         print("This is parent Vehicle class method")
#
#
# class Car(Vehicle):
#     def print_details(self):
#         print("This is child Car class method")
#
#
# class Cycle(Vehicle):
#     def print_details(self):
#         print("This is child Cycle class method")
#
#
# car_a = Vehicle()
# car_a. print_details()
#
# car_b = Car()
# car_b.print_details()
#
# car_c = Cycle()
# car_c.print_details()

#
# # METHOD OVERLOADING - the property of a method to behave in different ways,

# # depending upon the number or types of the parameters.

## Two or more methods have the same name but different numbers of parameters or different types of parameters, or both.

## Example 1

# First product method.
# Takes two argument and print their
# product

#
# def product(a, b):
# 	p = a * b
# 	print(p)
#
# # Second product method
# # Takes three argument and print their
# # product
#
#
# def product(a, b, c):
# 	p = a * b*c
# 	print(p)
#
# # Uncommenting the below line shows an error
# # product(4, 5)
#
#
# # This line will call the second product method
# product(4, 5, 5)



## Example 2
#
#
# class Car:
#
#    def start(self, a, b=None):
#
#         if b is not None:
#             print(a + b)
#         else:
#             print(a)