# Pandas Read CSV

# Read CSV Files
  # A simple way to store big data sets is to use CSV files (comma separated files).
  # CSV files contains plain text and is a well know format that can be read by everyone including Pandas.
  # In our examples we will be using a CSV file called 'data.csv'.

# Download data.csv. or Open data.csv

# Example:
   # Load the CSV into a DataFrame:

import pandas as pd

horse = pd.read_csv("resources/data.csv")
print(horse.to_string())

# Tip: use to_string() to print the entire DataFrame.

# If you have a large DataFrame with many rows, Pandas will only return the first 5 rows, and the last 5 rows:

# Example
     # Print the DataFrame without the to_string() method:

import pandas as pd

horse = pd.read_csv("resources/data.csv")
print(horse)

# max_rows
  # The number of rows returned is defined in Pandas option settings.
  # You can check your system's maximum rows with the pd.options.display.max_rows statement.
  # Example
     # Check the number of maximum returned rows:


import pandas as pd

print(pd.options.display.max_rows)

#In my system the number is 60, which means that if the DataFrame contains more than 60 rows, the print(df) statement will return only the headers and the first and last 5 rows.
# You can change the maximum rows number with the same statement.
# Example
   # Increase the maximum number of rows to display the entire DataFrame:


import pandas as pd

pd.options.display.max_rows = 200  # Here 200, the number may more than 169. 

horse = pd.read_csv("resources/data.csv")

print(horse)

# Own notes: Here 200, (Any value we can put but the number may more than 169)  
           # 169 are the total number  of rows displayed with 'to_string()' in result took data in data.csv.
           # Without 'to_string()', the result would display the first 5 rows and last 5 rows excluding headings. 
           # Only with print(horse) with defined number of rows returned - we can get the result of whole data.  