# Inheritance is the capability of one class to derive or inherit the properties from another class.
'''Class BaseClass:
    {Body}
Class DerivedClass(BaseClass):
    {Body}'''

class mom:
    def mom_fun(self):
        print("this is mom class")

class son(mom):
    def child_fun(self):
        print("this is child class")

obj=son()
obj1=mom()
obj.mom_fun()
obj1.mom_fun()




