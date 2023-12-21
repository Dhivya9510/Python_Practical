# Machine Learning
    # Machine Learning is making the computer learn from studying data and statistics.
    # Machine Learning is a step into the direction of artificial intelligence (AI).
    # Machine Learning is a program that analyses data and learns to predict the outcome.

# Mean, Median, and Mode
   # What can we learn from looking at a group of numbers?
   # In Machine Learning (and in mathematics) there are often three values that interests us:
         # Mean - The average value
         # Median - The mid point value
         # Mode - The most common value

   # Example: We have registered the speed of 13 cars:
         # speed = [99,86,87,88,111,86,103,87,94,78,77,85,86]

     # What is the average, the middle, or the most common speed value?

# Mean
     # The mean value is the average value.
     # To calculate the mean, find the sum of all values, and divide the sum by the number of values:
            # (99+86+87+88+111+86+103+87+94+78+77+85+86) / 13 = 89.77

# Mean Example:
  # Use the NumPy mean() method to find the average speed:

import numpy

speed = [99,86,87,88,111,86,103,87,94,78,77,85,86]

x = numpy.mean(speed)
print(x)

#  Median
      # The median value is the value in the middle, after you have sorted all the values:

# Example:
    # Use the NumPy median() method to find the middle value:

import numpy

speed = [99,86,87,88,111,86,103,87,94,78,77,85,86]
y = numpy.median(speed)
print(y)

# Mode
    # The Mode value is the value that appears the most number of times:
# Example: Use the SciPy mode() method to find the number that appears the most:

from scipy import stats
speed = [99,86,87,88,111,86,103,87,94,78,77,85,86]

z = stats.mode(speed)
print(z)

# Own notes: Note that we have to declare the data type first before putting variable array. 
            # For only Mean & Median, we use Numpy. For Mode - we should use 'stats' method in 'scipy' instead 'Numpy'.


