import numpy as np

np.random.seed(42)
arr = np.random.randint(1,51, size=(5,5))

arr[arr>25]=0
print(arr)

print("sum : ", np.sum(arr))
print("mean : ", np.mean(arr))
print("standard daviation : ", np.std(arr))