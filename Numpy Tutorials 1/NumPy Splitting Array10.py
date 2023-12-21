# NumPy Splitting Array

# Splitting NumPy Arrays
  # Splitting is reverse operation of Joining.
  # Joining merges multiple arrays into one and Splitting breaks one array into multiple.
  # We use array_split() for splitting arrays, we pass it the array we want to split and the number of splits.
  # Example
    # Split the array in 3 parts:

import numpy as np

you = np.array([1,2,3,4,5,6])

newyou = np.array_split(you,3)
print(newyou)

# Note: The return value is a list containing three arrays.

# If the array has less elements than required, it will adjust from the end accordingly.
 # Example:
   # Split the array in 4 parts:

import numpy as np

unit = np.array([1,2,3,4,5,6])
newunit = np.array_split(unit, 4)
print(newunit)

# Note: We also have the method split() available but it will not adjust the elements when elements are less in source array for splitting like in example above, array_split() worked properly but split() would fail.

# Split Into Arrays
  # The return value of the array_split() method is an array containing each of the split as an array.
  # If you split an array into 3 arrays, you can access them from the result just like any array element:
  # Example:
      # Access the splitted arrays:

import numpy as np

ipo = np.array([1,2,3,4,5,6])

newipo = np.array_split(ipo,3)

print(newipo[0])
print(newipo[1])
print(newipo[2])

# Own note: When we want to access the splitted array, we have to give the index number as shown above. 

# Splitting 2-D Arrays
   # Use the same syntax when splitting 2-D arrays.
   # Use the array_split() method, pass in the array you want to split and the number of splits you want to do.
   # Example:
     # Split the 2-D array into three 2-D arrays.

import numpy as np

use = np.array([[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]])
newuse = np.array_split(use, 3)
print(newuse)

# The example above returns three 2-D arrays.

# Let's look at another example, this time each element in the 2-D arrays contains 3 elements.
  # Example:
     # Split the 2-D array into three 2-D arrays.

import numpy as np

great = np.array([[1,2],[3,4],[4,5],[5,6],[6,7],[7,8]])

newgreat = np.array_split(great, 2)

print(newgreat)

# The example above returns three 2-D arrays.

# In addition, you can specify which axis you want to do the split around.
# The example below also returns three 2-D arrays, but they are split along the row (axis=1).
# Example:
   # Split the 2-D array into three 2-D arrays along rows.     [ALONG ROWS* - 'AXIS' needs to be used]

import numpy as np

yolk = np.array([[1,2,3],[2,3,4],[3,4,5],[4,5,6],[5,6,7],[6,7,8]])

newyolk = np.array_split(yolk, 3, axis = 1)

print(newyolk)

# Own note : Note the output, all first elements comes as first array in output, all second elements comes as second array in output and so on. Hence we use here 'axis' to do the same in one vertical line. 

# An alternate solution is using hsplit() opposite of hstack()
  # Example:
     # Use the hsplit() method to split the 2-D array into three 2-D arrays along rows.

import numpy as np

talk = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])
newtalk = np.hsplit(talk, 3)

print(newtalk)

# Own note: Just remembered this in 'hsplit', If we put 2 elements in one dimension, it will showing error.
# Here we put, 3 elements in one dimension, so the output will be showing without any arror. 














