# 3. SELECTING DATES AND TIMES: 

     # Here we are going to see ‘How to select and get the Date& Time’ from our data-frame or else string represented data series.
     # And also how to convert our datetime into multiple features? 

  # You have a vector of dates and you want to select one or more: 

  # Import Library
import pandas as pd

  # Create Dataframe
df = pd.DataFrame()

  # Create datetimes
df['Date'] = pd.date_range('1/1/2001', periods= 100000, freq='H') 
  
  # Due to the above code give so many outputs - we will go ahead selecting only observations between two datetimes: 

selected_dates1 = df[(df["Date"] > '2002-1-1 01:00:00') & (df["Date"] <= '2002-1-1 04:00:00')]
print(selected_dates1)

# Alternatively, we can set the date column as the Dataframe's index and then slice using loc: 

   # Set Index: 
df = df.set_index(df["Date"])

   # Select observations between two datetimes: 
selected_dates2 = df.loc['2002-1-1 01:00:00' : '2002-1-1 04:00:00']
print(selected_dates2)

  # Wheather we use boolean condition or index slicing is situation dependant. 
  # If we wanted to do some complex time series manipulation, it might be worth the overhead of setting the date column as the index of the dataframe. 
  # But if we wanted to do some simple data wrangling, the boolean conditions might be easier. 

# 4. BREAKING UP DATE DATA INTO MULTIPLE FEATURES: 
      # You have a column of dates and times and you want to create a feature for year, month, day, hour and minute.
      # Use panda’s Series.dt’s time properties: 

# Load Library:
import pandas as pd

# Create dataframe:
dataframe = pd.DataFrame()

# Create dates: 
dataframe["Dates"] = pd.date_range('1/1/2001', periods= 150, freq= 'W')
print(dataframe)

# Create features for Year, Month, Day, Hour and Minute. 
dataframe["Year"] = dataframe["Dates"].dt.year
dataframe["Month"] = dataframe["Dates"].dt.month
dataframe["Date"] = dataframe["Dates"].dt.date
dataframe["Hour"] = dataframe["Dates"].dt.hour
dataframe["Minute"] = dataframe["Dates"].dt.minute

dataframe.head(3)  # Output not showing due to the variable input when compare to Jupitar notebook as showing in LWM. 

# Sometimes it can be useful to break up a column of dates into components. 
# For example, we might want a feature that just includes the year of the observation or we might want only to consider the month of some  observation so we can compare them regardless of year. 


# Notes: 
    # There are two ways to selecting date&time. One is by using arithmetic operatiors like <,>,&... 
    # And the another method is using 'slicer' by inputing 'loc' function. (suitable for large amount of column data)
           # In the slicing method - we need to set the index to locate. 
    # Note that we always use ‘dt’ when we use ‘series’. 
    # Remember that We need to use 'dt' in order to seperate the features year, month, date, hours & minutes separately. Line 50 to 54. 

