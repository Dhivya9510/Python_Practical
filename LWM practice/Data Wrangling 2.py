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

     # To delete multiple columns with it's index number -> follow the below: 

run = dfm.drop(columns=["Col1", "Col2", "Col3"], axis= 1).head()
print(run)

# sample comment
# DELETING ROWS:
 
    # Delete rows, show first two rows of output. 

candy = dfm[dfm["Sex"] != "Male"].head(2)   # Note that We can process the question with code without drop() function to use 'axis'. 
print(candy)


nun = dfm.drop(["Sex"], axis=0).head()
print(nun)       # While technically you can use the drop method like above. df.drop([0,1], axis =0) to drop the first two rows).
                 # - a more practical method is simply to wrap a boolean condition inside df[]. 
                 # The reason is because we can use the power of conditionals to delete either a single row or (far more likely) many rows at once. 
                 # Example below to process question by deleting a particular row and giving multiple rows as output. 
     
     # Delete rows, show first two rows of output.

sure = dfm[dfm["Name"] != "Allison Watson"].head(2)
print(sure)       

     # Delete rows, show first two rows of output by index number

gun = dfm.drop(dfm.index[2:], axis = 0, inplace = False)
print(gun)       # In video, I did not understood tha given code & no explantion for that as well. 
                 # so note that I searched the here written code in CHATGPT. 

# DROPPING DUPLICATE ROWS: 
