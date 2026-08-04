matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 3

rows=len(matrix)
cols = len(matrix[0])
l = 0
r = rows*cols-1

while l<=r:
    mid = (l+r)//2
    if matrix[mid//cols][mid%cols] == target:
        print("yes")
        break
    elif matrix[mid//cols][mid%cols] > target:
        r = mid-1
    else:
        l = mid+1 