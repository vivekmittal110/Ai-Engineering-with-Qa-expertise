target = 13
nums = [2,4,5,7,11,15]
left = 0
right = len(nums)-1
while left<right:
    sum1 = nums[left]+nums[right]
    if sum1==target:
        print([left,right])
        break
    elif sum1>target:
        right-=1
    else:
        left+=1