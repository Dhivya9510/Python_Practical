# Random Numbers in NumPy:

# What is a Random Number?
  # Random number does NOT mean a different number every time. Random means something that can not be predicted logically.
  

# Pseudo Random and True Random.
  # Computers work on programs, and programs are definitive set of instructions. So it means there must be some algorithm to generate a random number as well.
  # If there is a program to generate random number it can be predicted, thus it is not truly random.
  # Random numbers generated through a generation algorithm are called pseudo random.
  # Can we make truly random numbers?
  # Yes. In order to generate a truly random number on our computers we need to get the random data from some outside source. This outside source is generally our keystrokes, mouse movements, data on network etc.
  # We do not need truly random numbers, unless its related to security (e.g. encryption keys) or the basis of application is the randomness (e.g. Digital roulette wheels).

  # In this tutorial we will be using pseudo random numbers.

# Generate Random Number
  # NumPy offers the random module to work with random numbers.
  # Example: 
    # Generate a random integer from 0 to 100:

from numpy import random

y = random.randint(100)
print(y)

# Generate Random Float
  # The random module's rand() method returns a random float between 0 and 1.
    # Example

from numpy import random
i = random.rand()
print(i)

# Own notes : If we give any other numbers in rand(), it will defaultedly considered as size. so we only have to mention it between 0&1 by putting empty brackets.

# Generate Random Array
  # In NumPy we work with arrays, and you can use the two methods from the above examples to make random arrays.

# Integers
  # The randint() method takes a size parameter where you can specify the shape of an array.
  # Example:
    # Generate a 1-D array containing 5 random integers from 0 to 100:

from numpy import random

o = random.randint(100, size=(5)) # Have to put "=" sign when giving the value size

print(o)

# Example
  # Generate a 2-D array with 3 rows, each row containing 5 random integers from 0 to 100:

from numpy import random

p = random.randint(100, size = (3,5))
print(p)

# Floats
  # The rand() method also allows you to specify the shape of the array.
  # Example:
     # Generate a 1-D array containing 5 random floats:

from numpy import random

r = random.rand(5)
print(r)

# Example
   # Generate a 2-D array with 3 rows, each row containing 5 random numbers:

from numpy import random

t = random.rand(3,5)
print(t)

# Generate Random Number From Array
  # The choice() method allows you to generate a random value based on an array of values.
  # The choice() method takes an array as a parameter and randomly returns one of the values.
  # Example
     # Return one of the values in an array:

from numpy import random

k = random.choice([1,3,5,7,9])
print(k)

# The choice() method also allows you to return an array of values.
# Add a size parameter to specify the shape of the array.
  # Example:
     # Generate a 2-D array that consists of the values in the array parameter (3, 5, 7, and 9):

from numpy import random

j = random.choice([3,5,7,9], size = (3,5))  # Here rows and columns are shuffled and output resulting as 3 rows and 5 coulmns by the values we given as argument. 

print(j)














