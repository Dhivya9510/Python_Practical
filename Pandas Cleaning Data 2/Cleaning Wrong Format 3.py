# Pandas - Cleaning Data of Wrong Format:

# Data of Wrong Format
  # Cells with data of wrong format can make it difficult, or even impossible, to analyze data.
  # To fix it, you have two options: remove the rows, or convert all cells in the columns into the same format.

# Convert Into a Correct Format
  # In our Data Frame, we have two cells with the wrong format. Check out row 22 and 26, the 'Date' column should be a string that represents a date:


# Let's try to convert all cells in the 'Date' column into dates.
# Pandas has a to_datetime() method for this:

# Example:
  # Convert to date:


import pandas as pd

tag = pd.read_csv("resources/Data1.csv")

tag['Date'] = pd.to_datetime(tag['Date'],format='mixed')  # Hubby checked this, per tutorial, it showing error - we need to put FORMAT = 'MIXED' to get the data. 
print(tag.to_string())

# As you can see from the result, the date in row 26 was fixed, but the empty date in row 22 got a NaT (Not a Time) value, in other words an empty value. 
# One way to deal with empty values is simply removing the entire row.

# Removing Rows
  # The result from the converting in the example above gave us a NaT value, which can be handled as a NULL value, and we can remove the row by using the dropna() method.

# Example
   # Remove rows with a NULL value in the "Date" column:

import pandas as pd

tag = pd.read_csv("resources/Data1.csv")
tag.dropna(subset = ["Date"], inplace = True)
print(tag.to_string())

# The below are the combo of two:

import pandas as pd

tag = pd.read_csv("resources/Data1.csv")
tag["Date"] = pd.to_datetime(tag["Date"], format = "mixed")
tag.dropna(subset = ["Date"], inplace = True)
print(tag)

# Own notes : There are two methods showing here to fix WRONG FORMAT - REMOVING ROWS / CONVERT INTO SAME FORMAT USING FUNCTION.
            # In DATETIME() method to format the date, as per the tutorial,it showing error - we need to put FORMAT = 'MIXED' to get the data. 
            # Note to remove rows, we need to add SUBSET AFTER DROPNA in variable. 