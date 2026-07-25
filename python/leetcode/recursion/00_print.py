# n = 5
# i = 1
# while i <= n:
#     print(i)
#     i+=1

def print_num(i,n):
    if i> n:
        return
    print(i)
    i+=1
    print_num(i,n)

n= 5
i = 1
print_num(i,n)