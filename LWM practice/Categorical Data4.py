# HANDLING IMBALANCED CLASSES: 

# What if ‘Target vector’ is highly imbalanced. How to encountered it? Let’s see here in this chapter: 
# (We can ask to our data providers to give more data in a particular observation or else we can change our Metrics to evaluate, we can use ‘class/weight’ parameters when we run our algorithms by given the % of data we have in each observation 
# We have a strategy called ‘Upsampling’ and ‘Downsampling’. Also, through this technique we can change our unbalanced data to balanced data.)

# Remember that ‘Iris’ dataset is balanced in Nature. 
# Each observation (Setosa, Virginica & Versicolor) have 50 cases. 
# To our understanding LWM artificially changed it as imbalanced dataset by deleting 40 cases in Setosa by leaving only 10 observations then combining ‘Virginica’ & ‘Versicolor’ together by having 100 observations. 
# Now it’s divided it as class 0 & class 1. Class 0 is ‘Setosa’ and Class 1 is ‘Not Setosa’.

# Import Libraries

import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import load_iris

# Load iris data: 
iris = load_iris()
print(iris)

# Creating feature matrix: 
feature = iris.data  # type:ignore

# Creating target matrix: 
target = iris.target # type: ignore

# Understand from above image that here 0 means ‘Setosa’, 1 means ‘Verinica’ and 2 means ‘Versicolor’. 

# Remove first 40 observations
features = feature[40:,:]
target = target[40:]

# Create a binary target vector indicating if class 0
target = np.where((target == 0), 0, 1)

# Look at the imbalanced target vector
print(target)

# Also understand from below image that:
   # Totally we have 150 observations. From that we need to delete first 40 observations from ‘Setosa’ so remaining ‘Setosa’ values will be ‘10 zero’. 
   # We started from 40th observation (means that we do not consider first 40). So [40:, :] – all columns.
   # Target [40:] means from 40th observations till end. That means until the end of ‘Versicolor’.
   # ‘np.where((target == 0), 0, 1)’ refers that if ‘Setosa’ is 0, continue as 0 (only 10 observations will be there for ‘Setosa’. 
   # Otherwise all other things will be 1 – means rewrite 1,2 as 1 itself. 

# Now our data is unbalanced with 110 observations. Here 10 observations belong to Class 0 and the remaining 100 observations belongs to Class 1. 
# Many Algorithms in Scikit-learn offer a parameter to ‘weight classes’ during training to counteract the effect of their imbalance. 
# While we have not covered it yet, RANDOMFORESTCLASSIFIER is a popular classification algorithm and includes a class_weight parameter. 
# You can pass an argument specifying the desired class weights explicitly: 

# Create Weights:
weights = {0:0.9, 1:0.1}  # Note to write the propotions in to dictionary. 

# Create Random Forest Classifier with weights: 
app = RandomForestClassifier(class_weight=weights)
print(app)

# If you feel like your dataset is ‘Balanced’ already – you can directly pass ‘Class_Weight = Balanced’) then the RandomForestClassifier straightly maps your data to the balanced data set. 

# UPSAMPLING AND DOWNSAMPLING: 
 # Before we use this technique – we should know what is Majority and what is Minority?
     # 10 cases in ‘Setosa’ in Class 0 is Minority 
     # 100 cased in ‘Veronica & Versicolor’ in Class 1 is Majority. 

# (First shall we write a code for counts on Majority and Minority (to proceed with upsampling/downsampling) So that we can count the indices of Class 0 & Class 1)
# (code for indices) Indicies of each class's observations. 
i_class0 = np.where(target==0)[0]  # Output showing the indices of each element in class0
i_class1 = np.where(target==1)[0]  # Output showing the indices of each element in class1

# Number of Observations in each class: 
n_class0 = len(i_class0)
n_class1 = len(i_class1)

# What is downsampling? 
   # Downsampling is nothing but reducing the sample size of majority equal to the sample size of Minority. 
   # Downsampling is generally done with Majority to perform reduction. 

# Rules: 
   # By having 10=10 i.e. with only 20 observations – we feed the data to ML algorithms. 
   # Remember that we should not took first/last observations from Majority for reduction, we must take it randomly.  
   # Similarly, we should perform any ‘replace’ function. So that we should give ‘replace = false’ parameter. 

# For every observation of class 0, randomly sample from class 1 without replacement. 

i_class1_downsampled = np.random.choice(i_class1, size= n_class0, replace= False)

# (Now we will do Join the class 0 with class 1 downsampled)
# Join together Class 0's target vector with the downsampled Class 1's target vector. 

Joint = np.hstack((target[i_class0], target[i_class1_downsampled]))

# The above code is for target vector. We need to get the original data with values right - so we need to write feature matrix code)
# Join together Class 0's feature matrix with the downsampled Class 1's feature matrix. 

Head_joint = np.vstack((feature[i_class0,:], feature[i_class1_downsampled,:]))
print(Head_joint)


# What is Upsampling?
    # Upsampling is nothing but increasing the sample size of Minority equal to the sample size of Majority. 
    # Upsampling is generally done with Minority to perform the action of increasing. 
    # Rules: 
        # Everything is same as ‘Downsampling’ but there is a only one change. 
        # We need to set the ‘replace’ function as ‘True’. When increasing Minority to Majority (10 to 100), there might be a chance to replace values. 

# For every observations in Class 1, randomly sample from Class 0 with replacement.
i_class0_upsampled = np.random.choice(i_class1, size= n_class1,replace=True)

# Join together Class 0's upsampled target vector with Class 1's target vector.
Joint1 = np.concatenate((target[i_class0_upsampled],target[i_class1]))

# Join together Class 0's upsampled feature matrix with Class 1's feature matrix. 
Head_Joint1 = np.vstack([feature[i_class0_upsampled,:],feature[i_class1,:]])
print(Head_Joint1)

# There is no use of predicting 99.9% accuracy in Unbalanced dataset. It may not be good enough. 
# But you are extraordinary if you predicting accuracy level 99.9% when your dataset is Balanced. 

# Upsampling -> Replace = True
# Downsampling -> Replace = False. 

# When to use Downsampling and When to use Upsampling? 
   # It’s up to us. We only need to analyze what sampling to use based on our context and dataset. 




