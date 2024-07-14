class Person:
    def __init__(self, n, c , dob,m):
        self.n=n
        self.c=c
        self.dob=dob
        self.m=m
    def current_age(self):

        if self.m>6:
            self.dob=self.dob+1
            self.m=12-(self.m-6)
            print(self.n,"age is",2024-self.dob,"years",self.m,"month")

        elif self.m==6:
            print(self.n,"age is",2024-self.dob)

        elif self.m<6:
            print(self.n,"age is",2024-self.dob,"years",6-self.m,"months")

name=input("enter your name= ")
country=input("enter your country= ")
dateofbirth=int(input("enter your birth date= "))
month=int(input("enter your birth month= "))
p=Person(name,country,dateofbirth,month)
p.current_age()