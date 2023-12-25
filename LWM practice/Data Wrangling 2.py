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

hop = dfm.drop(dfm.columns[1], axis=1).head(2)  # Note here we should not use 'index' as a parameter, instead we have to follow this. 
print(hop)

     # To delete multiple columns with it's index number -> follow the below: 

run = dfm.drop(columns=["Col1", "Col2", "Col3"], axis= 1).head()
print(run)

# sample comment
# DELETING ROWS:
    # Show the output of first two rows only with 'Female' under 'Sex' column.
    
candy = dfm[dfm["Sex"] != "Male"].head(2)   # Note that We can process the question with code without drop() function to use 'axis'. 
print(candy)

    # Delete rows, show first two rows of output.

nun = dfm.drop(["Sex"], axis=0).head()
print(nun)       # While technically you can use the drop method like above. dfm.drop([0,1], axis =0) to drop the first two rows).
                 # - a more practical method is simply to wrap a boolean condition inside df[]. 
                 # The reason is because we can use the power of conditionals to delete either a single row or (far more likely) many rows at once. 
                 # Example below to process question by deleting a particular row and giving multiple rows as output. 
     
     # Delete rows and show the first two rows of output except the name "Allison Watson"

sure = dfm[dfm["Name"] != "Allison Watson"].head(2)
print(sure)       

     # Delete rows, show first two rows of output by index number

gun = dfm.drop(dfm.index[2:], axis = 0, inplace = False)
print(gun)       # In video, I did not understood tha given code & no explantion for that as well. 
                 # so note that I searched the here written code in CHATGPT. 

# DROPPING DUPLICATE ROWS: 
    # By using drop_duplicates() function, we can took out the duplicate rows. 
    # Drop Duplicates, show just two rows of output. 

git = dfm.drop_duplicates()
print(git)         # Note that the code did not actually drop any rows. Because IN OUR DATAFRAME doesn't contains any duplicate rows. you can check this by the following:

print("No.of.rows in Original dfm:" , len(dfm))
print("No.of.duplicate rows in dfm:", len(dfm.drop_duplicates())) # Result showing the same. Because IN OUR DATAFRAME doesn't contains any duplicate rows.

    # Drop duplicates: 
          # Please note the below case is something different. 

ops = dfm.drop_duplicates(subset= ["Sex"])
print(ops)
               # Just understand that 'subset' is one of the parameter in 'drop_duplicates'
               # Here it gives the unique items without duplicates under 'sex' columns from top to bottom. 
               # In case if we want from bottom to top, we just need to put, 'keep' parameter like below: 

oops = dfm.drop_duplicates(subset= ["Sex"], keep= "last")
print(oops)

# GROUPING ROWS BY VALUES:   (CATEGORICAL)
    # Group rows by the values of the column 'Sex', calculate 'Mean'

ink = dfm.groupby("sex").mean()
print(ink)

    # What's the survived count of both male and female. 
    # Group rows and count rows. 

ment = dfm.groupby("Sex")["Survived"].count()
print(ment)

    # We can access multiple rows also in groupby() function
    # Group rows, calculate mean. 

king = dfm.groupby(["Sex", "Survived"])["Age"].count()
print(king)           # Output looks like a mini-pivot table because of more than one feature. 

#  LOOPING OVER A COLUMN: 

    # Print first two names uppercased: 

for name in dfm["Name"][0:2]:
    print(name.upper())

    # In addition to loops (often called for loops), we can also use list comprehensions: 

state = name.upper() for name in dfm["Name"][0:2]   # type: ignore
print(state)

# APPLYING A FUNCTION OVER ALL ELEMENTS IN A COLUMN: 

     # Create function: 



     # Apply function, show two rows: 


   
# APPLYING A FUNCTION TO GROUPS:

    # Group rows, apply function to groups: 



# CONCATENATING DATAFRAMES: 

    # 