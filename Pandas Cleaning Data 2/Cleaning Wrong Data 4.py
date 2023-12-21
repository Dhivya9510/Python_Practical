# Pandas - Fixing Wrong Data:

# Wrong Data
  # "Wrong data" does not have to be "empty cells" or "wrong format", it can just be wrong, like if someone registered "199" instead of "1.99".
  # Sometimes you can spot wrong data by looking at the data set, because you have an expectation of what it should be.
  # If you take a look at our data set, you can see that in row 7, the duration is 450, but for all the other rows the duration is between 30 and 60.
  # It doesn't have to be wrong, but taking in consideration that this is the data set of someone's workout sessions, we conclude with the fact that this person did not work out in 450 minutes.

# Replacing Values
  # One way to fix wrong values is to replace them with something else.
  # In our example, it is most likely a typo, and the value should be "45" instead of "450", and we could just insert "45" in row 7:
  # ExampleGet your own Python Server
     # Set "Duration" = 45 in row 7:

import pandas as pd

fox = pd.read_csv("resources/Data1.csv")

fox.loc[7, "Duration"] = 45   # note the square bracket. 

print(fox.to_string())

# For small data sets you might be able to replace the wrong data one by one, but not for big data sets.
  # To replace wrong data for larger data sets you can create some rules, e.g. set some boundaries for legal values, and replace any values that are outside of the boundaries.

# Example
  # Loop through all values in the "Duration" column.
  # If the value is higher than 120, set it to 120:

import pandas as pd

fold = pd.read_csv("resources/Data1.csv")

for c in fold.index:
    if fold.loc[c, "Duration"] >120:
        fold.loc[c,"Duration"] = 55
print(fold.to_string())

# Removing Rows
  # Another way of handling wrong data is to remove the rows that contains wrong data.
  # This way you do not have to find out what to replace them with, and there is a good chance you do not need them to do your analyses.
  # Example
     # Delete rows where "Duration" is higher than 120:

import pandas as pd

fold = pd.read_csv("resources/Data1.csv")
 
for u in fold.index:
   if fold.loc[u, "Duration"] >120:
       fold.drop(u, inplace = True)  # To remove the row in which duration is more than 120, we need to use 'DROP'
print(fold.to_string())

# Own notes : For replacing the wrong data - we have to search the row of wrong data first. For that we should use LOC function. 
            # To change the high number of wrong data, we should use LOOP i.e FOR LOOP with the IF condition
            # Note that ALWAYS we should use SQUARE BRACKET near LOC function. 
            # To REMOVE THE ROW IN ORIGINAL DATASET - we need to use DROP function along with INPLACE = TRUE. 

        

