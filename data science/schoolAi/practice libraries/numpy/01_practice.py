import numpy as np
numbers = [[10, 20, 30, 40, 50],[0,0,0,0,0]]
nums = np.array(numbers,dtype="float")
print(nums)
print(type(nums))
print(np.ndim(nums))
print(np.shape(nums))
print(np.size(nums))

int_arr = nums.astype(int)
print(int_arr)

tuple_arr = np.array(((1,2,3,4,4),(2,4,6,7,8)))
print(tuple_arr)

range_arr = np.arange(0,10,2)
print(range_arr)

a = np.array([10, 20, 30, 40, 50])
b = np.array([2, 4, 6, 8, 10])
print(a+b)
print(a-b)
print(a/b)
print(a*b)
print(a**2)
print(a%2)