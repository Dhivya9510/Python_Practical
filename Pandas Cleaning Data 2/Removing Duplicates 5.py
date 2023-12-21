# Pandas - Removing Duplicates:

# Discovering Duplicates
   # Duplicate rows are rows that have been registered more than one time.

# By taking a look at our test data set, we can assume that row 11 and 12 are duplicates.
# To discover duplicates, we can use the duplicated() method.
# The duplicated() method returns a Boolean values for each row:

# Example:
  # Returns True for every row that is a duplicate, othwerwise False:

import pandas as pd

hen = pd.read_csv("resources/Data1.csv")
print(hen.duplicated())

# Removing Duplicates
  # To remove duplicates, use the drop_duplicates() method.

# Example
  # Remove all duplicates:
import pandas as pd

hen = pd.read_csv("resources/Data1.csv")
hen.drop_duplicates(inplace = True)

# Remember: The (inplace = True) will make sure that the method does NOT return a new DataFrame, but it will remove all duplicates from the original DataFrame.


# Own notes: DUPLICATED() & DROP_DUPLICATES() are the two functions used here in Cleaning Duplicates.
          # print(x.duplicated()) & x.drop_duplicates(inplace = True) are the two formats
