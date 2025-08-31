# without using the broadcasting

prices = [100,200,300]
discount = 10
final_prices = []

for price in prices:
    final_price = price - (price*discount/100)
    final_prices.append(final_price)

print(final_prices)


"""
How numpy handel arrays of different-different shapes
@ Matching dimestion [1,2,3]+[4,5,6] 
[5,7,9]
@ Expanding single elements [1,2,3]+10
@ Incompatible shapes [1,2,3] + [1,2]
"""

import numpy as np

arr = np.array([100,200,300])  # 1-D
result = arr*2
print(result)

matrix = np.array([[1,2,3],[4,5,6]]) # 2-D
vector = np.array([10,20,30])

result1 = matrix+vector
print(result1)

arr1 = np.array([[1,2,3],[4,5,6]])
arr2 = np.array([1,2])

# result2 = arr1 + arr2 
# print(result2)           # use .reshape() 



"""
Without using Vectorization:
"""
list1 = [1,2,3]
list2 =[4,5,6]

result = [x+y for x,y in zip(list1 , list2)]
print(result)


"""
Using Vectorization Concept :
"""
import numpy as np 
arr3 = np.array([1,2,3])
arr4 = np.array([4,5,6])

result = arr3 + arr4
print(result)


import numpy as np
arr5 = np.array([10,20,30])
multiplied = arr*3

print(multiplied)


"""
Broadcasting : It expands smaller arrays in larger array.
               It faster then loops.

               1D ->  2D 

Vectorization : Entire array
                100X  faster then loops 
               
"""