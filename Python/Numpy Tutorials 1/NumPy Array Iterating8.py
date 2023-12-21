# NumPy Array Iterating
 
  # Iterating Arrays
    # Iterating means going through elements one by one.
    # As we deal with multi-dimensional arrays in numpy, we can do this using basic for loop of python.
    # If we iterate on a 1-D array it will go through each element one by one.
    # Example:
       # Iterate on the elements of the following 1-D array:

import numpy as np

car = np.array([1,2,3,4,5])

for x in car:                     # Own notes: use 'for' loop when the array come to iteration.
    print(x)

# Iterating 2-D Arrays
  # In a 2-D array it will go through all the rows.
  # Example:
      # Iterate on the elements of the following 2-D array:

import numpy as np

car = np.array([[1,2,3],[4,5,6]])

for x in car:
    print(x)

# If we iterate on a n-D array it will go through n-1th dimension one by one.
  
# To return the actual values, the scalars, we have to iterate the arrays in each dimension.
# Example:
   # Iterate on each scalar element of the 2-D array:

import numpy as np

car = np.array([[1,2,3],[4,5,6]])  #Own notes: Iterate each scalar elements in the sense, we have to 'for' loop for each dimension.
for x in car:
    for y in x:
        print(y)

# Iterating 3-D Arrays
  # In a 3-D array it will go through all the 2-D arrays.
  # Example:
    # Iterate on the elements of the following 3-D array:

import numpy as np

held = np.array([[[1,2,3],[4,5,6]],[[6,7,8],[9,0,1]]])

for x in held:
    print(x)           # Own notes: It's 3D, so the output will be like 2D

# To return the actual values, the scalars, we have to iterate the arrays in each dimension.
 # Example:
    # Iterate down to the scalars:

import numpy as np

held = np.array([[[1,2,3],[4,5,6]],[[6,7,8],[9,0,1]]])

for x in held:
    for y in x:
        for z in y:
            print(z)   # Own notes: It is the example of the scalar iteration of 3D.
                       # Scalar means output value shown as one by one. 

# Iterating Arrays Using nditer()
 # The function nditer() is a helping function that can be used from very basic to very advanced iterations. It solves some basic issues which we face in iteration, lets go through it with examples.

# Iterating on Each Scalar Element
  # In basic for loops, iterating through each scalar of an array we need to use n for loops which can be difficult to write for arrays with very high dimensionality.
  # Example:
     # Iterate through the following 3-D array:

import numpy as np

held = np.array([[[1,2,3],[4,5,6]],[[6,7,8],[9,0,1]]])

for x in np.nditer(held):
    print(x)                   # Own notes: In scalar iteration, we have to write 'for' loops for every scalars, instead we can write one 'for' loop by putting 'nditer' funtion. 
                               # And please note the format - pre-near 'nditer' we have to  put np and in bracket, we need to put the variable. 
   
# Iterating Array With Different Data Types
  # We can use op_dtypes argument and pass it the expected datatype to change the datatype of elements while iterating.
  # NumPy does not change the data type of the element in-place (where the element is in array) so it needs some other space to perform this action, that extra space is called buffer, and in order to enable it in nditer() we pass flags=['buffered'].
  # Example:
     # Iterate through the array as a string:

import numpy as np

yolk = np.array([[1,2,3],[4,5,6]])

for x in np.nditer(yolk, flags = ["buffered"], op_dtypes = ["S"]):
    print(x)
    
# Own notes:  To iterate the values one by one in 3D, we generally include 'for' loops in scalar format. Instead we use 'nditer' followed by np with variable in bracket. 
            # In Numpy, to change the data type (here, from integer to string), we use 'op_datatypes' along with  'flags = ["buffered"]' (this is reffered some space to perform the changing datatype function while iterating it)
            # " flags = ["buffered"], op_dtypes = [ ] " only coming when we use np.nditer funtion so far I noted.

# Iterating With Different Step Size
  # We can use filtering and followed by iteration.
  # Example: 
     # Iterate through every scalar element of the 2D array skipping 1 element:

import numpy as np

think = np.array([[1,2,3,4],[5,6,7,8]])

for x in np.nditer(think[:, ::2]):
    print(x)


# Enumerated Iteration Using ndenumerate()
  # Enumeration means mentioning sequence number of somethings one by one.
  # Sometimes we require corresponding index of the element while iterating, the ndenumerate() method can be used for those usecases.
  # Example:
    # Enumerate on following 1D arrays elements:

import numpy as np

calls = np.array([1,2,3,4])

for idx, x in np.ndenumerate(calls):
    print(idx, x)

# Own note: ndenumerate is generally to show the one by one elements along with idx i.e: index. 
          # Both idx & x needs to be put after printing that. 

# Example
  # Enumerate on following 2D array's elements:

import numpy as np

calls = np.array([[1,2,3],[4,5,6]])

for idx, x in np.ndenumerate(calls):
    print(idx, x)



# Own notes : Understand the example question first so that you can do the code to get the desired output. 
             # Here, Enumerate means output needs to shown as one by one elements. 'nditer' means looping only but in one function instead of putting many for loops. 
             # op_datatypes means changing the datatype with nditer importantly with 'flags = ["buffered"]' 
             # ndenumerate with idx means output resulting one by one elements along with it's index. 


            








