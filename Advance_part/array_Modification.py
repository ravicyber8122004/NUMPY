"""
Add
Remove
Stack
Split
Merging
"""

# insert :- np.insert(array,index, value ,axis=None)

import numpy as np

arr = np.array([10,20,30,40,50,60])

new_arr = np.insert(arr , 4 , 45 , axis=0)
print(new_arr)

arr_2D = np.array([[10,20],[30,40]])
print(arr_2D)

new_arr_2D = np.insert(arr_2D , 1 , [5,6] ,axis=None)

print(new_arr_2D)
new_2D = np.insert(arr_2D , 1 , [5,6] ,axis=1)
print(new_2D)


# append :- It mean add new element at the end of the array 

import numpy as np

arr1 = ([20,30,40,50,60,70,80])

arr_append =np.append(arr1 ,[90,100,110,120,130])
print(arr_append)

# conacating.py

"""
np.concatenate((array1,array2),axis = 0)
axis 0 -> vertical stacking
axis 1 -> horizontal stacking
"""

import numpy as np
arr2 = np.array([1,2,3])
arr3 = np.array([4,5,6])

new_array = np.concatenate((arr2 , arr3))
print(new_array)

# Removing elements array
"""
np.delete(array , index , axis=none)
flattern array
"""

import numpy as np

arr4 = np.array([10,20,30,40,50,60])
print(arr4)
new_arr4 = np.delete(arr4,0)
print(new_arr4)

arr_2d = np.array([[1,2,3],[5,6,7]])
print(arr_2d)
new_arr_2D = np.delete(arr_2d , 0 , axis = 0)
print(new_arr_2D) 
