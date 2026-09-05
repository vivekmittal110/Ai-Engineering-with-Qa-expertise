import numpy as np
salary = np.array([
    [30000, 40000, 50000],
    [45000, 55000, 65000],
    [35000, 42000, 58000]
])
print(salary*1.1)
print(salary+5000)
bonus = np.array([1.1,1.15,1.2])
print(salary*bonus)
print((salary-np.min(salary))/(np.max(salary)-np.min(salary)))