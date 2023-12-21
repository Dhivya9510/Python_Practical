# Pandas DataFrames

# What is a DataFrame?
   # A Pandas DataFrame is a 2 dimensional data structure, like a 2 dimensional array, or a table with rows and columns.
   # Example:
       # Create a simple Pandas DataFrame:

import pandas as pd

tag = {"Name":["Anu","Bharath","Chaithanya"], "Age":[23,24,21]}

b = pd.DataFrame(tag)
print(b)

# Locate Row
  # As you can see from the result above, the DataFrame is like a table with rows and columns.
  # Pandas use the loc attribute to return one or more specified row(s)
  # Example
      # Return row 0:

import pandas as pd

tag = {"Name":["Anu","Bharath","Chaithanya"], "Age":[23,24,21]}

b = pd.DataFrame(tag)
print(b.loc[0])                   # Note- To access the particular row with index number , we need to use 'LOC' attribute by adding dot . after variable name.

# Note: This example returns a Pandas Series.

# Example
   # Return row 0 and 1:

import pandas as pd

tag = {"Name":["Anu","Bharath","Chaithanya"], "Age":[23,24,21]}

y = pd.DataFrame(tag)
print(y.loc[[0,1]])

# Note: When using [], the result is a Pandas DataFrame.

# Named Indexes
  # With the index argument, you can name your own indexes.
  # Example
     # Add a list of names to give each row a name:

import pandas as pd

unit = {"Class":["First","Second","Third"], "Rank":["O-grade","A-grade","B-grade"]}

n = pd.DataFrame(unit, index = ["Numbers","Grades","List"])         # Note how many list elements need to input - two or three!

print(n)

# Locate Named Indexes
  # Use the named index in the loc attribute to return the specified row(s).
  # Example
     # Return "List":

import pandas as pd

unit = {"Class":["First","Second","Third"], "Rank":["O-grade","A-grade","B-grade"]}

n = pd.DataFrame(unit, index = ["Numbers","Grades","List"])         

print(n.loc["List"])

# Load Files Into a DataFrame
    # If your data sets are stored in a file, Pandas can load them into a DataFrame.
    # Example
         # Load a comma separated file (CSV file) into a DataFrame:

import pandas as pd

lid = pd.read_csv("tag.csv")
print(lid)



# Own Notes - To access the particular row with index number , we need to use 'LOC' attribute by adding dot . after variable name. 
           # WE NEED TO USE DOUBLE SQUARE BRACKETS [[]] IF WE NEED TO LOCATE TWO ROWS IN PANDAS DATAFRAME

