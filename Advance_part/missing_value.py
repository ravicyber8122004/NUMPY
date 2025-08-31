"""
Builtin function

np.isnan  --> detect missing values
np.nan_to_num()
np.isinf()  --> it is use to detect infinite value 


NaN  -> Not a Number  

"""

# np.isnan()

import numpy as np
arr = np.array([1,2,np.nan , 4,np.nan ,6])

print(np.isnan(arr))

#print(np.nan == np.nan)  # we can't directly compared this 


# np.nan_to_num(array , nan=value) default = 0

import numpy as np 

arr1 = np.array([1,2,np.nan , 4, np.nan , 6])

cleaned_arr = np.nan_to_num(arr1)

print(cleaned_arr)

# np.isinf()

import numpy as np
arr2 = np.array([1,2,np.inf,4,-np.inf , 6])

print(np.isinf(arr2))

cleaned_arr1 = np.nan_to_num(arr2 , posinf = 1000 , neginf = -1000)
print(cleaned_arr1)




"""
Refrence tutorial link :- https://youtu.be/9DhZ-JCWvDw?si=2B1w7gc9P-ZNWBcG
"""