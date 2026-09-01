import numpy as np
arr = np.arange(1,21)
print(arr[0])
print(arr[-1])
print(arr[0:5])
print(arr[-1:-6:-1])
print(arr[::-1])
print(arr[5:16:])
arr[:5] = 0
print(arr)
arr[1::2] = 1
print(arr)
arr[arr[:]>10] = 60
print(arr)
print(arr[arr[:]%2!=0])
print(arr[(arr[:]<=15) & (arr[:]>=5)])