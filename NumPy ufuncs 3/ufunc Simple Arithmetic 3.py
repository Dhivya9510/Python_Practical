# Simple Arithmetic:

# Simple Arithmetic
  # You could use arithmetic operators + - * / directly between NumPy arrays, but this section discusses an extension of the same where we have functions that can take any array-like objects e.g. lists, tuples etc. and perform arithmetic conditionally.

# Note: Arithmetic Conditionally: means that we can define conditions where the arithmetic operation should happen.

# All of the discussed arithmetic functions take a where parameter in which we can specify that condition.

# Addition
  # The add() function sums the content of two arrays, and return the results in a new array.
  # Example:
     # Add the values in arr1 to the values in arr2:

import numpy as np
arr1 = np.array([2,4,6,8,10])
arr2 = np.array([3,6,9,12,15])

new_arr = np.add(arr1,arr2)
print(new_arr)

# Subtraction
  # The subtract() function subtracts the values from one array with the values from another array, and return the results in a new array.
  # Example
    # Subtract the values in arr2 from the values in arr1:

import numpy as np

arr1= np.array([10,20,30,40,50])
arr2 = np.array([5,10,15,20,30])

newarr = np.subtract(arr1,arr2)

print(newarr)


# Multiplication
  # The multiply() function multiplies the values from one array with the values from another array, and return the results in a new array.
  # Example
     # Multiply the values in arr1 with the values in arr2:

import numpy as np

arr1 = np.array([2,4,6,8,10])
arr2 = np.array([2,4,2,4,2])

arr3 = np.multiply(arr1,arr2)
print(arr3)

# Division
  # The divide() function divides the values from one array with the values from another array, and return the results in a new array.
  # Example
    # Divide the values in arr1 with the values in arr2:

import numpy as np

arr1 = np.array([9,4,16,20,12])
arr2 = np.array([3,2,4,5,6])

newoutput = np.divide(arr1,arr2)
print(newoutput)

# Power
  # The power() function rises the values from the first array to the power of the values of the second array, and return the results in a new array.
  # Example
     # Raise the values in arr1 to the power of values in arr2:

import numpy as np

arr1 = np.array([3,4,5,6,2])
arr2 = np.array([2,3,2,3,1])
arr33= np.power(arr1,arr2)
print(arr33)

# Remainder
   # Both the mod() and the remainder() functions return the remainder of the values in the first array corresponding to the values in the second array, and return the results in a new array.
   # Example
     # Return the remainders:

import numpy as np

arr1 = np.array([10,15,16,17,18])
arr2 = np.array([3,4,5,6,7])

resultarr = np.mod(arr1,arr2)
print(resultarr)

# or                  - both remainder() &  mod() given the same output. 

import numpy as np

arr1 = np.array([10,15,16,17,18])
arr2 = np.array([3,4,5,6,7])

resultarr = np.remainder(arr1,arr2)
print(resultarr)

# Quotient and Mod
  # The divmod() function return both the quotient and the the mod. The return value is two arrays, the first array contains the quotient and second array contains the mod.
  # Example
    # Return the quotient and mod:

import numpy as np

arr1 = np.array([10,15,16,17,18])
arr2 = np.array([3,4,5,6,7])

resultarr = np.divmod(arr1,arr2)
print(resultarr)


# Absolute Values
   # Both the absolute() and the abs() functions do the same absolute operation element-wise but we should use absolute() to avoid confusion with python's inbuilt math.abs()
   # Example
      # Return the quotient and mod:

# note the question above.

import numpy as np

arr1 = np.array([-1,1,-2,-3,-4])

newarr = np.absolute(arr1)
print(newarr)

