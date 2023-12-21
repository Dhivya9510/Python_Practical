# NumPy Filter Array

# Filtering Arrays
  # Getting some elements out of an existing array and creating a new array out of them is called filtering.

# In NumPy, you filter an array using a boolean index list.
  # A boolean index list is a list of booleans corresponding to indexes in the array.
  # If the value at an index is True that element is contained in the filtered array, if the value at that index is False that element is excluded from the filtered array.

#  Example:
   # Create an array from the elements on index 0 and 2:


import numpy as np

card = np.array([41,42,43,44,45,46])    # original array

x = [True,False,False,True,True,True]   # Create an boolean index array for the basic filtering method

newcard = card[x]                       # Now create the newarray after filtering. 

print(card)
print(newcard)

# or (directly given as below:)

import numpy as np

card = np.array([41,42,43,44,45,46])

x = card[[True,False,False,True,True,True]]
print(x)

# The example above will return [41, 43], why?
# Because the new array contains only the values where the filter array had the value True, in this case, index 0 and 2.

# Creating the Filter Array
  # In the example above we hard-coded the True and False values, but the common use is to create a filter array based on conditions.

#Example:
  # Create a FILTER ARRAY that will return only values higher than 42:


import numpy as np

do = np.array([41,42,43,4,45,46])   # Original array

filter_do = []                     # Create an empty list for filtering

for i in do:                       # for going through each element in do
    if i > 42:                     # if the element is higher than 42, set the value to True, otherwise False:
       filter_do.append(True)      
    else:
        filter_do.append(False)

newdo = do[filter_do]               # Create the newarray variable after filtering from original array

print(filter_do)
print(newdo)

# Example
  # Create a filter array that will return only even elements from the original array:

import numpy as np

hulk = np.array([1,2,3,4,5,6,7,8])    # Original array

filter_hulk= []                       # Create an empty list for filtering

for i in hulk:                        #  for going through each element in hulk
    if i %2 == 0:                     # if the element is completely divisble by 2, set the value to True, otherwise False
        filter_hulk.append(True)
    else:
        filter_hulk.append(False)

newhulk = hulk[filter_hulk]           # # Create the newarray variable after filtering from original array

print(filter_hulk)
print(newhulk)

# Creating Filter Directly From Array
  # The above example is quite a common task in NumPy and NumPy provides a nice way to tackle it.
  # We can directly substitute the array instead of the iterable variable in our condition and it will work just as we expect it to.
  # Example:
    # Create a filter array that will return only values higher than 42:

import numpy as np

ford = np.array([41,42,43,44,45,46])   # original array

x = ford > 42    # Remember need to put one conditional variable before creating the new filtering array variable. 

newford = ford[x]   # New filtering array.

print(x)
print(newford)

# Example
  # Create a filter array that will return only even elements from the original array:

import numpy as np
talks = np.array([1,2,3,4,5,6,7,8])

h = talks %2 == 0

newtalks = talks[h]

print(h)
print(newtalks)

# Own notes:

# Here there are three types of filtering given. 
# 1.    Original array, Boolean index list (Only with square brackets) and new filtering array. 
# 2.    Original array, Create empty list, for loop with if, else. And then new filtering array
# 3.    Original array, Conditional array, and new filtering array. 




print