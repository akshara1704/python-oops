"""
Now we will create an method in an class
to perfrom an operation
"""
class Sabzi:
    price=None # the scope of this price varibale is within an
               # an class not inside an method
    def one_dozen_ki_price(self):
        print("Paisa of 1 dozen sabzi=",self.price*12)

mango = Sabzi()
mango.price=20
mango.one_dozen_ki_price()

#what is self
"""
“self” refers to the custom class used to access the class's members and methods,
as well as to create new members.SELF represents the instance of class. This handy 
keyword allows you to access variables, attributes, and methods of a defined class 
in Python.
"""