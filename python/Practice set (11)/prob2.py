class Animal:
    pass
class pet(Animal):
    pass
class dog(pet):
    def bark(self):
        return "bow boww bowww"
    
d = dog()
print(d.bark())