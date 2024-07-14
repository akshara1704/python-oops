class mom:
    def __init__(self,kitchen_size,pocket_money):
        self.kitchen_size=kitchen_size
        self.pocket_money=pocket_money

    def mom_fun(self):
        print("this is mom class")

class son(mom):
    def child_fun(self):
        print("this is child class")

mummy=mom(200,5000)
child=son()
print(child.pocket_money)