
"""
Now we will create an method in an class
to perfrom sum operation
"""
class Sabzi:
    price=None # the scope of this price varibale is within an
               # class not inside an method


    def one_dozen_ki_price(self):
        print("Paisa of 1 dozen sabzi=",price*12)
       #above line will generate an error
        #NameError: name 'price' is not defined
        #to solve this we use self
mango = Sabzi()
mango.price=20
mango.one_dozen_ki_price()

# in next program we will solve this error
