"""
change in dimenstion and shape of an array without change in that shpae

reshape(rows , columns) specify new shape
Condition:- if dimensions match
"""

import numpy as np

arr = np.array([10,20,30,40,50,60,70,80,90])
reshaped_arr = arr.reshape(3,3)
print(reshaped_arr)


# flattering array :- Ot is used to change multidimestional array in 1-D array
"""
.ravel() -> views update
.flatten() ->copy
"""

import numpy as np

arr_2D = np.array([10,20,30,40,50,60,70,80,90])
# print(arr_2D.ravel())
print(arr_2D.flatten())
print(arr_2D)