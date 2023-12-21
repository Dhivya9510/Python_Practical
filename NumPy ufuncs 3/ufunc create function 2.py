# Create Your Own ufunc

# How To Create Your Own ufunc
  # To create your own ufunc, you have to define a function, like you do with normal functions in Python, then you add it to your NumPy ufunc library with the frompyfunc() method.
  # The frompyfunc() method takes the following arguments:
     # function - the name of the function.
     # inputs - the number of input arguments (arrays).
     # outputs - the number of output arrays.
#Example:
   # Create your own ufunc for addition:

import numpy as np

def sales (t,u):
    return t+u

o = np.frompyfunc(sales,2,1)   # Input array value and the output result array value. 
print(o([1,2,3,4],[4,5,6,7]))  # Memorize and understood the format. 

# Check if a Function is a ufunc
  # Check the type of a function to check if it is a ufunc or not.
  # A ufunc should return <class 'numpy.ufunc'>.

# Example
  # Check if a function is a ufunc:

print(type(np.add))

# If it is not a ufunc, it will return another type, like this built-in NumPy function for joining two or more arrays:
# Example
  # Check the type of another function: concatenate():

print(type(np.concatenate))

# If the function is not recognized at all, it will return an error:
# Example:
   # Check the type of something that does not exist. This will produce an error:

  # print(type(np.blueblue))   # This code showing error hence commented it. 

# To test if the function is a ufunc in an if statement, use the numpy.ufunc value (or np.ufunc if you use np as an alias for numpy):
# Example:
  # Use an if statement to check if the function is a ufunc or not:

if type(np.add) == np.ufunc:
    print("Yes it is ufunc")
else:
    print("This is not ufunc")



# Today seen ufunc intro and ufunc create functions, the below are the summary by understanding. 

  # ufunc is an Universal function that implements vectorization that makes computation much faster to iterating the elements. 
  # "np.add" is an ufunc 
  # To add array items, "zip()"" is used in python without ufunc 
  # And "np.add" with ufunc.
  # "frompyfunct()" with arguments - functions, input and output. 






