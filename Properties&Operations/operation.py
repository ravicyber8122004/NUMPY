import numpy as np

arr = np.array([10,20,30,40,50,60,70,80,90])

print(arr+10)
print(arr-10)
print(arr*10)
print(arr/10)
print(arr**2)


# Aggregation function in numpy

arr1 = np.array([10,20,30,40,50,27,38,28,37,27,28])

print(arr1.sum())
print(arr1.mean())
print(arr1.min())
print(arr1.max())
print(arr1.std())
print(arr1.var())