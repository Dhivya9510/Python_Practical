# 1.4 - GENERATING POLYNOMIAL AND INTERACTION FEATURES: 

  # Load Libraries

import numpy as np 
import pandas as pd
from sklearn.preprocessing import PolynomialFeatures

  # Create Features: 

feature = np.array([[2,3],[3,4],[2,4]])

  # Create polynomial feature objects: 

polynomial_interactions = PolynomialFeatures(degree=2, include_bias= False)  
           # Here, degree parameter is 2 that means- until degree 2 is allowed. Eg: X power 1, X power 2, X1 power 1, X2 power 2. 
           # And as of now keep the 'include_bias = False' parameter by default. (will explain detailedly in statistics learning as per video)

   # Create polynomial feature: 
polynomial_feature = polynomial_interactions.fit_transform(feature)
print(polynomial_feature)

           # Note output will be first two numbers, then square root of 1st number, multiplication of 1&2 numbers, then square root of 2nd number. 
           # We can restrict the features created to only interaction by setting 'Interaction_only' to 'True'.
           # Meaning that the output only do interact function that is multiplication , not doing square roots. 
           

polynomial_interactions = PolynomialFeatures(degree=2, include_bias= False, interaction_only= True)
p_i = polynomial_interactions.fit_transform(feature)
print(p_i)
  
# 1.5 TRANSFORMING FEATURES: 

      # Load Libraries: 

from sklearn.preprocessing import FunctionTransformer

      # Create Feature Matrix: (Already created above)
     
      # Define a simple function: 

def add_ten(x):
    return x + 10

      # Create transformer

ten_transformer = FunctionTransformer(add_ten)

      # Transform Feature matrix:

transformer = ten_transformer.transform(feature)  # Note here only have to put 'transform' but not 'fit_transform'.
print(transformer)     

      # Same thing we might see before in pandas as below fyr: 

trnsfrmr = pd.DataFrame(feature, columns= ["feature_1", "feature_2"])
    
      # Apply function: 

pd_trnsfrmr = trnsfrmr.apply(add_ten)
print(pd_trnsfrmr)

# 1.5 DETECTING OUTLIARS: 

       #  Method ‘ EllipticEnvelope’ is used to detect ‘Outliars’.
       # ‘Contamination’ is one of the most important parameter in ‘EllipticEnvelope’ method. 

       # Load libraries: 

from sklearn.covariance import EllipticEnvelope      # Note here no 'preprocessing' but 'covariance'
from sklearn.datasets import make_blobs              # This is to help generating datasets by the method 'make_blobs' - creating data like 2d matrix (as of my understanding)

       # Create simulated data:

features = make_blobs(n_samples= 10, n_features= 2, centers= 1, random_state= 1)
print(features)

        # Replace the first observation's values with the extreme values

features[0,0] = 10000  # type: ignore
features[0,1] = 10000  # type: ignore

outliar_detector = EllipticEnvelope(contamination= .1)

       # Fit detector:

fit_detector = outliar_detector.fit(features)  # type: ignore

       # Predict detector: 

predict_detector = outliar_detector.predict(features)  #type: ignore

            # If outliers are less in number and we have been informed about it already, it will be easy for us and we can use this 'EllipticEnvelope' method. 
            # But what if the outliers are more in number and we did not even informed about it? 
            # So, in Statistics - we use the method called 'Inter-Quartile range'. 
            # Inter quartile range is one of the mathematical operations using percentiles. 
            # For detailed explanation - go through the screenshot of the notes in MS-word. 
            
# Inter Quartile Range: 

           # Create Feature. (already created above using 'make_blobs')
           # Create a function to return index of outliers.
           # ‘Percentile’ is generally used in ‘Inter-Quartile range’ 
     

def indices_of_outliers(y):
    q1,q3 = np.percentile(y, [25,75])  # type: ignore
    iqr = q3 - q1
    lower_bound = q1 - (iqr * 1.5)
    upper_bound = q3 + (iqr * 1.5)
    return np.where ((y > lower_bound) | (y< upper_bound))  # This is the set of format for Inter-quartile range that explained in the video. 

           # Run function: 

Int_Quar = indices_of_outliers(features)
print(Int_Quar)




    


            