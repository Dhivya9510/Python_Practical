# HANDLING CATEGORICAL DATA:

# In previous chapter – we go through ‘Handling Numerical data’ that is Quantitative. 
# Now we are going to go through ‘Handling Categorical data’ that is Qualitative. 
# Qualitative data can be divided into two types. One is Nominal (no intrinsic ordering) & the other one is ordinal (have some order)
# Example of Nominal data – Male & Female, Green, Yellow & Orange. (Here there is no order)
# Example of Ordinal data – Low marks, medium marks & High marks. (Here there is some order that is from ascending to descending)


# ML algorithms generally process the numerical data type. Hence, we need to process the categorical data (as an assignment given to us by our boss) into the numerical data. There are many strategies to perform the same.
# There is an Algorithm called KNN (K-Nearest Neighbor) – The main purpose of KNN is to calculate the distance. It involves the method of ‘Euclidean Distance (L2)’. 

# 1.	Encoding Nominal Categorical Features:

      # The term ‘Encoding’ is nothing but the process of converting categorical data into numerical data. 
      # Here we are going to cover how to encode nominal categorical data and ordinal categorical data in to numerical data. This process technique is known as ‘One-hot encode’. 
      # preprocessing - LabelBinarizer & MultiLabelBinarizer. 

# Import Libraries
import numpy as np
from sklearn.preprocessing import LabelBinarizer,MultiLabelBinarizer

# Creating a categorical feature 
feature = np.array([["Texas"],["California"],["Texas"],["Delaware"],["Texas"]])

# Create one-hot encoder
onehot_encoder = LabelBinarizer()
# Fitting one-hot encoder
apple = onehot_encoder.fit_transform(feature)
print(apple)

# We can use the 'classes_method' to output the classes. 

Bee = onehot_encoder.classes_
print(Bee)

# If we want to reverse the one-hot encoding, we can use 'inverse_transform' method.

Chart = onehot_encoder.inverse_transform(onehot_encoder.transform(feature))
print(Chart)

# We can even use PANDAS to one-hot encode the feature:

# Import Library
import pandas as pd
# Create dummy variables from feature:
den = pd.get_dummies(feature[:,0])    # Feature[:,0] is nothing but all rows and 1st column (actually there is one column only even though we mentioned it)
print(den)

# One helpful ability of scikit-learn is to handle a situation where each observations lists multiple classes: 

# Create Multiclass feature
multiclass_feature = [("Texas","California"),("California","Alabama"),("Texas","Florida"),("Delware","Florida"),("Texas","Alabama")]
# Create Multiclass onehot encoder
multiclass_onehot = MultiLabelBinarizer()
# Fitting MultiLabelBinarizer
elephant = multiclass_onehot.fit_transform(multiclass_feature)
print(elephant)

# Once again we can see the classes with 'classes_'method 
print(multiclass_onehot.classes_)

