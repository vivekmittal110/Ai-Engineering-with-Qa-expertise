num = 54
divident = num
count = 0
s=set()
r = len(str(num))
for i in range (1,r+1):
    rem = num%10
    num = num//10
    s.add(rem)
print(s)
for i in s:
    if divident%i==0:
        count+=1
print(count)