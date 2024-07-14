class vehicle:
    def type(self):
        print("vehicle class")

class twovehiler(vehicle):
    def bike(self):
        print("royal enfied 350")

class car(vehicle):
    def fourvehiler(self):
        print("car class")

class car1(car):
    def punch(self):
        print("punch car")

class car2(car):
    def nexon(self):
        print("nexon car")

obj1=twovehiler()
obj1.type()
obj1.bike()
obj2=car2()
obj2.fourvehiler()
obj2.type()