# NumPy LCM Lowest Common Multiple

# Finding LCM (Lowest Common Multiple)
  # The Lowest Common Multiple is the smallest number that is a common multiple of two numbers.
  # Example:
     # Find the LCM of the following two numbers:

import numpy as np

num1 = 8
num2 = 10

u = np.lcm(num1,num2)
print(u)

# Finding LCM in Arrays
  # To find the Lowest Common Multiple of all values in an array, you can use the reduce() method.
  # The reduce() method will use the ufunc, in this case the lcm() function, on each element, and reduce the array by one dimension.
  # Example
     # Find the LCM of the values of the following array:

import numpy as np

arr = np.array([3,6,9])

y = np.lcm.reduce(arr)
print(y)

# Example
  # Find the LCM of all values of an array where the array contains all integers from 1 to 10:

import numpy as np

array = np.arange(1,11)

i = np.lcm.reduce(array)
print(i)

# Own notes: To find LCM simply between two numbers, we can simply use np.lcm()
            # To find LCM for the values in an ARRAY, We should use the reduce() i.e np.lcm.reduce()
            # To find LCM for the set of values, we should use arange() before np.lcm.reduce()
