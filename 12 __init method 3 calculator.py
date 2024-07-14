class Calculator:

    def __init__(self,a,b):
        self.a=a
        self.b=b
    def add(self):
        print("addition is =", self.a* self.b)
    def mul(self):
        print("multiplication is =", self.a * self.b)
    def sub(self):
        print("substraction is =", self.a- self.b)

obj=Calculator(5,3)
obj.add()
obj.sub()
obj.mul()
