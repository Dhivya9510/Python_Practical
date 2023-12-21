# Trigonometric Functions
  # NumPy provides the ufuncs sin(), cos() and tan() that take values in radians and produce the corresponding sin, cos and tan values.
  # Example:
     # Find sine value of PI/2:

import numpy as np

p = np.sin(np.pi/2)
print(p)

# Example
  # Find sine values for all of the values in arr:

import numpy as np

arr = np.array([np.pi/2, np.pi/3, np.pi/4])   #Notr here np.pi/2, np.pi/3 and so on in an array

p = np.sin(arr)
print(p)

# Convert Degrees Into Radians
  # By default all of the trigonometric functions take radians as parameters but we can convert radians to degrees and vice versa as well in NumPy.
# Note: radians values are pi/180 * degree_values.

# Example:
   # Convert all of the values in following array arr to radians:

import numpy as np

u = np.array([90,45,180,360])       # These are all degrees in an angle that you convert to radians.So degree to radians

pit = np.deg2rad(u)
print(pit)

# Radians to Degrees
  # Example:
     # Convert all of the values in following array arr to degrees:

import numpy as np

arr = np.array([np.pi/2, np.pi, 1.5*np.pi, 2*np.pi])   # Here note that pi/2 = 1, so 1st one is pi/2 i.e half, then pi only, than its's increased by 0.5.
uiy = np.rad2deg(arr)
print(uiy)

# Check below with the radians inside the bracket by matching the own notes to convert those into degrees.
import numpy as np

yol = np.rad2deg(2*np.pi)
print(yol)


# Finding Angles
  # Finding angles from values of sine, cos, tan. E.g. sin, cos and tan inverse (arcsin, arccos, arctan).
  # NumPy provides ufuncs arcsin(), arccos() and arctan() that produce radian values for corresponding sin, cos and tan values given.
  # Example:
     # Find the angle of 1.0:

import numpy as np

t = np.arcsin(1.0)
print(t)

# Angles of Each Value in Arrays
  # Example:
    # Find the angle for all of the sine values in the array

import numpy as np

array = np.array([1,-1,-0.1])   # So as per the example question, these are all the values of sin, cos and tan each.

t = np.arcsin(array)
print(t)

# Hypotenues
   # Finding hypotenues using pythagoras theorem in NumPy.
   # NumPy provides the hypot() function that takes the base and perpendicular values and produces hypotenues based on pythagoras theorem.
   # Example:
      # Find the hypotenues for 4 base and 3 perpendicular:

import numpy as np

base = 4               # So note that we need to code the values seperately before put into function.
perp = 3

hit = np.hypot(base,perp)
print(hit)


# Own notes : radian = np.pi/2 = 1.0 that is 90 degree, np.pi = 180 degree, 1.5*np.pi = 270 degree & 2*np.pi = 360 degree
            # Note: radians values are pi/180 * degree_values.  (Not worked yet)
            # arcsin(1.0) resulting decimal places of 1.
            # arccos(1.0) resulting exact 0
            # arctan(1.0) resulting less than 1
            # By the given values of sin, cos & tan, arcsin(), arccos() & arctan() produces the radian value. 
            # As per my understanding, Hypotenues - hypot() contains the parameters such as base and perpendicular based on PYTHAGORAS THEORM