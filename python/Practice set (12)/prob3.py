
num = int(input("Enter a number : "))
l = [num*i for i in range(1,11)]
print(l)
with open("1.txt","w") as f1:
    f1.write(str(l))