# NumPy - Scientific Computation (DATA SCIENCE AND MACHINE LEARNING)
# pip install numpy
# pipenv install numpy

import numpy as np

array = np.array([1, 2, 3])  # Gives numpy array
print(array)
print(type(array))

td_ar = np.array([[1, 2, 3], [4, 5, 6]])  # A 2-D Array also called MATRIX
print(td_ar)
print(td_ar.shape)  # Returns a tuple specifying no of rows and columns

# Initialises a multidimensional array with 0 in a 3x4 matrix
mat = np.zeros((3, 4))  # floating type
print("\n", mat)

mat1 = np.zeros((3, 4), dtype=int)  # integer type
print("\n", mat, "\n")

# np.ones((3, 4), dtype=int)  # Initialises with 1
# np.full((3, 4), 5, dtype=int) # Initialises with 5 , custom number

# Generating Matrix with random numbers

# From random module importing random function and passing the shape of the matrix as an argument
matr = np.random.random((3, 4))
print(matr)
print(matr[0, 0])  # accessing element at first row and first column
print("\n", matr > 0.2)  # Returns boolean value

print("\n", matr[matr > 0.2])  # Will return the values

print("\n", np.sum(matr))  # Will return sum of all items in an array
