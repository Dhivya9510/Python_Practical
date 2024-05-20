# Reducing variance through Regularization - Ridge Regression 

    # Usually ‘High Variance’ are there in Underfitting and Overfitting.
    # If our (regression) model has any ‘High Variance’, instead using Linear method – we use ‘Regularization’ technique. 
    # There are two methods under Regularization. They are ‘Ridge’ and ‘Lasso’. 
    # These two methods are often called as ‘Shrinkage Penalty’. (Here penalty is nothing but adding penalty values to co-efficient)

# Hands-on:

   # You want to reduce the variations of your linear regression model. 
   # Use a learning algorithm that includes a 'Shrinkage Penalty' (also called as Regularization) like ridge regression and lasso regression. 

# Load Libraries: 
from sklearn.linear_model import Ridge
from sklearn.datasets import fetch_openml
from sklearn.preprocessing import StandardScaler

load_boston = fetch_openml(name='boston', version=1)

# Load data:

boston = load_boston
features = boston.data
target = boston.target

# Standarized features: 

scalar = StandardScaler()
standard_features = scalar.fit_transform(features)

# Create Ridge regression with an alpha value

regression = Ridge(alpha=0.5)  # we can give penalties by mentioning the values in alpha. 

# Fit the linear regression: 

model = regression.fit(standard_features,target)

# Scikit-learn includes a Ridge-CV method that allows us to select the ideal value for alpha. 
# RidgeCV is nothing but 'Ridge Cross Validation'. 

# Load Libries: 
from sklearn.linear_model import RidgeCV 

# Create ridge regression with three alpha values: 

regr_CV= RidgeCV(alphas=[0.1, 1.0, 10.0])  #type:ignore

# Fit the linear regression

model = regr_CV.fit(standard_features, target)
# View Co-efficients: 
model.coef_

# View alpha: 
model.alpha_