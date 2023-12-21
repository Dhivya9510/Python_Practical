# 1.  Pandas DataFrame abs() Method 
      # Return a DataFrame with the absolute value of each value
      # Example:
         # Find the absolute value of each value in the DataFrame:

import pandas as pd
yolk = [[-1,2,-3],[4,-5,-6]]
unit = pd.DataFrame(yolk)              # First we need to put the 2D array into DataFrame before print it as in abs()
print(unit.abs())

      # Note: This function does NOT make changes to the original DataFrame object.

# 2. Pandas DataFrame add() Method
      # The add() method adds each value in the DataFrame with a specified value.
      # Example
        # Add 10 to each value in the DataFrame:

import pandas as pd
hat = {"Numbers":[20,25,30],"Days":[5,10,15]}
good = pd.DataFrame(hat)
print(good.add(10))

# 3. Pandas DataFrame add_prefix() Method
     # Definition and Usage
          # The add_prefix() method inserts the specified value in front of the column label.
          # To add a value after the column label, use the  add_suffix() method.

import pandas as pd
great = {"Age":[20,25,30,35,40], "Qualification":["Yes","No","Yes","No","Yes"]}
new_great = pd.DataFrame(great)
print(new_great.add_prefix("Person_"))

         # Note: This method does not change the original DataFrame.

# 4. Pandas DataFrame add_suffix() Method
       # The add_suffix() method inserts the specified value at the end of each column label.
import pandas as pd
horse = {"Roll no.":[23,25,27,29],"Strength":[30,29,28,27]}
new_horse = pd.DataFrame(horse)
print(new_horse.add_suffix("of a Class"))

       # Note: This method does not change the original DataFrame.

# 5. Pandas DataFrame agg() Method
      # The agg() method allows you to apply a function or a list of function names to be executed along one of the axis of the DataFrame, default 0, which is the index (row) axis.
      #  the agg() method is an alias of the aggregate() method.

import pandas as pd
hen = {"P":[1,2,3],"Q":[5,6,7]}
new_hen = pd.DataFrame(hen)
r = new_hen.agg(["sum"])
print(r)

      # Note: A DataFrame or a Series object, with the changes.This function does NOT make changes to the original DataFrame object.
            # Note the code syntax, line 51. It's slight different from previous functions. 


# 6. Pandas DataFrame all() Method

# ExampleGet your own Python Server
   # Check if all values in each row (index) are True:

import pandas as pd

scratch_data = [[True, True, True], [True, True, False]]   # It's check indexwise returning the result. 

h = pd.DataFrame(scratch_data)
print(h.all())

# Definition and Usage
   # The all() method returns one value for each column, True if ALL values in that column are True, otherwise False.
   # By specifying the column axis (axis='columns'), the all() method returns True if ALL values in that axis are True.

# Return Value
   # A Series of True and False values.
   # If the level argument is specified, this method will return a DataFrame object.
   # This function does NOT make changes to the original DataFrame object.

#  7. 




