import numpy as np
arr = np.arange(1,17).reshape(4,4)
print(arr)

# sum_r = np.zeros((len(arr)))
# i = 0
# while i < len(arr):
#     sum_r[i] = sum(arr[i])
#     i+=1
# arr_tran = arr.T
# j = 0
# sum_c = np.zeros((len(arr_tran)))

# while j < len(arr_tran):
#     sum_c[j] = sum(arr_tran[j])
#     j+=1

# print(sum_r)
# print(sum_c)


# esy way
# axis 1 = rows
# axis 0 = cols
print(np.sum(arr,axis=1))
print(np.sum(arr,axis=0))