# Evaluation Metrics – Classification: 

      # We already know about our ML process, we will use performance metrics to evaluate how our model did. Let us discuss Classification metrics in more detail
            # Key Classification metrics we need to understand are: 
                  # Accuracy
                  # Recall
	              # Precision
            	  # F-1 Score

     # First we should understand the reasoning behind these metrics and how they will actually work in real world. 
     # Accuracy = Total number of correct predictions / Number of Predictions. 
          # Example result: Accuracy = 80/100 = 0.8 or 80% accuracy. 

# a.Accuracy:

  # Note: 
     # It would be considered 99 % accuracy is good only when our training data is well- balanced. 
     # Example: we have 100 images. It should be 50 as dogs and 50 as cats. If we input 70% well-balanced data into training model, the accuracy would be good when it predicts well with both the well-balanced data. 
     # If we give, 90% dogs and 10% cats images as training data – machine will predict testing data mostly with dogs only due to there are much dogs inputted testing data – we could not say it predicts good with 99% accuracy. 

# ACCURACY IS GOOD WHEN WE HAVE THE WELL-BALANCED DATA

# b.Recall:

   # For Unbalanced data – We can use ‘Recall’ Metrics. 
   # Recall = Number of True positives / Number of True positives + Number of False negatives. 
   # By using this formula – we can get all the relevant data from our dataset. 
   # So far, just understand this alone in ‘Recall’ Metrics. 

# c.Precision:
   # For Unbalanced data – We can also use ‘Precision’ Metrics. 
   # Precision = Number of True positives / Number of True positives + Number of False POSITIVES. 
   # By using this formula – we can get ONLY THE relevant data from our dataset.
   # So far, just understand this alone in ‘Precision’ Metrics. 

# d.F1 Score:

    # It’s doing ‘Optimal blend’ which is nothing but here we collectively use both the metrices called  ‘Recall’ & ‘Precision’
    # F1 Score = 2 * (Precision * Recall / Precision + Recall) 
    # Usually, we called this type of formula is known as ‘Harmonic mean’ (combining two metrics that has formula for each one separately). 

# As a model developer – once we done with our model, we obviously presenting our model to our client. Their trustworthy is based on our Evaluation Metrics. 
# They will ask our model’s accuracy – if we said, our model depends on unbalanced data, then they will ask not for accuracy but for precision and also the combination of both recall & precision i.e F1 score. Based on the result, they will understand that model performing level. If it’s given well score as result – they will approve for final deployment. 



# REGRESSION: 

 # Trade off – It contains two parameters. Recall and Precision. 
 # Here when ‘Precision’ goes up but the ‘Recall’ goes down or vice versa. 
 # When we slightly changed our decision boundary, the ‘Positive’ boundary will falls on ‘Negative’ boundary or vice versa. It may lead to misclassification of our data. Through ‘Precision’ and ‘Recall’, we can encounter such misrates.
 

# EVALUATION METRICS – REGRESSION:
    # Like ‘Classification’ that has different Evaluation metrics, Regression also having some. 
         # MAS: Mean Absolute Error
	     # MSE: Mean Square Error & 
	     # RMSE: Root Mean Squared Error.  

    # Here we consider ‘House price prediction’ for regression. It attempts to find out the continuous values. 
         
          # MAS – Example: If we want to predict housing price. Original value by our 30% data is rs. 100. However it predicts 95. So the difference would be |(100 – 95)| = 5 (It’s positive only). 
          # In case, it predicts 105. The difference would be 100 – 105 = -5 (It’s negative), so we use ‘modulars’ (which is like pipe symbol on both sides) to covert the negative sign into positive. So, 5 is the Mean Absolute error from the original value. 
          # MAS has a major problem - it punishes only small errors but not the high/large errors. The above screenshot has one data. If we have the multiple data... (please first refer to the below screenshot), 
          # When we add those errors one by one in multiple data, if any outliers found, then it will damage our evaluation metrics. Other than this everything in MAS would be fine. 
          # To rectify this problem (outliers in errors that damaged MAS evaluation metrics), we will go to MSE. MSE will encounter this problem. Only we need to square the formula of MAS. 
          # RMSE & MSE is like Standard deviation and Variance. To take square root for the answer that is obtained by squaring a value. 
