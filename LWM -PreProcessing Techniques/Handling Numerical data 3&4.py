# 1.6 HANDLING OUTLIERS:  
         
       # Typically we have 3 stratergies we can use to handle outliers. 
       # First, we drop them. 

   # Load Libraries:
import pandas as pd 

   # Create Dataframe:

houses = pd.DataFrame()
houses["Price"] = [534433, 392333, 293222, 4322032]
houses["Bathrooms"] = [2, 3.5, 2, 116]
houses["Square_feet"] = [1500, 2500, 1500, 48000]

   # Filter observations: 

first = houses[houses["Bathrooms"] < 5]
print(first)

        # Second, we can mark them as outliers and include it as a feature: 

   # Load Libraries:
import numpy as np 

   # Create feature based on boolean condition: (like directly applied filtered observations here with boolean condition)

houses["outlier"] = np.where(houses["Bathrooms"] < 5, 0, 1)   # Not a list bracket but a normal bracket. 
print(houses["outlier"])

        # Finally, we can transform the feature to dampen the effect of the outlier. 

houses["log_of_square_feet"] = [np.log(x) for x in houses["Square_feet"]]   # Format for log to detect the outliers. 
print(houses["log_of_square_feet"])


# 1.7 DISCRETIZATING FEATURES: 

     # Depending on how we want to break up the data, there are 2 techniques we can use. 
# First, we can binarize the feature according to some threshold. 
     # ('Threshold' means - we can limit the data up to some level, if in case it may go up beyond our setting limit - it will reflect in output)


  # Load Libraries
import numpy as np
from sklearn.preprocessing import Binarizer

  # Create Feature: 

age = np.array([[6],[12],[20],[36],[65]])

  # Create Binarizer:

binarizer = Binarizer(18)     # type: ignore
                  # We set 18 as Threshold (setting a limit), the first two are below 18, so the output will be 0, but the last three are above 18, so the output will be showing as 1. 

  # Transform the feature:

hey = binarizer.fit_transform(age)
print(hey)

# Second, we can break up numerical features according to multiple thresholds. 

   # Bin feature (1):

goat = np.digitize(age, bins=[20,30,64])
print(goat)

    # Bin feature (2):

hen = np.digitize(age, bins=[20,30,64], right= True)  # type: ignore
print(hen)


# 1.8 GROUPING OBSERVATIONS USING CLUSTERING: 3:23
  
      # Load Libraries

import pandas as pd
from sklearn.datasets import make_blobs
from sklearn.cluster import KMeans

      # Make simulated feature matrix:
features = make_blobs(n_samples= 50, n_features= 2, centers= 1, random_state=1)

      # Create dataframe:

df = pd.DataFrame(features, columns= ["features_1", "features_2"])

      # Make K-Means clusterer:

clusterer = KMeans(3, random_state=0)

      # Fit clusterer:

fit_clusterer = clusterer.fit(features)

      # Predict values:

df["group"]= clusterer.predict(features)

      # View first few observations: 

hat = df.head()
print(hat)

# 1.9 DELETING OBSERVATIONS WITH MISSING VALUES: 

      # You need to delete observations containing missing values: 









# Own notes: 
  # Handling Outliers: 
     # Fist method:      In 'Pandas', Just using '<' operator.
     # Second method:    In 'Numpy', Just using '<' operator but with 'where' method along with boolean condition. 
     # Final method:     Using 'dampen' - nothing but the 'log' feature. (like List comprehension)

  # Discretizating Features: 
     #  Binarizer – 
        # Means we can binarize the feature according to some threshold. 
        # Clearly, we can limit the data up to some level, if in case it may go up beyond our setting limit – it will reflect in output.

     # Digitize – 
        # Here we can set multiple thresholds by putting the parameter ‘bins’. 
        # If we add one more parameter ‘right = True’ (note by default the ‘right’ parameter is in ‘False’), it excludes the bin value given and move to the next numerical number after that.

     # Note that 'np.digitize', but not 'np.binarize' that only given as 'binarize' without np. 
 