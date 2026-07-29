nums = [3,1,2,4]
# odd=[]
# even=[]
# for i in nums:
#     if i%2==0:
#         even.append(i)
#     else:
#         odd.append(i)
# even.extend(odd)
# print(even)
start = 0
n = len(nums)
for i in range(0,n):
    if nums[i]%2==0:
        nums[start],nums[i]=nums[i],nums[start]
        start+=1
print(nums)