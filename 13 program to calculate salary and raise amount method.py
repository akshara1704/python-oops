class Employee:
    def __init__(self,name:str,id:int,devices:list[str]):
        self.name=name
        self.id=id
        self.devices=devices
    def calculate_salary(self,salary):
        self.salary=salary
        print(f'yearly salary = {salary*12} INR')

    def raise_amount(self):
        raise_ratio=2
        print(f'new monthly salary={self.salary*raise_ratio}')

    def total_items(self):
        print(f'devices are {self.devices}')
        print(f'number of devices is {len(self.devices)}')


emp1=Employee("akshara",17,["laptop","iphone"])
emp1.calculate_salary(50000)
emp1.raise_amount()
emp1.total_items()