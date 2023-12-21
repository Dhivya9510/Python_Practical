# NumPy Set Operations:

# What is a Set
  # A set in mathematics is a collection of unique elements.
  # Sets are used for operations involving frequent intersection, union and difference operations.

# Create Sets in NumPy
  # We can use NumPy's unique() method to find unique elements from any array. E.g. create a set array, but remember that the set arrays should only be 1-D arrays.

# Example:
  # Convert following array with repeated elements to a set:

import numpy as np

arr = np.array([1,1,2,2,2,3,4,4,5,6,6,6])

u = np.unique(arr)
print(u)

# Finding Union
  # To find the unique values of two arrays, use the union1d() method.

# Example
     # Find union of the following two set arrays:

import numpy as np

set1= np.array([1,2,3,4])
set2 = np.array([3,4,5,6])

newarr = np.union1d(set1,set2)
print(newarr)

# Finding Intersection
  # To find only the values that are present in both arrays, use the intersect1d() method.

# Example
    # Find intersection of the following two set arrays:

import numpy as np

arr1 = np.array([1,2,3,4,5])
arr2 = np.array([3,4,5,6,7])

new_arr = np.intersect1d(arr1,arr2,assume_unique = True)

print(new_arr)

# Note: the intersect1d() method takes an optional argument assume_unique, which if set to True can speed up computation. It should always be set to True when dealing with sets.

# Finding Difference
   # To find only the values in the first set that is NOT present in the seconds set, use the setdiff1d() method.

# Example
    # Find the difference of the set1 from set2:

import numpy as np

set1 = np.array([1,2,3,4])
set2 = np.array([3,4,5,6,7])

r = np.setdiff1d(set1,set2, assume_unique = True)
print(r)

# Note: the setdiff1d() method takes an optional argument assume_unique, which if set to True can speed up computation. It should always be set to True when dealing with sets.

# Finding Symmetric Difference
   # To find only the values that are NOT present in BOTH sets, use the setxor1d() method.

# Example
  # Find the symmetric difference of the set1 and set2:

import numpy as np

set1 = np.array([1,2,3,4,5])
set2 = np.array([2,3,4,5,6])

e = np.setxor1d(set1,set2, assume_unique = True)

print(e)


# Own notes : Use unique() for one single array with multiple repeated items
           #  Use union1d() for multiple sets to find the unique values. 
           # Note we can use ASSUME_UNIQUE = TRUE  optionally from intersection onwards.. 
           #  Note significantly that SETDIFF1D() is used to find DIFFERENCE between the two sets - THAT RETUNS THE VALUES PRESENT ONLY IN THE FIRST SET. 
           # Symmetric differnce is the one that are the values which not intersected. 
           # Note symmetric difference function is SETXOR1D() ~ it's setxor & 1d