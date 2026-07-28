low = int(input())
high = int(input())

# 1 11   6  11-1 n+1
# 1 10   5  10-1 n+1
# 2 11   5  11-2 n+1
# 2 10   4  10-2 n
# 4 16   6  12 

ans = high - low 
ret = ans//2
if low % 2 != 0 or high %2 != 0:
    ret+=1
print(ret)