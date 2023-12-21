# Normal Data Distribution
    # In the previous chapter we learned how to create a completely random array, of a given size, and between two given values.
    # In this chapter we will learn how to create an array where the values are concentrated around a given value.
    # In probability theory this kind of data distribution is known as the normal data distribution, or the Gaussian data distribution, after the mathematician Carl Friedrich Gauss who came up with the formula of this data distribution.

# Example:
    # A typical normal data distribution:

import numpy
import matplotlib.pyplot as plt

r = numpy.random.normal(5.0,1.0,100000)
plt.hist(r,100)
plt.show()

# Histogram Explained
     # We use the array from the numpy.random.normal() method, with 100000 values,  to draw a histogram with 100 bars.
     # We specify that the mean value is 5.0, and the standard deviation is 1.0.
     # Meaning that the values should be concentrated around 5.0, and rarely further away than 1.0 from the mean.
     # And as you can see from the histogram, most values are between 4.0 and 6.0, with a top at approximately 5.0.

# Own notes: Note the question that it's a 'NORMAL DATA DISTRIBUTION'. 
          # In Normal data distribution, the two given values would be Mean, SD & the size. 
          # As usual, we have to mention the count (number of bars we needed - see line 13)
          # Normal data distribution is otherwise known as Gaussian data distribution and it's shape is like BELL-CURVED
          # See that the histo graph's mid max bell curve would be mean value. 