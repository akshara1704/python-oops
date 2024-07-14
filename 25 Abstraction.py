'''ABSTRACTION-

Abstraction in python is defined as a process of handling complexity by hiding unnecessary information from the user.
This is one of the core concepts of object-oriented programming (OOP) languages.
That enables the user to implement even more complex logic on top of the provided abstraction without understanding
or even thinking about all the hidden background/back-end complexity.

An abstract class can be considered a blueprint for other classes.
It allows you to create a set of methods that must be created within any child classes built from the abstract class.
A class that contains one or more abstract methods is called an abstract class.
An abstract method is a method that has a declaration but does not have an implementation.
We use an abstract class while we are designing large functional units
or when we want to provide a common interface for different implementations of a component.'''

class Parent:
    def logic(self):
        pass

class Child(Parent):
    def logic(self):
        print("abstraction ho gya")

obj=Child()
obj.logic()