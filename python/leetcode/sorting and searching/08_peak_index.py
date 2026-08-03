arr = [0,10,5,2]
l = 0
n = len(arr)
r = n-2
ans = n-1
while l<=r:
    mid = (l+r)//2
    if arr[mid]<arr[mid+1]:
        l = mid+1
    else:
        ans=mid
        r=mid-1
