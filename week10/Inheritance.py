"""
EXERCISE 2  --> INHERIT FROM A CLASS
"""


# #1.  Create Class Vehicle
class Vehicle:
    def vehicle_method(self):
        print("This is parent Vehicle class method")


# Create Class Car that inherits Vehicle
class Car(Vehicle):
    def car_method(self):
        print("This is child Car class method")


car_a = Car()
car_a.vehicle_method()
car_a.car_method()
#
#



# # MULTIPLE CHILDREN OF ONE PARENT CLASS
# # let's add another class
#
class Cycle(Vehicle):
    def cycleMethod(self):
        print("This is child Cycle class method")


car_b = Cycle()
car_b.vehicle_method()
#
#



# # MULTIPLE PARENTS
#
# class Camera:
#
#     def camera_method(self):
#         print("This is parent Camera class method")
#
#
# class Radio:
#
#     def radio_method(self):
#         print("This is parent Radio class method")
#
#
# class MobilePhone(Camera, Radio):
#
#     def cell_phone_method(self):
#         print("This is child MobilePhone class method")
#
#
# cell_phone_a = MobilePhone()
# cell_phone_a.camera_method()
# cell_phone_a.radio_method()

