import numpy as np
from numpy import random

# array = np.array([[1, 2, 3], [4, 5, 6]])
# print(array)
# print(array.shape)

# array = np.zeros((3, 4), dtype=int)
# array = np.ones((3, 4), dtype=int)
# array = np.full((3, 4), 5, dtype=int)
# array = np.random.random((3, 4))
# print(array)
# print(array[0, 0])
# print(array > 0.2)
# print(array[array > 0.2])
# print(np.round(array))

# first = np.array([1, 2, 3])
# second = np.array([1, 2, 3])
# print(first + second)

# dimension_inch = np.array([1, 2, 3])
# dimension_cm = dimension_inch * 2.5
# print(dimension_cm)

# arr = np.array([1, 2, 3, 4], ndmin=5)
# print(arr)
# print("Number of dimensions: ", arr.ndim)

# Print array from dimensions
# arr = np.array([[1, 2, 3, 4], [6, 7, 8, 9]])
# print(arr[0, 2])
# arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
# print(arr[1, 1, 1])

# Slicing array
# arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
# print(arr[0, 2:])
# print(arr[0:2, 3])
# print(arr[0:2, 1:4])

# Shape of Array
# arr = np.array([1, 2, 3, 4], ndmin=5)
# print(arr)
# print('shape of array :', arr.shape)


# arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
# for x in arr:
#     for y in x:
#         for z in y:
#             print(z)
#
# for x in np.nditer(arr):
#     print(x)

# Random number array
x = random.randint(100, size=(3, 5))
print(x)
y = random.choice([3, 5, 7, 9], size=(3, 5))
print(y)