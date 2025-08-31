import numpy as np

arr1 = np.array([1,2,3.5])
arr2 = np.array([[1,2,3],
                [4,5,6]])
arr3 = np.array([[[1,2,3],
                [4,5,6],
                [7,8,9],
                [8,9,10]
                ]])


print(arr2.shape)  # for shape 
print(arr2.size)   # for size
print(arr1.ndim)
print(arr2.ndim)   # find out the no. of dimestion in array
print(arr3.ndim)
print(arr1.dtype)  # for return the data type of element of array

arr4 = np.array([1.2, 4.3,6.4,2.4,9.5])
print(arr4.dtype)
arr5 = arr4.astype(int)
print(arr5)
print(arr5.dtype)