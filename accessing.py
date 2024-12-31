# In this file i learned about the how to access/changing
# rows, colums and elements in numpy.

import numpy as np

a = np.array([[1,2,3,4,5,6,7],[8,9,10,11,12,13,14]])
print(a)

#get a specfic element [r,c]
c = a[1,2]
print(c)

#get a specific row
d = a[:,6]
print(d) 

#get a specfic column
z = a[0,:]
print(z)