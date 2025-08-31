# INDEXING :-

"""
array[index] # for 1-D array
array[row,column]  # for 2-D array
""" 

import numpy as np 

arr1 = ([10,20,30,40,50,60])  # numpy array indexing start from the zero
print(arr1[4])
print(arr1[-1]) # numpy array last element indexing is -1

# Fancy Indexing :- Selecting multiple elements at once

import numpy as np 
arr3 =np.array([10,20,30,40,50,60,70,80,90])
print(arr3[[0,3,6]]) # consider the double indexing for using the fancy indexing 
 
# SLICING 

"""
array[start:end:step]
array[start:end] , start to end - 1
negative step -1 ,, # for acell element in reverse order

"""

import numpy as np

arr2 = np.array([10,20,30,40,50,60,70,80,90])

print(arr2[1:5])
print(arr2[1:5:2])
print(arr2[3:6:3])
print(arr2[:4])
print(arr2[::2])
print(arr2[::-1])