"""
Now we will create an method in an class
to perfrom some operation
"""
class calculator:
    a=None
    b=None

    def add(self):
        print("Addition is =",self.a+self.b)

    def sub(self):
        print("substraction is =",self.a-self.b)

    def mul(self):
        print("Multiply is =",self.a*self.b)


operation1 = calculator()
operation1.a=7
operation1.b=4
operation1.add()
operation1.sub()
operation1.mul()