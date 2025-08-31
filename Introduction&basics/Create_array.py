# Creating array from python list 

"""
np.array([e1,e2,e3,e4.....])
"""

import numpy as np
arr = np.array([1,2,3,4,5])
print(arr)

# Create array with default values
"""
np.arr(size)
"""

import numpy as np

array1 = np.zeros(3) # for 1-D array and default value zero
print(array1)

array2 = np.ones((2,3)) # for 2-D array and default value is one 
print(array2)

array3 = np.full((2,2),7) # array with customize default value like 7
print(array3)