# Percentiles
   # Percentiles are used in statistics to give you a number that describes the value that a given percent of the values are lower than.
   # Example: Let's say we have an array of the ages of all the people that live in a street.
       # ages = [5,31,43,48,50,41,7,11,15,39,80,82,32,2,8,6,25,36,27,61,31]

   # What is the 75. percentile? The answer is 43, meaning that 75% of the people are 43 or younger.
   # The NumPy module has a method for finding the specified percentile:

# Example:
    # Use the NumPy percentile() method to find the percentiles:

import numpy as np

ages = [5,31,43,48,50,41,7,11,15,39,80,82,32,2,8,6,25,36,27,61,31]

j = np.percentile(ages, 75)
print(j)

# What is the age that 90% of the people are younger than?

import numpy
ages = [5,31,43,48,50,41,7,11,15,39,80,82,32,2,8,6,25,36,27,61,31]
p = numpy.percentile(ages, 90)
print(p)


# Own notes: We have to put the percentage number (after ages, as you see in the line numbers: 16 & 23) 
        # so that it can gives you the value that indicates how many people (are/ less than) there with 90% / 75% .

