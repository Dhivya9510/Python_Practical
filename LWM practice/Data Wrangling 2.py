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

     # To Create function for uppercase: 

def uppercase(x):
    return x.upper()    # type: ignore

     # Apply function, show two rows: 

gain = dfm["Name"].apply(uppercase)[0:2]
print(gain)

   
# APPLYING A FUNCTION TO GROUPS: (We can also use the above given method, hence the below methods are the possiblities to write the code to obtain the required)

    # Group rows, apply function to groups: 

fit = dfm.groupby("sex").apply(lambda x: x.count())     # If we creating one+ more rows by using lambda function, the count() function automatically adds the counts catagorywise under the column that mentioned in 'groupby' function. 
print(fit)                                              # Understood the concept. 


# CONCATENATING DATAFRAMES: (Joining dataframes. For that first we need to create two dataframe to concatenate)

    # Create first dataframe

data_a = ({"id" : ['1','2','3']},
          {"First": ["Allen","Benly", "Charles"]},
          {"Last":["Dongles", "Edward", "David"]})
 
dataframe_1 = pd.DataFrame(data_a, columns = ["id","First","Last"])

   # Create another dataframe

data_b = ({"id" : ['4','5','6']},
          {"First": ["Franklin","George", "Martin"]},
          {"Last":["Nutshell", "lenin", "Frank"]})

dataframe_2 = pd.DataFrame(data_b, columns = ["id","First","Last"])

   # Concatenate dataframes by rows: 

Final = pd.concat([dataframe_1, dataframe_2], axis= 0)
print(Final)

   # Concatenate dataframes by columns: 

Finale = pd.concat([dataframe_1, dataframe_2], axis= 1)
print(Finale)

   # Alternatively we can use 'append' to add a new row to a dataframe: 
         # Create row: 

row = pd.Series([10,"Nun","Catie","Bagath"], index = ["id","First","Last"])

        # Append row: 

appended_row = dataframe_1.append(row, ignore_index=True) # type: ignore
print(appended_row)

# MERGING DATAFRAMES: 
       # Creating first dataframe: 

Employee_data = ({"id": ["1","2","3","4"]},
           {"Name"}:["Allen","Bonie","Charlie","Dawson"])

dataframe_emp = pd.DataFrame("Employee_data", columns = ["id", "Name"])

      # Creating another dataframe: 

Sales_data = ({"id": ["1","2","3","4"]},
           {"total_sales":[1234,2345,3456,3214]})

dataframe_sal = pd.DataFrame("Sales_data", columns = ["id", "total_sales"])

      # Merge Dataframes: 
          # Note the below 'on' parameter showing the results with only the same id number in both the dataframes.
          # Here it shows only 3 & 4 (bcz this two is common in both the dataframes.)

jack = pd.merge(dataframe_emp, dataframe_sal, on= "id")
print(jack)         # Merge defaults to inner joints. If we want to do an outer join, we can specify that with the 'how' parameter. 

Queen  = pd.merge(dataframe_emp, dataframe_sal, on= "id", how= "outer")
print(Queen)        # Here you can see the output that actually merges with all the items in both the dataframes. 

           # The same parameter can be used to specify left and right joins. 

king  = pd.merge(dataframe_emp, dataframe_sal, on= "id", how= "left")
print(king)

Prince  = pd.merge(dataframe_emp, dataframe_sal, on= "id", how= "right")
print(Prince)

            # Here in 'left' - you can see it ignores all the 'NaN' in left side and showing only the rows with values filled.
            # Similary Here in 'right' - you can see it ignores all the 'NaN' in the right side and showing only the rows with values filled.