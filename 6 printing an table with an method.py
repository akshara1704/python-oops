class table:
    a=None

    def garv(self):
        for i in range(1,11):
            print(self.a ,"*",i,"=",self.a*i)


obj=table()
obj.a=3
obj.garv()
