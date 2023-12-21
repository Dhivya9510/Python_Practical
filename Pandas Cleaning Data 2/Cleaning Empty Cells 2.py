# Pandas - Cleaning Empty Cells

# Empty Cells
  # Empty cells can potentially give you a wrong result when you analyze data.

# Remove Rows
  # One way to deal with empty cells is to remove rows that contain empty cells.
  # This is usually OK, since data sets can be very big, and removing a few rows will not have a big impact on the result.

# Example: 
   # Return a new Data Frame with no empty cells:

import pandas as pd

unit = pd.read_csv("resources/Data1.csv")

new_unit = unit.dropna()
print(new_unit.to_string())

# Note: By default, the dropna() method returns a new DataFrame, and will not change the original.

# If you want to change the original DataFrame, use the inplace = True argument:
# Example
  # Remove all rows with NULL values:

import pandas as pd

unit = pd.read_csv("resources/Data1.csv")

unit.dropna(inplace = True)

print(unit)

# Note: Now, the dropna(inplace = True) will NOT return a new DataFrame, but it will remove all rows containing NULL values from the original DataFrame.

# Replace Empty Values
  # Another way of dealing with empty cells is to insert a new value instead.
  # This way you do not have to delete entire rows just because of some empty cells.
  # The fillna() method allows us to replace empty cells with a value:

#Example
  # Replace NULL values with the number 130:

import pandas as pd

unit = pd.read_csv("resources/Data1.csv")

unit.fillna(130, inplace = True)
print(unit)

# Replace Only For Specified Columns
  # The example above replaces all empty cells in the whole Data Frame.
  # To only replace empty values for one column, specify the column name for the DataFrame:

# Example
   # Replace NULL values in the "Calories" columns with the number 130:

import pandas as pd

unit = pd.read_csv("resources/Data1.csv")

unit["Calories"].fillna(130, inplace = True)

print(unit)

# Replace Using Mean, Median, or Mode
  # A common way to replace empty cells, is to calculate the mean, median or mode value of the column.
  # Pandas uses the mean() median() and mode() methods to calculate the respective values for a specified column:

# Example
   # Calculate the MEAN, and replace any empty values with it:
   
import pandas as pd

unit = pd.read_csv("resources/Data1.csv")

p = unit["Calories"].mean()

unit.fillna(p, inplace = True)
print(unit)

# Mean = the average value (the sum of all values divided by number of values).

# Example
  # Calculate the MEDIAN, and replace any empty values with it:

import pandas as pd

unit = pd.read_csv("resources/data1.csv")

y = unit["Calories"].median()

unit.fillna(y, inplace = True)
print(unit)

# Median = the value in the middle, after you have sorted all values ascending.

# Example
  # Calculate the MODE, and replace any empty values with it:

import pandas as pd

unit = pd.read_csv("resources/Data1.csv")
t = unit["Calories"].mode()[0]
unit.fillna(t, inplace = True)
print(unit)

# Mode = the value that appears most frequently.

# Own notes : With new variable - dropna() is for showing output with new dataframe by ignoring empty cells
              # Without new variable - dropna() using "inplace = True" is for showing output within original dataframe without creating new dataframe. 
              # fillna() is for filling the given value on all empty places in the dataframe 
              # fillna() with specified column only returns new given values on empty places in the specified column name. 
              # Mean = the average value (the sum of all values divided by number of values).
              # Median = the value in the middle, after you have sorted all values ascending.
              # Mode = the value that appears most frequently.
              # Note that we need to put MODE for index number 0




