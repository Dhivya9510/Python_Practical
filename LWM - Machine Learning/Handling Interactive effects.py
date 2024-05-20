
# What are Interactive effects? 

   # In simple words, two features combined and interacted to creating an output and then how to use that output in our algorithm for better optimization. 

# Load Libraries: 
from sklearn.linear_model import LinearRegression
from sklearn.datasets import fetch_openml
from sklearn.preprocessing import PolynomialFeatures

load_boston = fetch_openml(name='boston', version=1)

# Load data with only two features: 

boston = load_boston
features = boston.data
target = boston.target

# Create interaction term: (This is for interating POLYNOMIAL FEATURE to fit into feature)

interaction = PolynomialFeatures(degree=3, interaction_only= True, include_bias= False)
feature_interaction = interaction.fit_transform(features)
print(feature_interaction)

# Create regression line: 

regression = LinearRegression()
print(regression)

# Fit the linear regression line: (This is for interating REGRESSION to fit into feature)

model = regression.fit(feature_interaction, target)  # Remember model should have both feature and target. 
print(model)

# Formula

    # (Unable to do practical in Visual Studio Code due to raised errors because of version controls). 
    # (I have explained in MS-Word on the thing which mentioned in the  screenshot attached in the word document for the better understanding).
    # (Please refer to that)


# NOTE THAT:  ‘INTERACTION_ONLY = TRUE’ ONLY IF IT IS LINEAR REGRESSION
             #‘INTERACTION_ONLY = FALSE’ IF IT IS NON-LINEAR REGRESSION. 
    