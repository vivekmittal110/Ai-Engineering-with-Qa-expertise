nums = [2,0,2,1,1,0]

mx = max(nums)
freq = [0]*(mx+1)
for i in nums:
    freq[i]+=1

nums=[]
print(freq)
for i in range(0,mx+1):
    while freq[i]>0:
        nums.append(i)
        freq[i]-=1
print(nums)