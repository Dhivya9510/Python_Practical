# NumPy GCD Greatest Common Denominator

# Finding GCD (Greatest Common Denominator)
  # The GCD (Greatest Common Denominator), also known as HCF (Highest Common Factor) is the biggest number that is a common factor of both of the numbers.
  # Example:
    # Find the HCF of the following two numbers:

import numpy as np

num1 = 4
num2 = 8

u = np.gcd(num1,num2)
print(u)

# Returns: 4 because that is the highest number both numbers can be divided by (4/4 = 1, 8/4 = 2).

# Finding GCD in Arrays
  # To find the Highest Common Factor of all values in an array, you can use the reduce() method.
  # The reduce() method will use the ufunc, in this case the gcd() function, on each element, and reduce the array by one dimension.
  # Example
     # Find the GCD for all of the numbers in the following array:

import numpy as np

num = np.array([20, 8, 32, 36, 16])

p = np.gcd.reduce(num)
print(p)

# Returns: 4 because that is the highest number all values can be divided by.

 # Own notes : LCM is the lowest number that can be multiplied all the given numbers
              # GCD is the highest number that can be multiplied all the given numbers.

