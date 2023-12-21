# NumPy Hyperbolic Functions

# Hyperbolic Functions
    # NumPy provides the ufuncs sinh(), cosh() and tanh() that take values in radians and produce the corresponding sinh, cosh and tanh values..
# Example: 
   # Find sinh value of PI/2:

import numpy as np

e = np.sinh(np.pi/2)
print(e)

# Example
  # Find cosh values for all of the values in arr:

import numpy as np

arr = np.array([np.pi/2, np.pi/3, np.pi/4, np.pi/5])

y = np.cosh(arr)
print(y)

# Finding Angles
  # Finding angles from values of hyperbolic sine, cos, tan. E.g. sinh, cosh and tanh inverse (arcsinh, arccosh, arctanh).
  # Numpy provides ufuncs arcsinh(), arccosh() and arctanh() that produce radian values for corresponding sinh, cosh and tanh values given.

# Example:
   # Find the angle of 1.0:

import numpy as np

u = np.arcsinh(1.0)
print(u)

# Angles of Each Value in Arrays
  # Example
     # Find the angle for all of the tanh values in array:

import numpy as np

arr1 = np.array([0.1,0.2,0.3])             # Note these are the kinds TANH() values. In Trignometry, SIN() values kinda 1,-1,0.1..
i = np.arctanh(arr1)
print(i)



# Own notes: # Note the kinds TANH() values. In Trignometry, SIN() values kinda 1,-1,0.1..