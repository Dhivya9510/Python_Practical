# Rounding Decimals:

  # There are primarily five ways of rounding off decimals in NumPy:
      # truncation
      # fix
      # rounding
      # floor
      # ceil


# Truncation
   # Remove the decimals, and return the float number closest to zero. Use the trunc() and fix() functions.
   # Example:
       # Truncate elements of following array:

import numpy as np

arr = np.trunc([-4.8243])
print(arr)

# or         # Both trunc() & fix() shown the same results. 

import numpy as np

arr = np.fix([-4.8243])
print(arr)

#Rounding
   # The around() function increments preceding digit or decimal by 1 if >=5 else do nothing.
   # E.g. round off to 2 decimal point, 4.37566 is 4.38
      # Example
       # Round off 3.1666 to 2 decimal places:

import numpy as np

arr = np.around(4.37566, 2)     # Note here square bracket doesn't put. only parenthesis. 
print(arr)

# Floor
   # The floor() function rounds off decimal to nearest lower integer.
   # E.g. floor of 3.166 is 3.
   # Example
       # Floor the elements of following array:

import numpy as np

arr = np.floor([-2.456])
print(arr)

# Ceil
   # The ceil() function rounds off decimal to nearest upper integer.
   # E.g. ceil of 3.166 is 4.
   # Example
      # Ceil the elements of following array:

import numpy as np

arr = np.ceil([-3.456])
print(arr)


# Own notes - Here I can see trunc() & fix() showing the same output
            # Round function, we have to put around() without square bracket by giving the number of decimal places
            # Floor function, showing results as nearest LOWER INTEGER
            # Ceil function, showing results as nearest HIGHER INTERGER.