'''single inheritence in python
accessign parent class atributes '''
class mom:
    kitchen_size=None
    pocket_money=500
    def mom_fun(self):
        print("this is mom class")

class son(mom):
    def child_fun(self):
        print("this is child class")

mummy1=mom()
mummy1.pocket_money=6000
child=son()
print(child.pocket_money)