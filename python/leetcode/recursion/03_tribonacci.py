def tribonacci(n):
    if n == 0 or n ==1:
        return n
    elif n == 2:
        return 1
    return tribonacci(n-3)+tribonacci(n-2)+tribonacci(n-1)
print(tribonacci(29))