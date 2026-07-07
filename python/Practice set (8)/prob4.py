def star(n):
    for i in range(n,0,-1):
        print("*"*i, end="")
        print()

n = int(input("Enter a number : "))
star(n)