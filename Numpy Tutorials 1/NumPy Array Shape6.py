# NumPy Array Shape

# Shape of an Array
  # The shape of an array is the number of elements in each dimension.

# Get the Shape of an Array
  # NumPy arrays have an attribute called shape that returns a tuple with each index having the number of corresponding elements.

# Example:
   # Print the shape of a 2-D array:

import numpy as np

unit = np.array([[1,2,3,4],[5,6,7,8]])

print(unit.shape)

# Own notes: totally four elements (column-wise) are there, so the last digit would be 4
#            Two rows are there, so first digit would be 2

# Example:
  # Create an array with 5 dimensions using ndmin using a vector with values 1,2,3,4,5 and verify that last dimension has value 5:

import numpy as np

unity = np.array([[1,2,3,4,5],[6,7,8,9,0]], ndmin = 5)

print(unity)
print("shape of the array is " , unity.shape)

# Own notes: Here ndmin is 5, so the output shape would be definietly 5, last digit would be 5 because there are five elements in vector
        # The fourth value would be two, because it's a two dimension means that two rows. 
        # And the first three values would be 1 by default. 


# What does the shape tuple represent?
  # Integers at every index tells about the number of elements the corresponding dimension has.
  # In the example above at index-4 we have value 4, so we can say that 5th ( 4 + 1 th) dimension has 4 elements.



