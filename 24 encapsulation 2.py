# to demonstrate private members
class Base:
    def __init__(self):
        self.a="geeks for geeks"
        self.__c="private c"
        self.c=self.__c


class Derived(Base):
    def __init__(self):
        Base.__init__(self)

    def print_C_of_Baseclass(self):
        print("private value of c",self.c)

obj1=Base()
print(obj1.a)
print(obj1.c)
obj2=Derived()
obj2.print_C_of_Baseclass()
