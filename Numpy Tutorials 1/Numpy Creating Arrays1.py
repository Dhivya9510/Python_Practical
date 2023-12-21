# NumPy Tutorial:
  # NumPy is a Python library.
  # NumPy is used for working with arrays.
  # NumPy is short for "Numerical Python".


import numpy 

tom = numpy.array(['a','b','c','d','e'])
print(tom)

# NumPy as np:
    # NumPy is usually imported under the np alias.
    # alias: In Python alias are an alternate name for referring to the same thing.
    # Create an alias with the as keyword while importing:


import numpy as np
tom = np.array(['a','b','c','d','e'])
print(tom)

# Checking NumPy Version
   # The version string is stored under __version__ attribute.


import numpy as np
print(np.__version__)

# NumPy Creating Arrays
  # Create a NumPy ndarray Object
    # NumPy is used to work with arrays. The array object in NumPy is called ndarray.
    # We can create a NumPy ndarray object by using the array() function.

import numpy as np

henry = np.array([1,2,3,4,5])
print(type(henry))

# Dimensions in Arrays
  # A dimension in arrays is one level of array depth (nested arrays).
  # nested array: are arrays that have arrays as their elements.

# 0-D Arrays
  # 0-D arrays, or Scalars, are the elements in an array. Each value in an array is a 0-D array.
  # Example:  
     # Create a 0-D array with value 42

import numpy as np

yolk = np.array(42)
print(yolk)

# 1-D Arrays
  # An array that has 0-D arrays as its elements is called uni-dimensional or 1-D array.
  # These are the most common and basic arrays.
  # Example:
     # Create a 1-D array containing the values 1,2,3,4,5:

import numpy as np

unit = np.array([2,4,6,8,10])
print(unit)

# 2-D Arrays
  # An array that has 1-D arrays as its elements is called a 2-D array.
  # These are often used to represent matrix or 2nd order tensors.
  # NumPy has a whole sub module dedicated towards matrix operations called numpy.mat
  # Example
     # Create a 2-D array containing two arrays with the values 1,2,3 and 4,5,6:

import numpy as np

unity = np.array([[1,2,3],[4,5,6]])
print(unity)

# 3-D arrays
  # An array that has 2-D arrays (matrices) as its elements is called 3-D array.
  # These are often used to represent a 3rd order tensor.
  # Example
    # Create a 3-D array with two 2-D arrays, both containing two arrays with the values 1,2,3 and 4,5,6:

import numpy as np

unitfy = np.array([[[1,2,3],[4,5,6]],[[1,2,3],[4,5,6]]])

print(unitfy)

# Check Number of Dimensions?
  # NumPy Arrays provides the ndim attribute that returns an integer that tells us how many dimensions the array have.
  # Example
    # Check how many dimensions the arrays have:

import numpy as np

unitfy = np.array([[[1,2,3],[4,5,6]],[[1,2,3],[4,5,6]]])
unity = np.array([[1,2,3],[4,5,6]])
unit = np.array([2,4,6,8,10])
yolk = np.array(42)

print(unitfy.ndim)
print(unity.ndim)
print(unit.ndim)
print(yolk.ndim)

# Higher Dimensional Arrays
  # An array can have any number of dimensions.
  # When the array is created, you can define the number of dimensions by using the ndmin argument.
  # Example
    # Create an array with 5 dimensions and verify that it has 5 dimensions:

import numpy as np

tommy = np.array([1,3,5,7,9], ndmin = 5)

print(tommy)
print("The number of total dimensions is ", tommy.ndim)

# In this array the innermost dimension (5th dim) has 4 elements, the 4th dim has 1 element that is the vector, the 3rd dim has 1 element that is the matrix with the vector, the 2nd dim has 1 element that is 3D array and 1st dim has 1 element that is a 4D array.

