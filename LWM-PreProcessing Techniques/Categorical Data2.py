# HANDLING CATEGORICAL DATA (PART -2)

# Use Pandas Dataframe’s replace method to transform string labels to numerical equivalents: 

# Import Libraries
import pandas as pd
# Create features
Df = pd.DataFrame({"Score" :["Low","Low","Low","Medium","Medium","High"]})
# Create Mapping
Scale_mapping = {"Low":1,"Medium":2, "High":3}
# Replace feature values into scale
App = Df["Score"].replace(Scale_mapping)
print(App)

# Another Example: 
import pandas as pd
feature = pd.DataFrame({"Score" : ["Low","Low","Medium","Medium","High","Barely more than medium"]})
Scalar_mapping = {"Low":1,"Medium":2,"High":4,"Barely more than medium":3}
bee = feature["Score"].replace(Scalar_mapping)
print(bee)

# In this example, the distance between LOW & MEDIUM is the same as the distance between Medium & Barely more than medium, which is almost certainly not accurate.
# The best approach is to be consious about hte numeical vales mapped to clases. 
import pandas as pd
feature = pd.DataFrame({"Score" : ["Low","Low","Medium","Medium","High","Barely more than medium"]})
Scalar_mapping = {"Low":1,"Medium":2,"High":4,"Barely more than medium":2.1}
Chair = feature["Score"].replace(Scalar_mapping)
print(Chair)

# ENCODING DICTIONARIES AS FEATURES: (Seperate values from keys as endcode per my understanding)

# This is to convert Dictionary into Feature Matrix. 
# If ‘Sparse=True’ – In the output matrix, you won’t see any zeros, only numbers will be there like 1,2,3 and so on. 
# If we set ‘Sparse=False’ means that you will allow Zeros in the output Matrix.                                                                                                                                     Allowing ‘Zeros’ will be okey for ‘Toy datasets’ however if you work on the massive datasets – you must have to set the ‘Sparse=True’ to get your data encountered as you worked. For example, NLP: it (sparse = True) makes the Text data to change as Vector


# Import Library
from sklearn.feature_extraction import DictVectorizer
# Creating a Dictionary
data_dict = [{"Red" : 2, "Blue" :4},{"Red" :4, "Blue" :3},{"Red" :1, "Yellow" : 2},{"Red": 2, "Yellow" : 2}]
# Creating DictionaryVectorizer
dictVectorizer = DictVectorizer(sparse=False) # Sparse says 'I will NOT allow Zeros'.'False' allows Zeros.
# Convert dictionary to featurematrix
features = dictVectorizer.fit_transform(data_dict)
print(features)

# We can get the names of each generated feature using the ‘get_feature_names_out()’ method. 
feature_names = dictVectorizer.get_feature_names_out()
print(feature_names)
