'''
Working on Python Abstract classes -

By default, Python does not provide abstract classes.
Python comes with a module that provides the base for defining Abstract Base classes(ABC) and that module name is ABC.
ABC works by decorating methods of the base class as an abstract
and then registering concrete classes as implementations of the abstract base.
A method becomes abstract when decorated with the keyword @abstractmethod.
'''
# Python program showing
# abstract base class work
from abc import ABC, abstractmethod


class Polygon(ABC):
    @abstractmethod
    def noofsides(self):
        pass


class Triangle(Polygon):
    def noofsides(self):  # overriding abstract method
        print("I have 3 sides")


class Quadrilateral(Polygon):
    def noofsides(self):  # overriding abstract method
        print("I have 4 sides")


# Driver code
R = Triangle()
R.noofsides()

K = Quadrilateral()
K.noofsides()