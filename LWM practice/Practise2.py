# Import numpy and pandas
# Import Visualization libraries and set % matplotlib inline
# Read in the csv file as a dataframe called df
# Check the info() of the df
# Check the head() of the df

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style("whitegrid")                # This set_style is default for better visualization.

df = pd.read_csv("resources/911.csv")     # We loaded this as asked.

df.info()

df.head()
print(df)
                                      
# Basic Questions: 

# What are the top 5 zipcodes for 911 calls? 

all = df["zip"].value_counts().head()
print(all)                                      # “Value_counts()” is generally used to showing the output with the AlphaValues list with its max count (descending to ascending)

# What are the top 5 zipcodes (twp) for 911 calls? 

ball = df["twp"].value_counts().head()
print(ball)    

# Take a look at the 'title' column, how many unique title codes are there? 

cherry = df["title"].nunique()        # The question is 'how many', so the answer should be in number. 
print(cherry) 

# CREATING NEW FEATURES. 
  
  # In the 'title's column - there are "Reasons/Departments" specified before the title code. 
  # These are EMS, Fire and Traffic. 
  # Use .apply() with a custom lambda expression to create a new column called "Reason" that contains this string value.
  # For eg: If the title column value is EMS: BACK PAIN/ INJURY, the reason column value would be EMS. 

df["Reason"] = df["title"].apply(lambda title : title.split(":")[0])
print(df["Reason"].head())

# What is the most common reason for 911 call based off of this new column? 

desk = df["Reason"].value_counts()
print(desk)

# Now use Seaborn to create a countplot of 911 calls by reason. 

sns.countplot(x = "Reason", data = df)
plt.show()


# Now let us begin to focus on time information. 
 # What is the data type of the objects in the timestramp column? 

egg = type(df["timeStamp"][0])   #Why [0]? because type of df is 'pandas.series'. We need to find out the data type, so we should put [0] so that it would taken the first index row of the timstamp resulting class 'string'.
print(egg)                                         


# You should have seen that these timestamps are still strings. Use 'pd.to_datetime' to convert the timestamp column from strings to datetime objects. 
   # Notes: # ‘Times’ are all should be stored in the Timeformat in Pandas by using to_datetime() format, so that we can access it easily in to the ‘datetime’ objects.  
            #‘Timeformat’ has many attributes such as year, month, date, minutes, seconds, hours…If we stored the ‘timeformat’ in strings, it would be a bit complex and we have to write each and every time. 

df["timeStamp"] = pd.to_datetime(df["timeStamp"])     # We can check the type now.
folk = type(df["timeStamp"][0])                       # Output is <class 'pandas._libs.tslibs.timestamps.Timestamp'> - Type has changed now. 
print(folk)                                                             

# Now that the TimeStamp columns are actually DateTime objects,Create 3 columns called - Hour, Month & Day of the week.
  # Time Format Attributes. 

import datetime as dt

# Hour

df["Hour"] = df["timeStamp"].dt.hour 
print(df["Hour"])

# Month

df["Month"] = df["timeStamp"].dt.month
print(df["Month"])

# dayofWeek

df["Dayofweek"] = df["timeStamp"].dt.dayofweek
print(df["Dayofweek"])


# Days Directed map with Integers. 

dmap = {0: "Sun", 1:"Mon", 2: "Tue", 3: "Wed", 4: "Thu", 5: "Fri", 6: "Sat"}

print(df["Dayofweek"].map(dmap))


# Now use Seaborn to create a countplot of the day of week column with the hue based off the reason column. 

sns.countplot(x = "Dayofweek", data = df, hue = "reason")
plt.show()

# Now use Seaborn to create a countplot of the Month column with the hue based off the reason column. 

sns.countplot(x = "Month", data = df, hue = "reason")
plt.show()

# Now use Seaborn to create a countplot of the hour column with the hue based off the reason column. 

sns.countplot(x = "Hour", data = df, hue = "reason")
plt.show()

# WHEN YOU SEE THE OUTPUT OF MONTH CHART, YOU MAY FIND THE MISSING DATA FOR THE MONTHS 9,10 & 11.
  # WE CAN USE DREW THE PLOT FOLLOWED BY THE 'GROUPBY()' FUNCTION TO GET THE REQUIRED DATA. 
  # NOTE THAT WE MUST USE ONE AGGREGATE FUNCTION WHEN WE USE 'GROUPBY()' FUNCTION. HERE WE USE 'COUNT()' FUNCTION. 

bymonth= df.groupby("Month").count()
print(bymonth.head())                    # Until here the output not showing the missing data. 
     
# Now create a simple plot off of the dataframe indicating the count of calls per month. 

                           # We can give any column title, to obtain the required data via graph. 
                           # So now you can get the data for the months of 9,10 & 11 through the chart. 

# Now see if you can use seaborn's lmplot() to create a linear fit on the number of calls per month townshipwise. 
# Keep in mind you may need to reset the index to a column. 
# (because you mentioned "bymonth" in data parameter, so you need to give "reset_index" so that it can taken also itself the groupby() function with the finded missing data)



# Create a new column called 'Date' that contains the date from the timeStamp column. 
# You'll need to use apply along with the .date() method. 




# Now groupby() this date column with the count() aggregate and create a plot of counts of 911 calls. 

                                                # Can take any column title, our choice - not neccessary to took only "twp"


# Now create this plot but create 3 seperate plots with each plot representing a reason (Traffic, EMS & Fire) for the 911 calls. 
 # Understand the format below for your future reference. 







