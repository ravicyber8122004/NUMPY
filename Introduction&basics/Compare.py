# using normal python

temperatures = [35 , 36.5, 40 , 25, 37, 68 , 35, 19, 39]

total = 0
for x in temperatures:
    total += x
average = total/len(temperatures)

print(f"average: {average}")


# using numpy

import numpy as np
temp =np.array([23,24,45,34,25,25,25,24])

avg = np.mean(temp)
print(avg)