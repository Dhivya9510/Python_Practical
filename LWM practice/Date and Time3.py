# 5.CALCULATING THE DIFFERENCES BETWEEN THE DATES: 

   # You have the two datetime features and want to calculate the time between them for each observation. 
   # Subtract the two date features using Pandas. 

# Load Library: 
import pandas as pd

# Create dataframe: 
df = pd.DataFrame()

# Create two datatime features: 
df["Arrived"] = [pd.Timestamp("01-01-2017"),pd.Timestamp("01-04-2017")]
df["Left"] = [pd.Timestamp("01-01-2017"),pd.Timestamp("01-06-2017")]

# Calculate duration between features: 

Date_difference = df["Left"] - df["Arrived"]
print(Date_difference)

# There are times when the feature we want is the change (delta) between two points in time. 
# For example, we might have the dates a customer check in and checks out of a hotel, but the feature we want is the duration of his stay. 
# Pandas makes this calculation easy using the 'TimeDelta' data type. 

Date_differnces1 = pd.Series(delta.days for delta in (Date_difference)) #type: ignore
print(Date_differnces1)

# (Here it’s just showing the output without mentioning ‘days’ as like previous output.
# As we all know this contains integers (numerical) only as it will easy for ML algorithm to process). 
# Note that this list comprehension has been written inside the 'Series'. 

# 6.ENCODING DAYS OF THE WEEK.

     # You have a vector of dates and want to know the day of week for each date. 
     # Use Panda’s Series - dt.dayofweek.

# Load Library: 
import pandas as pd

# Create dates: 
dates = pd.Series(pd.date_range("2/2/2002", periods= 3, freq = "M"))
days = dates.dt.dayofweek
print(days)

# Here the output will be 3, 6 & 1 means that Thursday, Sunday and Tuesday. 
      # Usually referred - Monday as 0
      # Tuesday as 1
      # Wednesday as 2
      # Thursday as 3
      # Friday as 4
      # Saturday as 5 &
      # Sunday as 6.

    # Knowing the weekday can be helpful if, for instance, we want to compare total sales on Sundays for the past three years, Pandas makes creating a feature vector containing ‘dayofweek’ information easy. 

# 7. CREATING A LAGGED FEATURE: 
       # Generally we are interested in using values in the past to make predictions (this is often called lagging a feature). 
       # You want to create a feature that is lagged in time periods. 
       # Use Panda’s Shift()

# Load Library: 
import pandas as pd
dataframe = pd.DataFrame()

# Create dateframe:

dataframe["Date"] = pd.date_range('1/1/2001', periods= 5, freq= "D")
dataframe["Stock_price"] = [1.1,2.2,3.3,4.4,5.5]

# Lagged values by one row: 
dataframe["previous_days_stock_price"] = dataframe["Stock_price"].shift(1)
print(dataframe)   # You can understand the concept when seeing the output. 

# Very often data is based on regularly spaced time periods (eg., every day, every hour, every three hours).
# And we are interested in using values in the past to make predictions (this is often called lagging a feature). 
# For example, we might want to predict a stock’s price using the price it was the day before. 
# With Pandas, we can use shift to lag values by one row, creating a new feature containing past values. 
# In our solution, the first row for ‘previous_days_stock_price’ is a missing value because there is no previous ‘stock_price’ value. 


# Notes: Date difference can be calculated either by subracting them or else with list comprehension. 
        # Use panda's 'shift' method while creating a lagged feature.    
        # Understand the concept of 'creating a lagged feature'. 

