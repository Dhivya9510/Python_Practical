# NumPy Searching Arrays

#  Searching Arrays
  # You can search an array for a certain value, and return the indexes that get a match.
  # To search an array, use the where() method.
  # Example:
     # Find the indexes where the value is 4:

import numpy as np

car = np.array([1,2,2,3,4,4,5,6,4,7])

u = np.where(car == 4)
print(u)

# The example above will return a tuple: (array([4,5,8],)
   # Which means that the value 4 is present at index 4, 5, and 8.

# Example
  # Find the indexes where the values are even:

import numpy as np

unit = np.array([1,2,3,4,5,6,7,8])
i = np.where(unit%2 == 0)
print(i)

# Example
  # Find the indexes where the values are odd:

import numpy as np

icon = np.array([1,2,3,4,5,6,7])
o = np.where(icon%2 == 1)
print(o)

# Search Sorted
  # There is a method called searchsorted() which performs a binary search in the array, and returns the index where the specified value would be inserted to maintain the search order.
  # The searchsorted() method is assumed to be used on sorted arrays.

# Example:
  # Find the indexes where the value 5 should be inserted:

import numpy as np

yolk = np.array([1,2,3,4,5,6,7,8])

t = np.searchsorted(yolk, 5)
print(t)

# Own notes: Search and searchsorted are moreover the same hence search does not see the sorted array but the searchsorted does. 
#            The only difference between the two when we use that is, if we want to MAINTAIN THE SORT ORDER OR NO NEED TO MAINTAIN THE SORT ORDER. 

# Example explained: The number 7 should be inserted on index 1 to remain the sort order.
  # The method starts the search from the left and returns the first index where the number 7 is no longer larger than the next value.

# Search From the Right Side
  # By default the left most index is returned, but we can give side='right' to return the right most index instead.

# Example:
  # Find the indexes where the value 8 should be inserted, starting from the right:

import numpy as np

horn = np.array([2,4,6,8,10])

u = np.searchsorted(horn, 8, side = "right")
print(u)

# Example explained: The number 7 should be inserted on index 2 to remain the sort order.
 # The method starts the search from the right and returns the first index where the number 7 is no longer less than the next value.

# Multiple Values
  # To search for more than one value, use an array with the specified values.

#Example:
   # Find the indexes where the values 2, 4, and 6 should be inserted:

import numpy as np

tag = np.array([1,3,5,7,9])

r = np.searchsorted(tag, [2,4,6])

print(r)

# The return value is an array: [1 2 3] containing the three indexes where 2, 4, 6 would be inserted in the original array to maintain the order.

# Own notes: Wanna search simply the value in array, use 'where()' method
# Wanna search value by considering the sort order array, use 'searchsorted()' method. 





 







