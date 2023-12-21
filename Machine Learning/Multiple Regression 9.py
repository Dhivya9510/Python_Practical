# Multiple Regression
     # Multiple regression is like linear regression, but with more than one independent value, meaning that we try to predict a value based on two or more variables.

# Check under resources, your can find 'MR- data.csv' - In that we can predict the CO2 emission of a car based on the size of the engine, but with multiple regression we can throw in more variables, like the weight of the car, to make the prediction more accurate.

# How Does it Work?
    # In Python we have modules that will do the work for us. Start by importing the Pandas module.
          # import pandas
    # The Pandas module allows us to read csv files and return a DataFrame object.
    # Then make a list of the independent values and call this variable X.
         # Put the dependent values in a variable called y.
                # X = df[['Weight', 'Volume']]
                # y = df['CO2']

# Tip: It is common to name the list of independent values with a upper case X, and the list of dependent values with a lower case y.

# We will use some methods from the sklearn module, so we will have to import that module as well:
     # from sklearn import linear_model
# From the sklearn module we will use the LinearRegression() method to create a linear regression object.
# This object has a method called fit() that takes the independent and dependent values as parameters and fills the regression object with data that describes the relationship:
     # regr = linear_model.LinearRegression()
     # regr.fit(X, y)

# #predict the CO2 emission of a car where the weight is 2300kg, and the volume is 1300cm3:
     # predictedCO2 = regr.predict([[2300, 1300]])

# Example: 
   # See the whole example in action: (Predic with the above line 24 & 25)

import pandas as pd
from sklearn import linear_model

df = pd.read_csv("resources/MR.data.csv")

X = df[["Weight","Volume"]]
y = df["CO2"]

regr = linear_model.LinearRegression()
regr.fit(X,y)

predictedCO2 = regr.predict([[2300,1300]])
print(predictedCO2)

# We have predicted that a car with 1.3 liter engine, and a weight of 2300 kg, will release approximately 107 grams of CO2 for every kilometer it drives.

# Coefficient
   # The coefficient is a factor that describes the relationship with an unknown variable.
   # Example: if x is a variable, then 2x is x two times. x is the unknown variable, and the number 2 is the coefficient.
   # In this case, we can ask for the coefficient value of weight against CO2, and for volume against CO2. The answer(s) we get tells us what would happen if we increase, or decrease, one of the independent values.

# Example
    # Print the coefficient values of the regression object:

import pandas as pd
from sklearn import linear_model

df = pd.read_csv("resources/MR.data.csv")

X = df[["Weight","Volume"]]
y = df["CO2"]

regr = linear_model.LinearRegression()
regr.fit(X,y)

print(regr.coef_)

# Result Explained
    # The result array represents the coefficient values of weight and volume.
           # Weight: 0.00755095
           # Volume: 0.00780526
    # These values tell us that if the weight increase by 1kg, the CO2 emission increases by 0.00755095g.
    # And if the engine size (Volume) increases by 1 cm3, the CO2 emission increases by 0.00780526 g.
    # I think that is a fair guess, but let test it!
    # We have already predicted that if a car with a 1300cm3 engine weighs 2300kg, the CO2 emission will be approximately 107g.
    # What if we increase the weight with 1000kg?

# Example
    # Copy the example from before, but change the weight from 2300 to 3300:

import pandas
from sklearn import linear_model

df = pd.read_csv("resources/MR.data.csv")

X = df[["Weight","Volume"]]                # Note brackets.
y = df["CO2"]

regr = linear_model.LinearRegression()
regr.fit(X,y)

predictedCO2 = regr.predict([[3300,1300]])   # Note brackets. # type: ignore
print(predictedCO2)

# We have predicted that a car with 1.3 liter engine, and a weight of 3300 kg, will release approximately 115 grams of CO2 for every kilometer it drives.
# Which shows that the coefficient of 0.00755095 is correct:
    # 107.2087328 + (1000 * 0.00755095) = 114.75968


# Own notes: When writing variables, we SHOULD NOT PUT PARENTHESIS after df.. Just put DOUBLE SQUARE BRACKETS for X & Single square bracket for y.
           # But when prediction, we should use Parenthesis and double square brackers here. Note line 91.
           # We predicted CO2 value (107) based on regression objects -  2300 (weight) & 1300 (Engine volume)
           # Then we find Co-efficient values for both regression objects. 
           # Will check the new prediction value with co-efficient we found out - when the weight increased from 2300 to 3300 (increased by 1000)
           # With the change of 3300, the new prediction value is 114.75 
           # Test : old prediction value (2300, 1300) - 107, new prediction value(3300,1300) - 114.75
           # so, 107 + (1000*0.00755095) = 114.75968
           #    107 + (increased by value * co-ef of weight we found) =  114.75968













