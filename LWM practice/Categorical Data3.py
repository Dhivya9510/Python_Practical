# IMPUTING MISSING CLASS VALUES: 

# This is almost little advanced for beginners, however in practise - it will be easy. 
# Impute is nothing but how to input new values in the place of missing categorical data. 
# The ML strategy used for this is known as ‘KNeighborsClassifier’. 

# Load Libraries
import numpy as np
from sklearn.neighbors import KNeighborsClassifier # used to impute the missing categorical data. 

# Create a feature matrix in the categorical feature. 
X = np.array([[0, 2.10,1.45],[1, 1.18,1.33],[0, 1.22,1.27],[1, -0.21,-1.19]])

# Create a feature matrix with missing values in the categorical feature. 
X_with_nan = np.array([[np.nan,0.87,1.31],[np.nan,-0.67,-0.22]])

# Train KNN Learner 
App = KNeighborsClassifier(3, weights= 'distance') # Mostly '3' used by default, 'distance' is the target that we are going to find out. 
trained_model = App.fit(X[:,1:],X[:,0])

# Predit missing value's class:
imputed_values = trained_model.predict(X_with_nan[:,1:])
print(imputed_values)

# So the result would be showing as [0. 1.]  - we need to bring the output in to the matrix -for that we need to write 'reshape' function. 

