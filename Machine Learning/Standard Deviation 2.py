# What is Standard Deviation?
    # Standard deviation is a number that describes how spread out the values are.
    # A low standard deviation means that most of the numbers are close to the mean (average) value.
    # A high standard deviation means that the values are spread out over a wider range.

    # Example: This time we have registered the speed of 7 cars:
             # speed = [86,87,88,86,87,85,86]

# STANDARD DEVIATION CALCULATOR
 
   # Sum of speed = 605 whereas count is 7, so mean (average value) is 86.42. SD calculated as:
   # To find Difference, Subract (the original array value - mean value) , you will get - (-0.42,0.58,1.58,-0.42,0.58,-1.42,-0.42)
   # Find Square of each Difference now - (0.1764,0.3364,2.4964,0.1764,0.3364,2.0164,0.1764) = Sum = 5.7024
   # Find Variance now = 5.7024/7 = 0.815
   # Square root of the Variance is SD. So, the answer would be 0.9. 

import numpy 

speed = [86,87,88,86,87,85,86]

u = numpy.std(speed)
print(u)

# Another example:
  # Speed = [32,111,138,28,59,77,97]

   # Sum of speed = 542 whereas count is 7, so mean (average value) is 77.42. SD calculated as:
   # To find Difference, Subract (the original array value - mean value) , you will get - (-45.42,33.58,60.58,-49.42,-18.42,-0.42,19.58)
   # Find Square of each Difference now - (2062.97,1127.61,3669.93,2440.36,339.29,0.1764,383.37) = Sum = 10025.71429
   # Find Variance now = 10025.71429/7 = 1432.244
   # Square root of the Variance is SD. So, the answer would be 37.84 

import numpy
speed = [32,111,138,28,59,77,97]

i = numpy.std(speed)
print(i)

# Variance
    # Variance is another number that indicates how spread out the values are.
    # In fact, if you take the square root of the variance, you get the standard deviation!
    # Or the other way around, if you multiply the standard deviation by itself, you get the variance!

# Use the NumPy var() method to find the variance:

import numpy 
Speed = [32,111,138,28,59,77,97]
o = numpy.var(speed)
print(o)

# Use the NumPy std() method to find the standard deviation:

import numpy 
Speed = [32,111,138,28,59,77,97]
o = numpy.std(speed)
print(o)

# Symbols
   # Standard Deviation is often represented by the symbol Sigma: σ
   # Variance is often represented by the symbol Sigma Squared: σ2


# Own notes: Understand the calculation method of Variance to find out the Standard Deviation 
           # Another name of SD is sigma. 

