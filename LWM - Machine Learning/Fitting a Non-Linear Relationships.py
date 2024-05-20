# FITTING A NON-LINEAR RELATIONSHIPS:
  
    # We can’t say that each and every time our features/data would be in linear relationship. 
    # Sometimes it may go to Non-linear relationship. 
    # In such instances, this chapter is going to explain about how to fit our Linear regression algorithm for Non-linear features. 

# Detailed explanations are provided in the MS-word. Please refer for the better understanding. 

# You have to model a non-linear relationship. 
# Create a polynomial regression by including polynomial features in a linear regression model. 

# Load Library:

from sklearn.linear_model import LinearRegression
from sklearn.datasets import fetch_openml
from sklearn.preprocessing import PolynomialFeatures

load_boston = fetch_openml(name='boston', version=1)

# Load data with one feature: (unable to indexing due to VSC version control)

boston = load_boston
feature = boston.data
target = boston.target

# Create polynomial features X power of 2 and X power of 3:

polynomials = PolynomialFeatures(degree=3, include_bias= False)
feature_polynomials = polynomials.fit_transform(feature)

# Create Linear regression:

regression = LinearRegression()
print(regression)

# Fit the linear regression:

model = regression.fit(feature_polynomials, target)
print(model)

# View first observation:

feature[0]   # (Indexing error raised due to VSC version controls, so that did not run it)

# View first observation raised to the power of 2:
 
feature[0] ** 2  # (Indexing error raised due to VSC version controls, so that did not run it)

# View first observation raised to the power of 3:

feature[0] ** 3   # (Indexing error raised due to VSC version controls, so that did not run it)

# View first observation's values for X, power of 2 & power of 3:

feature_polynomials[0]   # (Indexing error raised due to VSC version controls, so that did not run it)

# Formula

    # (Unable to do practical in Visual Studio Code due to raised errors because of version controls). 
    # (I have explained in MS-Word on the thing which mentioned in the  screenshot attached in the word document for the better understanding).
    # (Please refer to that)

# NOTE: WE HAVE TO ADD ‘POLYNOMIAL FEATURE’ EXTENSION TO THE ‘LINEAR REGRESSION’ FORMULA SO THAT WE CAN FIT THE ‘NON-LINEAR RELATIONSHIP’ TO THE ‘LINEAR REGRESSION’. 
       # Here in this chapter, I have a doubt that why we did not include parameter 'interaction_only = False' being it was non-linear. 
       # "Interaction_only = True" only it was Linear regression. 