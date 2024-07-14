class Calculate_area:
    def __init__(self,l,b,a,h,r):
        self.l=l
        self.b=b
        self.a=a
        self.h=h
        self.r=r
    def rectangle(self):
        print(f'area of rectangle is {self.l*self.b}')

    def square(self):
        print(f'area of square is {self.a*self.a}')

    def traingle(self):
        print(f'area of triangle is {0.5*self.l * self.h}')

    def circle(self):
        print(f'area of circle is {3.14*self.r*self.r}')

choice=int(input("enter 1 for rectangle, 2 for square, 3 for triangle,4 for circle= "))
length=int(input("enter length= "))
breadth=int(input("enter breadth= "))
side=int(input("enter side for square= "))
height=int(input("enter height= "))
radius=int(input("enter radius= "))

area=Calculate_area(length,breadth,side,height,radius)
if choice==1:
    area.rectangle()
elif choice==2:
    area.square()
elif choice==3:
    area.traingle()
elif choice==4:
    area.circle()