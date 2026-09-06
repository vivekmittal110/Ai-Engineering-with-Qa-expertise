import numpy as np
np.random.seed(42)
age = np.random.randint(20,80,size=(100,1))
experience = np.random.randint(0,60,size=(100,1))
salary = np.random.randint(20000,80000,size=(100,1))
performance = np.random.randint(0,10,size=(100,1))
projects = np.random.randint(0,1000,size=(100,1))
hours_worked = np.random.randint(6,12,size=(100,1))
data = np.hstack([age,experience,salary,performance,projects,hours_worked])
print(data[:3])
print(np.shape(data))
mask = data[:,0]>data[:,1]
print(mask[:5])
data1 = data[mask]
print(np.shape(data1))
print("avg age",np.mean(data1[:,0]))
print("avg exp",np.mean(data1[:,1]))
print("median of salary",np.median(data1[:,2]))
print("std of performance",np.std(data1[:,3]))
print("max sal", np.max(data1[:,2]))
print("min age", np.min(data1[:,0]))


older = data[data[:,0]>50]
print(np.shape(older))