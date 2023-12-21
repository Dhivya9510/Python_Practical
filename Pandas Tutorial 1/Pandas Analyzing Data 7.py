# Pandas - Analyzing DataFrames

# Viewing the Data
  # One of the most used method for getting a quick overview of the DataFrame, is the head() method.
  # The head() method returns the headers and a specified number of rows, starting from the top.
  # Example:
      # Get a quick overview by printing the first 10 rows of the DataFrame:

import pandas as pd

tag = pd.read_csv("resources/data.csv")
print(tag.head(10))

# Note: if the number of rows is not specified, the head() method will return the top 5 rows.
# Example:
     # Print the first 5 rows of the DataFrame:

import pandas as pd

tag = pd.read_csv("resources/data.csv")
print(tag.head())

# There is also a tail() method for viewing the last rows of the DataFrame.
# The tail() method returns the headers and a specified number of rows, starting from the bottom.
# Example:
   # Print the last 5 rows of the DataFrame:

import pandas as pd

print(tag.tail())

# Info About the Data
  # The DataFrames object has a method called info(), that gives you more information about the data set.
  # Example:
     # Print information about the data:

import pandas as pd

print(tag.info())

#Null Values
  # The info() method also tells us how many Non-Null values there are present in each column, and in our data set it seems like there are 164 of 169 Non-Null values in the "Calories" column.
  # Which means that there are 5 rows with no value at all, in the "Calories" column, for whatever reason.
  # Empty values, or Null values, can be bad when analyzing data, and you should consider removing rows with empty values. This is a step towards what is called cleaning data, and you will learn more about that in the next chapters.

# Own notes : Here in Pandas Analysing data, we saw HEAD, TAIL & INFO on datasets.
            # head(7) returns the first 7 rows of dataset excluding header. head() defaultly returns first 5 rows excluding header
            # Tail(7) returns the last 7 rows of dataset excluding header. Tail () defaultly returns last 5 rows excluding header
            # info() returns the information on the dataset. 
