
import numpy as np

# create a one dimensional array
arr1 = np.array([1,2,3])
print(arr1)

# create a 2D array
arr2 = np.array([[9.0, 8.0, 7.0], [5.0, 6.0, 7.0]])
print(arr2)

# check dimension of array
print(arr1.ndim)
print(arr2.ndim)

# check shape of array
print(arr1.shape)  # (3,) => an array of 3 values
print(arr2.shape)  # (2, 3) => an array of 2 arrays, each containing 3 values each

# check datatype of arrays
print(arr1.dtype)
print(arr2.dtype)

# In numpy we can change or specify the datatype of array.
# In numpy array must be homogeneous.
# If need heterogeneous then specify the datatype as object

stringArr = np.array(["Hello", "World"])
print(stringArr)
print(stringArr.dtype)

arr3 = np.array([1,5,9], dtype="float16")
print(arr3)
print(arr3.dtype)

arr3 = np.array([1,5,9], dtype="<U5")
print(arr3)
print(arr3.dtype)

# check size(in bytes) of an each element of array 
print(arr1.itemsize)
print(arr2.itemsize)
print(arr3.itemsize)

# check count of items in array
print(arr1.size)
print(arr2.size)
print(arr3.size)

# check total size(in bytes) of an array
print(arr1.itemsize * arr1.size)
print(arr2.itemsize * arr2.size)
print(arr3.itemsize * arr3.size)
# # OR use arr.nbytes
print(arr1.nbytes)
print(arr2.nbytes)
print(arr3.nbytes)


arr4 = np.array([[1,2,3,4,5,6,7], [8,9,10,11,12,13,14]])
# Accessing a specific element of array [row, col] 
print(arr1[2])
print(arr4[1,5])
print(arr4[1, -5])

# range of values
print(arr1[1:])
print(arr4[1][4])
print(arr4[1, 2:6])  # row = 1, values from [2:6] === arr4[1][2:6]

# get a specific row
print(arr4[1, :])     # get all 1st index row values
# get a specific columns
print(arr4[:, 4])   # get all 4th index column values

# start:stop:step works

# All zero array
shape = (5,)
zarr1 = np.zeros(shape)
print(zarr1)
shape = (5,2)
zarr1 = np.zeros(shape)
print(zarr1)

# All ones array
shape = (5,)
oarr1 = np.ones(shape)
print(oarr1)
shape = (5,2)
oarr1 = np.ones(shape)
print(oarr1)

# All n array
shape = (5,)
farr1 = np.full(shape, 5)
print(farr1)
shape = (5,2)
farr1 = np.full(shape, 3.6)
print(farr1)


# random array
rarr1 = np.random.rand(5,2)  # 5-rows, 2 cols
print(rarr1)
rarr2 = np.random.randint(7, size=(3,3))  # (endVal, size=shape)
print(rarr2)
rarr3 = np.random.randint(-2,3, size=(3,3))  # (startVal, endVal, size=shape)
print(rarr3)

# identity matrix
imat = np.identity(5)
print(imat)

# copy an array
a = np.array([1,2,3])
b = a.copy()
print(b)

# Arithmetic on each element of array
add = a + 5
print(add)
subtract = a -5
print(subtract)
mul = a * 5
print(mul)
div = a / 5
print(div)
power = a ** 2
print(power)

# Array to array Arithmetic (performs operation on corresponding elements)
a = np.array([1,2,3])
b = np.array([4,5,6])
print(a+b)
print(a-b)
print(a*b)
print(a/b)

# basic stats on array
a = np.array([[1,4,6], [9,2,3]])
# axis available for max, min too
print(np.max(a))  
print(np.min(a))
print(np.sum(a))
print(np.sum(a, axis=0))  # axis=0, sums columns
print(np.sum(a, axis=1))  # axis=1, sums rows


# Reshaping an array
before = a.copy()
print(before.shape)

# # NOTE: after(row * col) == before(row * col)
after = before.reshape((6,1))
print(after)
after = before.reshape((1,6))
print(after)
after = before.reshape((3,2))
print(after)
after = before.reshape((2,3,1))
print(after)




