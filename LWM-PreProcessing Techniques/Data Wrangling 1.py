# PROGRAM FOR TRAINING AND SPILITING: 

import numpy as np
from sklearn.model_selection import train_test_split

X,y = np.arange(10).reshape((5,2)),range(5)
print(X)
print(list(y))

X_train, X_test, y_train, y_test = train_test_split (X, y, test_size = 0.3)

print(X_train)
print(y_train)
print(X_test)
print(y_test)

# LOADING A SAMPLE DATASET

import numpy as np
import pandas as pd

from sklearn import datasets

digits = datasets.load_digits()
features = digits.data    #type: ignore
target = digits.target    #type: ignore

print(features[0])

# DATA WRANGLING:   (https://www.youtube.com/watch?v=j9hC_-QaWkA)

   # Load Library
import pandas as pd

   # Create URL:
URL = "https://raw.githubusercontent.com/chrisalbon/simulated_datasets/master/titanic.csv"

   # Load data as a dataframe
df = pd.read_csv(URL)

   # Show first 5 rows: 
print(df.head())

# NOTE:  IN YOU-TUBE VIDEO, THE LINK GIVEN WAS NOT IN CLOUD SO UNABLE TO DOWNLOAD IT. JUST WRITTEN THE CODE BELOW AS TAUGHT IN VIDEO BUT OUTPUT WONT' BE SHOWN. 

# CREATING A DATA FRAME:

dataframe = pd.DataFrame()

   # Adding columns

dataframe["Name"] = ["Jackie jackson",  " Steve Stevenson"]
dataframe["Age"] = [25,38]
dataframe["Driver"] = [True, False]

print(dataframe)

# Alternatively, once you have created a DataFrame object, we can append new rows to the bottom. 
     # Create row
new_person = pd.Series(["Paul Welsely", 40, True], index = ["Name", "Age", "Driver"])
     # Append now
goat = dataframe.append(new_person, ignore_index = True)  #type: ignore (If you run the dataframe, 'append' will be in color)
print(goat)


# DESCRIBING THE DATA: 

     # Create URL
dfm = pd.read_csv("https://raw.githubusercontent.com/chrisalbon/simulated_datasets/master/titanic.csv")
     # Show two rows: 
print(dfm.head(2))

     # We can also take a look at the number of rows and columns:
     # # Show dimensions:

calce = dfm.shape             # Note 'shape' is an attribute - NOT A FUNCTION. 
print(calce)                  # Output will be (rows X columns)

     # Additionally, we can get descriptive statistics for any numeric columns using 'describe':
     # Show statistics:

henry = dfm.describe()         # descriptive statistics - count, mean, std, max, min etc.. will be the output. 
print(henry)


# NAVIGATING DATAFRAMES: 

dfm.iloc[0]
dfm.iloc[1:4]
dfm.iloc[:4]

  # Dataframe do not need to be numerically indexed. We can set the index of dataframe to any value where the value is unique to each row. 
  # Eg: We can set the index to be passenger names and then select rows using a name. 
  # Set index:
dfm = dataframe.set_index(["Name"])
  # Show row: 
dfm.loc["Allen, Miss Walton"]

# TOR (Things to remember)
 
   # 	‘loc’ is useful when the index of the dataframe is a label (eg: string)
   
   # ‘iloc’ works by looking for the position in the dataframe. Eg: iloc[0] will return the first row regardless of  whether the index is an integer or a label. 

# SELECTING ROWS BASED ON CONDITIONALS: 

    # Show top two rows where column 'sex' is 'female'

dfm[dfm["sex"]= "Female"].head()  # type: ignore   - for some more clarity on this code, watch the above given link - (13:57 to 14:15)

    # To see only the names of the Female of the first two in the file. 

dfm[dfm["sex"] = "Female"]["Name"].head()  # type: ignore 

    # To select rows with MULTIPLE CONDITIONS USING CONDITIONAL OPERATORS: 

dfm[(dfm["sex"] = "Female") & (dfm["Age"] >= 65)].head() # type: ignore

     
     # To reset_index:

dfm.reset_index(drop=True)   # Previously we set index as string type called 'Name'. Now we again reset it as index. 


# REPLACING VALUES:  

    # Replace values, show two rows: 
cot = dfm["Sex"].replace("female", "women").head(2)  # type: ignore - if we give 'inplace=True' - then the changes will reflect in original data also. So here we give only 'replace'.
print(cot)

    # We can also replace multiple values at the same time:

dot = dfm["Sex"].replace(["female","male"],["Women", "Men"]).head(2)  # type: ignore 
print(dot)

    # Replace values, show two rows: 

hat = dfm.replace(1, "one").head(2)   # always use () bracket after the 'replace' function.
print(hat)

    # To reset index: 

cold = dfm.reset_index(drop= True, inplace= True)  # Index changes will reflect in original data also. 
print(cold)

    # Replace also accepts regular expressions: 
    # Replace values, show two rows: 

dfm.replace(r"1st", "First", regex= True).head(2)  # Note the code for regular expression. 


# RENAMING COLUMNS: 
     # Rename column, show two rows: 

Hello = dfm.rename(columns={"PClass": "Passenger Class"}).head(2)       
print(Hello) 

     # ‘Rename()’ function accepts only dictionary. So we need to give dictionary only when comes to rename()  function. 
     # Note that the rename method can accept a dictionary as a parameter. We can use the dictionary to change multiple column names at once

Guts = dfm.rename(columns={"PClass": "Passenger Class", "Sex": "Gender"}).head(2)       
print(Guts) 

     # In the above link dataset - there are only 6 columns. What if the real world data in case it might having 130 columns with large data. So that we need to import 'collection' library. 
     # Load Library

import collections

      # Create Dictionary: 

column_names = collections.defaultdict(str)     

       # Create keys: 

for names in dfm.columns:
    column_names[names]

      # Show dictionary:

print(column_names)

# FINDING THE MAXIMUM, MINIMUM, SUM, AVERAGE AND COUNT. 

   # Calculate Statistics: 

print("Maximum:".dfm["Age"].max())         # type: ignore
print("Mininum:".dfm["Age"].min())         # type: ignore
print("Sum:".dfm["Age"].sum())             # type: ignore
print("Count:".dfm["Age"].count())         # type: ignore
print("Mean:".dfm["Age"].mean())           # type: ignore

  # Show counts.

google = dfm.count()             # Showing columnwise count information with label. 
print(google)


# FINDING UNIQUE VALUES: 
  # Select Unique values: 

cool = dfm["Sex"].unique()
print(cool)

   # Show counts:  (How many male and how many female)

bulk = dfm["Sex"].value_counts
print(bulk)


# HANDLING MISSING VALUES: 

    # Select missing values in "Ages", show head rows()

jack = dfm[dfm["Age"].isnull()].head()  # inside dfm is for showing real data values instead returning boolean values. 
print(jack)

    # Attempt to replace values with NaN for 'Male' in sex column. 

rplc = dfm["Sex"].replace("Male", "NaN")
print(rplc)                   # Note the result showing error. Because, 'NaN' is not a normal data type - It's numpy's data type. so we need to import numpy first. 


import numpy as np
rplc = dfm["Sex"].replace("Male", np.nan)
print(rplc)

    # Set NaN values to another values. 

bgm = pd.read_csv(URL, na_values= [np.nan, 'None', -999])   # type: ignore
print(bgm)


# __________________________________PART ! DONE_______________________________________________________
   

