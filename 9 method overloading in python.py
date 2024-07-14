#Method Overloading:

'''Two or more methods have the same name but different numbers of parameters
or different types of parameters, or both.
These methods are called overloaded methods and this is called method overloading.
python does not support method overloading by default.
But there are different ways to achieve method overloading in Python.
The problem with method overloading in Python is that we may overload the methods
but can only use the latest defined method.'''

class prod:
    a=None
    b=None

    def product(self,a, b):
        p = a * b
        print(p)

    def product(self,a, b, c):
        p = a * b * c
        print(p)

obj=prod()
obj.product(4,5,6)

#isme sirf second wala chalega kyunki python latest wale methods leta hai