#greatest of three
def great(x,y,z):
    if x > y and x >z:
        return x
    elif y > x and y > z:
        return y
    else:
        return z

a = int(input("Enter first number : "))
b = int(input("Enter second number : "))
c = int(input("Enter third number : "))
print(f"Greatest of three numbers is : {great(a,b,c)}")