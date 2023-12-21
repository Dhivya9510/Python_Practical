# Pandas Tutorial review 

# Pandas is a python library. It is used for analyzing data
# If we need to work with large data sets, we can use Pandas library to analyze, clean, explore & manipulate data.
# The name 'Pandas' refer to both 'Panel Data' & 'Pyton Data Analysis' which was discovered in 2008 by  Wes McKinney 
# We can prefer pandas if we want to get answers regarding finding correlations between two or more columns, average value, Max value and Min value
# Also it much helps to clean the messy data by cleaning method - deleting empty (null) data, irrelevant data, wrong data & duplicate data 
# In data science, when work with large data set, pandas library much helps us to analyzing the data to make ease deriving the required information from the large data set. 

# Dictionary could be used in this. 
# DataFrame should be used in this to get the index number with table like output. 

# Example:

import pandas as pd

mydataset = {"Cars":["BMW","Ford","Maruthi","Lamborgini"],"Model":["2000","2002","2003","2005"]}

my_newdata = pd.DataFrame(mydataset)
print(my_newdata)

# Version
import pandas as pd
print(pd.__version__)

# Pandas series is like a single table in a column
# It's an one dimentional array that holds any data type

import pandas as pd
hut = [5,10,15]
unit = pd.Series(hut)
print(unit)

# Accessing elements using index number.
print(unit[1])

# Create Labels
unit = pd.Series(hut, index = ["x","y","z"])
print(unit)

# Accessing elements using index number (labelling)
print(unit["y"])

# The keys of the dictionary become the labels.
import pandas as pd
horse = {"names":"Anu","Topper":"Radha","Absentee":"Charitha"}
hor = pd.Series(horse)
print(hor)

# 



