'''__init__ method is like default constructor in C++ and Java.
Constructors are used to initialize the object’s state.

The task of constructors is to initialize(assign values) to the data members of the class
when an object of the class is created.

Like methods, a constructor also contains a collection of statements(i.e. instructions)
that are executed at the time of Object creation. It is run as soon as an object of a class is instantiated.

The method is useful to do any initialization you want to do with your object.'''


class Student:
    def __init__(self,name,lastname):
        self.name=name
        self.lastname=lastname
        self.fullname= name + '_kumar_' + lastname

std1=Student("garv","mehra")
print(std1.fullname)
