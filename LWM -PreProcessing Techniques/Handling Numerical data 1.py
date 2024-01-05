# Introduction: 
  
   # Quantitative data is the measurement of something – whether class size, monthly sales or student’s scores. 
   # The natural way to represent these quantities is numerically (eg: 29 Students, $2345.00 Sales). 
   # In this chapter, we will cover numerous STRATERGIES FOR TRANSFORMING RAW NUMERICAL DATA IN TO FEATURES PURPOSE-BUILT FOR ML ALGORITHYMS. 

# 1.1 RESCALING A FEATURE: (from raw numerical data to feature rescaling)

     # Use scikit-learn's MinMaxScalar to rescale the feature array: 
     # Import the libraries first. 

import numpy as np
import pandas as pd

from sklearn import preprocessing   # Because Rescaling is a common preprocessing task in ML. 

     # Create Feature: (on your own data)

feature = np.array([[-500.5],[-100.1],[0],[100.1],[900.9]])

    # Create scalar: 

minmax_scale = preprocessing.MinMaxScaler(feature_range=(0,1))

     # Scale feature: 

scaled_feature = minmax_scale.fit_transform(feature)
print(scaled_feature)

# 1.2 STANDARDIZING A FEATURE: 
   # You want to transform a feature to have a mean 0 & SD of 1. Scikit-learn’s STANDARDSCALAR perform both transformations. 
   # Create Feature

Feature = np.array([[-1000.1],[-200.2],[500.5],[600.6],[9000.9]])

   # Create Scalar
standard_scale = preprocessing.StandardScaler()

   # Transform the feature: 

standardized_scalar= standard_scale.fit_transform(Feature)
print(standardized_scalar)
  

# Print mean & SD. 

print("Mean:", round(standardized_scalar.mean()))
print("Standard_Deviation:", standardized_scalar.std())

       # If our data has significant outliars, it can negatively impact our standardization by affecting the feature’s mean & variance. 
       # In this scenario, it is often helpful - instead rescale the feature using the median & quartile range. 
       # In Scikit learn, we do this using the Robust scalar method. 

   # Create Feature (already created last above one)
   # Create Scalar

robust_scalar = preprocessing.RobustScaler()

   # Transform feature. 

Robust_feature = robust_scalar.fit_transform(Feature)     

# 1.3 NORMALIZING OBSERVATION: 

      # You want to rescale the feature values of observations to have unit norm (a total length of 1). 
      # Use Normalizer with a norm argument 
      # Load Libraries

from sklearn.preprocessing import Normalizer

      # Create Feature Matrix

Feature_matrix = np.array([[0.5,0.5],[1.1,3.4],[1.5,20.2],[1.63,34.4],[10.9,3.3]])

      # Create Normalizer

normalizer = Normalizer(norm= "l2")

      # Transform feature matrix: 

features_matrix= normalizer.transform(Feature_matrix)  # Note here no 'fit_transform', only 'transform'.
print(features_matrix)

     # Transforming feature matrix in Euclidean norm (i.e: L2)

Feature_l2_norm = Normalizer(norm="l2").transform(Feature)
print(Feature_l2_norm)

     # Alternatively we can specify MANHATTAN norm (i.e: L1)

Feature_l1_norm = Normalizer(norm="l1").transform(Feature)
print(Feature_l1_norm)
 
     # Check by showing the adding value output is 1 as unit no
print("Sum of first observation/s value:", Feature_l1_norm[0,0] + Feature_l1_norm[0,1]) # type:ignore





























# Some General Notes: 

 	# This Standardizing feature is the one that mostly used Algorithm called PCA (Principal compound Analysis) used in ML. 
 	# Outliars generally affects Mean & Variance (i.e also SD). 
 	# There is a term called ‘Robust Scalar’ – Instead find Mean & Variance. It involves Median and Quartile range. 
   # 'MinMax Scale’ is mostly used in ‘Neural Network’ ~ which was discovered after ML – for accuracy and improvement
   # Normalizing is usually used in ‘Text Classification’ & NLP. 
   # Note here in 'Normalizing' - feature elements are not single. It should have two elements in the list. 
   # In video -It has been said that 'l2' is something that obtained from a formula (refer MS-Word notes)
   # One more term was shared in video that 'Euclidean Distance' which related to 'L2'