# NumPy Sorting Arrays

# Sorting Arrays
  # Sorting means putting elements in an ordered sequence.
  # Ordered sequence is any sequence that has an order corresponding to elements, like numeric or alphabetical, ascending or descending.
  # The NumPy ndarray object has a function called sort(), that will sort a specified array.

# Example:
   # Sort the array:

import numpy as np

car = np.array([3,2,1])

h = np.sort(car)
print(h)

# Note: This method returns a copy of the array, leaving the original array unchanged.

# You can also sort arrays of strings, or any other data type:

# Example:
  # Sort the array alphabetically:

import numpy as np

tag = np.array(["Cherry","Banana","Apple"])

o = np.sort(tag)
print(o)

# Example
  # Sort a boolean array:

import numpy as np

iron = np.array([True, False, True])
r = np.sort(iron)
print(r)

# Sorting a 2-D Array
  # If you use the sort() method on a 2-D array, both arrays will be sorted:

# Example:
  # Sort a 2-D array:

import numpy as np

too = np.array([[3,4,1],[8,2,4]])
e = np.sort(too)
print(e)








