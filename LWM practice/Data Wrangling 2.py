# DELETING A COLUMN: 
     # The best way to delete a column is to use 'drop' with the parameter 'axis =1' (ie. Column axis)
   
     # Load data

import pandas as pd
dfm = pd.read_csv("url")

     # Delete column:

bgm = dfm.drop("Sex", axis=1).head(2)
print(bgm)

gm = dfm.drop(["Sex", "Age"], axis=1).head(2)  # We need to put it in list if we want to delete multiple columns. 
print(gm)

    # If a column does not have a name (which can sometimes happen), you can drop it by it's column index using dfm columns. 

hop = dfm.drop(dfm.columns[1], axis=1).head(2)
print(hop)

     # To delete multiple columns with it's index number - follow the below: 

run = dfm.drop(columns=["Col1", "Col2", "Col3"], axis= 1).head()
print(run)


# DELETING ROWS:
 
    # Delete rows, show first two rows of output. 

nun = dfm[dfm["sex"] != "Male"].head()
print(nun)

    # 