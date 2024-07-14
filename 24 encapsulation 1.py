#to demonstrate protected members in python

class Vehicle:
    def __init__(self):
        self._mileage=15

class Zx10r(Vehicle):
    def __init__(self):
        Vehicle.__init__(self)
        print("mileage of zx10r is",self._mileage)
    def printi(self):
        print("bas itna hi deti hai ", self._mileage)
bike=Zx10r()
bike.printi()
