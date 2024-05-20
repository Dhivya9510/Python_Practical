# LINEAR REGRESSION: 
      # Linear Regression is one of the Simple Algorithm of Supervised Learning. 
      # It can find our the ‘Quantitative Target Vector’ (nothing but output that has numerical values like house price, age, etc..)
      # Francis Galton was the one who formulates ‘Linear Regression’ in 1800. 

       # If we have two points, it will be easy for us to calculate the mean value. 
       # For example, saying - what is for 3.5 in x-axis? The answer would be 7. It’s like we simply calculate it’s average to find out the mid-point.
       # What if there are multiple data points? By using ‘Least Square Method’ – we can calculate the closer (minimum distance with the mean – to minimize the vertical distance of data points) to find the algorithm to draw the regression line among multiple points. 

       # Main Goal – To Minimize the Vertical Distance. 
       # Residuals – The distance between the line and the closest data points are known Residuals. 
       # We need to minimize the residual distance to get our algorithm to perform well to give target vectors accurately. 

# LINEAR REGRESSION – EXPLANATION:
       # Linear regression analysis is used to predict the value of a variable based on the value of another variable. The variable you want to predict is called the dependent variable. The variable you are using to predict the other variable's value is called the independent variable.

             # There must be some linear relationship between the feature and the target vector so that we can get into the linear regression. 
             # If there are any effects occurred in ‘Features’, it constantly affects the ‘Target Vector’. (Output)

# 1.1 FITTING A LINE: 
 
  # You want to train a model that represents a linear relationship between the feature and target vector. 
  # Use Linear regression (In scikit-learn, Linear Regression):

# Load Libraries:

from sklearn.linear_model import LinearRegression
from sklearn.datasets import fetch_openml 
load_boston = fetch_openml(name='boston', version=1)  # Quora suggestive additional code due to the unavailability of Load-boston data in this version. 
print(load_boston)


# Load data with only two features:
boston = load_boston
features = boston.data
target = boston.target

# Create Linear Regression
regression = LinearRegression()
print(regression)

# Fit the linear regression

model = regression.fit(features, target)
print(model)

   # Beta ....(This concept will be explained later – Here Beta1 & Beta2 mentioned in the formula are the co-efficient of our features. 
   # Beta 0 is showing with the value by adding Bias/ Intercept).

# Formula: 

    # Beta 0, also called the Bias or Intercept, can be viewed using ‘intercept_’.
    # To view the intercept_:

beta0 = model.intercept_
print(beta0)

    # And Beta1 and Beta2 are shown using ‘coef_’
    # Here we gonna see first value in the target vector multiplied by 1000.

X1000 = target[0] *1000
print(X1000)

     # Predict the target value of the first observation, multiplied by 1000. 

Predicted_value = model.predict(features)[0]
X1000_predict = float(Predicted_value) * 1000
print(X1000_predict)

     # Finally we have to view the feature co-efficient. 
    
coef = model.coef_
print(coef)


# Why we multiplied 1000 for beta1 & beta2? 
# Because by default in ‘Boston’ dataset they convert our terms in to standardized values. 
# (We need to do this by default when working on this for beta 1 and beta 2 everytime). 
# First value in the target vector multiplied by 1000 and then we have to predict the target value of the first observation, multiplied by 1000 
# (meaning that out of two features that we taken here, we have to predict the target value for the first observation of a feature). 