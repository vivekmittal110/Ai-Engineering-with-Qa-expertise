class Employee:
    def __init__(self,a,b):
        self.salary = a
        self.increment = b
    @property
    def salaryAfterIncrement(self):
        return ((self.salary* (self.increment/100)) + self.salary) 

emp1 = Employee(10000, 10)

print(emp1.salaryAfterIncrement)