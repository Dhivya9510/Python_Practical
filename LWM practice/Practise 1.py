# Machine Learning:   GETTING STARTED
   # Making Computer learn from studing data and statistics. 
   # ML is a step into the direction of AI.
   # By analysing data, it can predicts the outcome. 

# Need to know what type of data we are dealing with, before we analysing it. There are 3 catogories:
   # Numerical - Numbers data that can be measured. 
       # Discrete - Limited to integers. 
       # Continuos - Infinte Value. 
   # Catagorical - Values that cannot be measured. 
   # Ordinal - Type of Catagorical but can be measured. Eg: Grade A is greater than Grade B. 

# Standard Deviation: SD is a number that describes how spread the values are. 
   # LSD - Most of the numbers are close the mean value. 
   # HSD - The values that are spread over a wider range.

# Percentiles: 
   
ages = [5,31,43,48,50,41,7,11,15,39,80,82,32,2,8,6,25,36,27,61,31]

       # What is the 75. percentile? The answer is 43, meaning that 75% of the people are 43 or younger.
       #    (Need to mention the percentage number in input)


# DD
   # Create an array containing 250 random floats between 0 and 5:

import numpy as np

d = np.random.uniform(0.0,5.0,250)
print(d)

# Create an array with 100000 random numbers, and display them using a histogram with 100 bars:

import numpy as np
import matplotlib.pyplot as plt

u = np.random.uniform(0.0,5.0,100000)

plt.hist(u,100)
plt.show()





