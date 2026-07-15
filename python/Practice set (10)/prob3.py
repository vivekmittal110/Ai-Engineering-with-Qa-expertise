class cls:
    a = 10
    @staticmethod
    def display():
        print("hello there!!")
obj = cls()
obj.display()
obj.a = 20
print(obj.a)