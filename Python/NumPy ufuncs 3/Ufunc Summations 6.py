 # NumPy Summations:

# Summations
   # What is the difference between summation and addition?
        # Addition is done between two arguments whereas summation happens over n elements.

# Example:
   # Add the values in arr1 to the values in arr2:

import numpy as np

arr1 = np.array([1,2,3])
arr2 = np.array([1,2,3])

arr3 = np.add(arr1,arr2)
print(arr3)

# Example
  # Sum the values in arr1 and the values in arr2:

import numpy as np

arr1 = np.array([1,2,3])
arr2 = np.array([1,2,3])

newarr = np.sum([arr1,arr2])
print(newarr)

# Summation Over an Axis
  # If you specify axis=1, NumPy will sum the numbers in each array.

# Example:
  # Perform summation in the following array over 1st axis:

import numpy as np

arr1 = np.array([1,2,3])
arr2 = np.array([1,2,3])

newarr = np.sum([arr1,arr2],axis =1)
print(newarr)

# Cummulative Sum
  # Cummulative sum means partially adding the elements in array.
  # E.g. The partial sum of [1, 2, 3, 4] would be [1, 1+2, 1+2+3, 1+2+3+4] = [1, 3, 6, 10].
  # Perfom partial sum with the cumsum() function.

# Example:
   # Perform cummulative summation in the following array:

import numpy as np

arr1 = np.array([1,2,3])

newarr1 = np.cumsum(arr1)
print(newarr1)

# Cumulative with two arrays:

import numpy as np

arr1 = np.array([1,2,3])
arr2 = np.array([1,2,3])

newarr = np.cumsum([arr1,arr2])
print(newarr)

# Own notes:  In summation coding, note that there included a square bracket which was not in add. 
             # And in cumulative there is only one array. And if there are two arrays, it will continue adding like summation. Example above. 

