# BIAS AND VAIRANCE

 # When you searching the definition of ‘Bias and Variance’, internet shows so many. But the below is the basic and general definitions of ‘Bias and Variance’
      # Assume that both ‘Bias’ & ‘Variance’ are errors. 
	  # Bias is the error that has been created in our training data while we train the model. 
	  # After we fitting the model, we moved to testing it. Isn’t it?  
	  # ‘Variance’ is the error that has been created in our testing data. 

  # When we increasing the degree of the polynomial – the flexibility of the linear curve also improves. When the degree is 1, means that it’s Linear. 

  # Underfitting:
      # When the residuals between the data points are high, it is stated as ‘Underfitting’. 
      # Underfitting involves High Bias and High Variance. 
      # Underfitting is nothing but it gives the Poor performance in both Training data and Testing data. 
      # Whenever our data showing ‘High Bias’ or ‘High Variance’, we need to use some techniques such as Optimization technique or Tuning Technique. 

  # Overfitting:
      # In Overfitting – we increase our degree. i.e. degree of 3. Hence there will be more flexibility in our line over the data points. 
      # So here, our model will be performing well in our Training data. Therefore, Performance accuracy is good due to Low Bias. 
      # Next step is evaluating the model by providing it to testing. Isn’t it? Here in test data – our model performance will be low means that it showing errors without correct output. Hence in Overfitting involves Low Bias and High Variance. 

  # Generalized model: (other than overfitting and underfitting)

      # So far, we have to avoid Overfitting and Underfitting (degree of 3 and degree of 1). We should move to ‘Generalized model’ (degree of 2) where it gives both ‘Low Bias and Low Variance’. (Second Graph). 
      # The above all is for Regression, right? What if for Classification?             
           # For example (refer MS-Word notes), In Model 1 – Error % is 1 means that there is 99% accuracy in training data and in testing data, there is 20% of error and 80% of accuracy. 
           # Hence it performs well in training data (Low Bias) and performs poor in Testing data (High Variance).  

