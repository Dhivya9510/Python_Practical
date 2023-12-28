# Introduction: 
  
   # Quantitative data is the measurement of something – whether class size, monthly sales or student’s scores. 
   # The natural way to represent these quantities is numerically (eg: 29 Students, $2345.00 Sales). 
   # In this chapter, we will cover numerous STRATERGIES FOR TRANSFORMING RAW NUMERICAL DATA IN TO FEATURES PURPOSE-BUILT FOR ML ALGORITHYMS. 

# RESCALING A FEATURE: 

     # Use scikit-learn's MinMaxScalar to rescale the feature array: 
     # Import the libraries first. 

import numpy as np
import pandas as pd

from sklearn import preprocessing

     # Create Feature: (on your own data)

feature = np.array([[-500.5],[-100.1],[0],[100.1],[900.9]])

    # Create scalar: 

minmax_scale = preprocessing.MinMaxScaler(feature_range=(0,1))

     # Scale feature: 

scaled_feature = minmax_scale.fit_transform(feature)
print(scaled_feature)

# STANDARDIZING A FEATURE: 
   # You want to transform a feature to have a mean 0 & SD of 1. Scikit-learn’s STANDARDSCALAR perform both transformations. 
   # Create Feature

Feature = np.array([[-1000.1],[-200.2],[500.5],[600.6],[9000.9]])

   # Create Scalar
standard_scale = preprocessing.StandardScaler()

   # Transform the feature: 

standardized = standard_scale.fit_transform(Feature)
print(standardized)