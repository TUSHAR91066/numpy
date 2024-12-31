import numpy as np

# np.array() is used to create the array
b = np.array([[1,1,3,4],[2,4,5,5]])
print(b)

# .ndim is used to know the dimension of the array
c = b.ndim
print(c)

# .shape tell us (row,colums)
d = b.shape
print(d)

# .dtype is used to know the data type of the array
e = b.dtype
print(e)

#get size
sd = b.size
print(sd)

#get total size
sf = b.nbytes
print(sf)