class calculator:
    def __init__(self,a):
        self.square = a*a
        self.cube = a*a*a
        self.squareroot = a**0.5
num = int(input("Enter a number: "))
obj = calculator(num)
print(obj.square,obj.cube, obj.squareroot)
