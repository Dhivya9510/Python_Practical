# Pandas Series

# What is a Series?
   # A Pandas Series is like a column in a table.
   # It is a one-dimensional array holding data of any type.
   # Example:
        # Create a simple Pandas Series from a list:

import pandas as pd

i = [1,2,3,4]

yolk = pd.Series(i)
print(yolk)

# Labels
  # If nothing else is specified, the values are labeled with their index number. First value has index 0, second value has index 1 etc.
  # This label can be used to access a specified value.
  # Example
    # Return the first value of the Series:

import pandas as pd

t = [2,4,6,8]

hit = pd.Series(t)
print(hit[0])

# Create Labels
  # With the index argument, you can name your own labels.
  # Example
     # Create your own labels:

import pandas as pd

r = ["H","U","G"]

mouse = pd.Series(r, index = ["A","B","C"])   # Note that index should be write inside the list with double quotes. 
print(mouse)

# When you have created labels, you can access an item by referring to the label.
  # Example
     # Return the value of "y":

import pandas as pd

e = ["Ab","Bc","Cd"]
horse = pd.Series(e, index= ["P","Q","R"])

print(horse["Q"])

# Key/Value Objects as Series
  # You can also use a key/value object, like a dictionary, when creating a Series.
  # Example
     # Create a simple Pandas Series from a dictionary:

import pandas as pd

mydata = {"day1":420,"day2":420,"day3":410}      # need to double quote separately for keys and values, for numeric values - quotes not needed. 

q = pd.Series(mydata)
print(q)

# Note: The keys of the dictionary become the labels.
   # To select only some of the items in the dictionary, use the index argument and specify only the items you want to include in the Series.
   # Example
       # Create a Series using only data from "day1" and "day2":


import pandas as pd

t = {"day1":450,"day2":420,"day3":430}

g = pd.Series(t, index = ["day1","day2"])  # Note do not put double quotes for INDEX. Key values also should put as list for index. 
print(g)

# DataFrames
   # Data sets in Pandas are usually multi-dimensional tables, called DataFrames.
   # Series is like a column, a DataFrame is the whole table.
   # Example:
      # Create a DataFrame from two Series:

import pandas as pd

myinfo = {"Age":[23,34,31], "Name":["Anju","Henry","Ragu"]}

w = pd.DataFrame(myinfo)
print(w)


# Own Notes: In creating labels, the index should be write inside the list with double quotes. 
           # need to double quote separately for keys and values, for numeric values - quotes not needed.
           # Note do not put double quotes for the word INDEX. Key values also should put as list for index. 