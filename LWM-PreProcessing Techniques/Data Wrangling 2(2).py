import pandas as pd
import numpy as np

# GROUPING ROWS BY TIME (NUMERICAL)
     
     # We don't have the dataset for 'time'. So we created it by our own. 
     # Create date range.(For this use, 'date_range' function with the required parameters. 

time_index = pd.date_range("06/06/2017", periods = 100000, freq = '30S')   
print(time_index)

     # Create Dataframe

df  = pd.DataFrame(index = time_index)
print(df)
 
     # Create a new column called 'Sale_Amount' of random values. 

df["Sale_Amount"] = np.random.randint(1,10,100000)
print(df)

     # Group rows by week, Calculate sum per week. 

kit = df.resample("W").sum()
print(kit)
   
     # Group by two weeks, Calculate mean. 

lock = df.resample("2W").mean()
print(lock)
   
     # Group by month, Count rows. 

goat = df.resample("M").count()
print(goat)

     # Group by month, count rows (Here we use 'label' parameter - this is nothing but the starting of the month or ending of the month that indicates 'label = right/ label = left)

hen = df.resample("M", label = "left").count()
print(hen)   # This is not much explained detailedly bcz he said this is not that much important thing. 

