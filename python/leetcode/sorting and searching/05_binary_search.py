nums = [-1,0,3,5,9,12]
target = 9

n = len(nums)
s = 0
end = n-1

while s<=end:
    mid = (s+end)//2
    if nums[mid]==target:
        print(mid)
        break
    elif target>mid:
        s=mid
    else:
        end=mid
