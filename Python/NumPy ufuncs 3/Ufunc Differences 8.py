# NumPy Differences:

# Differences
  # A discrete difference means subtracting two successive elements.
  # E.g. for [1, 2, 3, 4], the discrete difference would be [2-1, 3-2, 4-3] = [1, 1, 1]
  # To find the discrete difference, use the diff() function.

# Example:
  # Compute discrete difference of the following array:

import numpy as np

arr1 = np.array([5,10,15,20])

arr2 = np.diff(arr1)
print(arr2)

# We can perform this operation repeatedly by giving parameter n.
  # E.g. for [1, 2, 3, 4], the discrete difference with n = 2 would be [2-1, 3-2, 4-3] = [1, 1, 1] , then, since n=2, we will do it once more, with the new result: [1-1, 1-1] = [0, 0]
# Example:
  # Compute discrete difference of the following array twice:

import numpy as np

arr1 = np.array([4,12,10,5])

newarr = np.diff(arr1, n= 2)

print(newarr)

# Own notes: Subtract the second number from first number - this is the correct way.
           # Second example is quite interesting, n=2, until the output resulting two numbers it's keep subtracting the second from first. 
