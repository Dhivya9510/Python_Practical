# NumPy Array Copy vs View
  
# The Difference Between Copy and View
   # The main difference between a copy and a view of an array is that the copy is a new array, and the view is just a view of the original array.
   # The copy owns the data and any changes made to the copy will not affect original array, and any changes made to the original array will not affect the copy.
   # The view does not own the data and any changes made to the view will affect the original array, and any changes made to the original array will affect the view.

# COPY:
  # Example:
     # Make a copy, change the original array, and display both arrays:

import numpy as np
golf = np.array([1,2,3,4])
newgolf = golf.copy()

golf[0] = 90

print(golf)
print(newgolf)

# The copy SHOULD NOT be affected by the changes made to the original array.

# VIEW:
  # Example:
    # Make a view, change the original array, and display both arrays:

import numpy as np
golf = np.array([1,2,3,4])
newgolff = golf.view()

golf[0] =90

print(golf)
print(newgolff)

# The view SHOULD be affected by the changes made to the original array.

# Make Changes in the VIEW:
  # Example:
     # Make a view, change the view, and display both arrays:

import numpy as np
idea = np.array([1,2,3,4])

newidea = idea.view()

newidea[0] = 20

print(idea)
print(newidea)

# The original array SHOULD be affected by the changes made to the view.

# Check if Array Owns its Data
  # As mentioned above, copies owns the data, and views does not own the data, but how can we check this?
  # Every NumPy array has the attribute base that returns None if the array owns the data.
  # Otherwise, the base  attribute refers to the original object.
  # Example:
     # Print the value of the base attribute to check if an array owns it's data or not:

import numpy as np

ideas = np.array([1,2,3,4,5])

newideas = ideas.copy()
newlyideas= ideas.view()

print(newideas.base)
print(newlyideas.base)

# Own notes:
 # View affects when changes done in original data and vise versa. 
 # Copy base always returns 'none' except the direct changes made in copy





