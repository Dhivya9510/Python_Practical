# NumPy Joining Array

# Joining NumPy Arrays
  # Joining means putting contents of two or more arrays in a single array.
  # In SQL we join tables based on a key, whereas in NumPy we join arrays by axes.
  # We pass a sequence of arrays that we want to join to the concatenate() function, along with the axis. If axis is not explicitly passed, it is taken as 0.
  # Example:
    # Join two arrays

import numpy as np

tool1 = np.array([1,2,3])
tool2 = np.array([4,5,6])

tool = np.concatenate((tool1,tool2))  #Note:  We need to put the joining variable in one whole bracket. See here there are two brackets.  
print(tool)

# Example
  # Join two 2-D arrays along rows (axis=1):

import numpy as np

tell1 = np.array([[1,2,3],[4,5,6]])
tell2 = np.array([[7,8,9],[5,7,2]])

tell = np.concatenate((tell1,tell2), axis = 1)
print(tell)       # Note: The output will be showing as column wise. You know why? Just think the output of simple 2D array. 

# Joining Arrays Using Stack Functions
  # Stacking is same as concatenation, the only difference is that stacking is done along a new axis.
  # We can concatenate two 1-D arrays along the second axis which would result in putting them one over the other, ie. stacking.
  # We pass a sequence of arrays that we want to join to the stack() method along with the axis. If axis is not explicitly passed it is taken as 0.
  # Example

import numpy as np

yolk1 = np.array([1,2,3])
yolk2 = np.array([5,6,7])

yolk = np.stack((yolk1,yolk2), axis = 1)
print(yolk)


# Stacking Along Rows
   # NumPy provides a helper function: hstack() to stack along rows.
   # Example

import numpy as np

unit1 = np.array([1,2,3,4])
unit2 = np.array([5,6,7,8])

unit = np.hstack((unit1,unit2))
print(unit)

# Stacking Along Columns
  # NumPy provides a helper function: vstack()  to stack along columns.
  # Example

import numpy as np

unit1 = np.array([1,2,3,4])
unit2 = np.array([5,6,7,8])

unit = np.vstack((unit1,unit2))
print(unit)

# Stacking Along Height (depth)
  # NumPy provides a helper function: dstack() to stack along height, which is the same as depth.
  # Example

import numpy as np

unit1 = np.array([1,2,3])
unit2 = np.array([5,6,7])

unit = np.dstack((unit1,unit2))
print(unit)

# Own note: In concatenate, for 1D array - there is a simple joining in one line without any axis. 
          # In concatenate, for 2D arrays - there is a simple 2D joining WITH AXIS. 
          # In Stack, for 1D array - there is a column wise 2D looking joining with axis. 
          # In hstack(), for 1D -  every elements comes in one line. Here there is no need to put axis. 
          # In vstack(), for 1D -  there is a column wise 2D looking joining. Here there is no need to put axis. 
          # In dstack(), for 1D -  there is a column wise 2D looking joining without axis but also inculdes stack(), means that there is one more square bracket in output. 

 



