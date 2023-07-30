class Vehicle:
    def vehicle_method(self):
        print("This is parent vehicle class method")


    class Car(Vehicle):
        def car_method(self):
            print("This is child Car class method")

car_a=Car()
car_a.vehicle_method()
#the line above you will get error as it's outside scope of class. you cant access method of other class as its not a child class
car_a.car_method()

