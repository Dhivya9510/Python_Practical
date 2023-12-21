# Chi Square Distribution:
   # Chi Square distribution is used as a basis to verify the hypothesis.
   # It has two parameters:
        # df - (degree of freedom).
        # size - The shape of the returned array.

# Example:
    # Draw out a sample for chi squared distribution with degree of freedom 2 with size 2x3:

from numpy import random

y = random.chisquare(df=2, size=(2,3))
print(y)

# Visualization of Chi Square Distribution
   # Example:

from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

sns.distplot(random.chisquare(df=1, size=1000), hist = False)
plt.show()

# Own notes: No mean, variance or stardard deviation. As per theory, chi square test has Observed Frequency and expected frequency. 
