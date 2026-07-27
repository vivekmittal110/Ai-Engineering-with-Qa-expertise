n = 12
def power(n):
    # while n%2 == 0:
    #     n//=2
    # if n == 1:
    #     print("power")
    # else:
    #     print("not")
    if n<=0:
        return False
    if n == 1:
        return True
    if n%2==0:
        power(n//2)
    else:
        return False
    
    
power(n)