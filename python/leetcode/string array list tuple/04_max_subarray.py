nums = [-2,1,-3,4,-1,2,1,-5,4]
max_sum = nums[0]
sum = 0
n=len(nums)
for i in range(0,n):
    sum+=nums[i]
    if sum<0:
        sum=0
    if max_sum<sum:
        max_sum=sum
print(max_sum)
