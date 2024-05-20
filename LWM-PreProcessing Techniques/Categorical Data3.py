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

# So the result would be showing as [0. 1.]  - we need to bring the output in to a matrix -for that we need to write 'reshape' function. 

ball = imputed_values.reshape(-1,1)
print(ball)

# Now we need to join this imputed values into our feature matrix. So that we used 'HSTACK' & 'VSTACK'.
# Before doing that we need to understand what is Hstack and what is Vstack.

# An alternative solution is to fill in missing values with the feature’s most frequent value: 

a = np.ones((3,3))
print(a)
Cat = np.vstack((a, np.array((2,2,2))))
print(Cat)

# Therefore we done with vertical stack.
# Adding a column requires a bit more work. However, you can't use 'np.hstack' directly.

b = np.ones((3,3))
c = np.array((2,2,2)).reshape(3,1)
dog = np.hstack((b,c))
print(dog)

# Note: For the codes for Hstack & Vstack – note that double brackets are written. (Line 36 & 43)
    # Here (Line 43) the matrix is in the form 1X3 for the matrix 3X3 (line 42). 
    # If we write (3,1) when reshaping, it means (3X1) 3 rows and 1 column. 
    # Now we can get the desired output when run it. 

#Now we are going to join imputed values with the feature. 

X_with_imputedvalues = np.hstack((imputed_values.reshape(-1,1),X_with_nan[:,1:]))
print(X_with_imputedvalues)

# Join two feature Matrices
gate = np.vstack((X_with_imputedvalues,X))
print(gate)

# Alternatively there is an another method to join two feature matrices by using 'SimpleImputer'.

from sklearn.impute import SimpleImputer
X_complete = np.vstack((X_with_nan,X))
imputer = SimpleImputer(strategy="most_frequent") # There are many stratergies such as mean, median , mode so on.. 
imputer.fit_transform(X_complete)



