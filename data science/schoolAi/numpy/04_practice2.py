import numpy as np

arr1 = np.arange(1,10)
r1 = arr1.reshape((3,3))

r2 = r1.T
print(r1 + r2)
print(r1 - r2)
print(r1 * r2)
print(r1 / r2)