
"""
ENCAPSULATION

It refers to data hiding. In OOP one class should not have direct access to the data of the other class.
"""
### Example 1

class Computer:

    def __init__(self):
        self.__maxprice = 900

    def sell(self):
        print("Selling Price: {}".format(self.__maxprice))

    def setMaxPrice(self, price):
        self.__maxprice = price

c = Computer()
c.sell()

# change the price
c.__maxprice = 1000
c.sell()

# using setter function
c.setMaxPrice(1000)
c.sell()

### Example 2
# class Car:
#
#     def __init__(self, model):
#         # initialize instance variables
#         self.model = model
#
#     # Creates model property
#     @property
#     def model(self):
#         return self.__model
#
#     # Create property setter
#     @model.setter
#     def model(self, model):
#         if model < 2000:
#             self.__model = 2000
#         elif model > 2021:
#             self.__model = 2021
#         else:
#             self.__model = model
#
#     def getCarModel(self):
#         return "The car model is " + str(self.model)
#
#
# my_car = Car(2033)
# print(my_car.getCarModel())

