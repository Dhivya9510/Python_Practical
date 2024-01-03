# 1.4 - GENERATING POLYNOMIAL AND INTERACTION FEATURES: 

  # Load Libraries

import numpy as np 
from sklearn.preprocessing import PolynomialFeatures

  # Create Features: 

feature = np.array([[2,3],[3,4],[2,4]])

  # Create polynomial feature objects: 

polynomial_interactions = PolynomialFeatures(degree=2, include_bias= False)  
           # Here, degree parameter is 2 that means- until degree 2 is allowed. Eg: X power 1, X power 2, X1 power 1, X2 power 2. 
           # And as of now keep the 'include_bias = False' parameter.(will explain detailedly in statistics learning as per video)

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
      


            