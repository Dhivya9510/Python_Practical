# HANDLING DATE AND TIME: 

# INTRODUCTION: 
    # Dates & times (datetimes) are frequently encountered during preprocessing for ML, whether the time of a particular sale or the year of some public health statistic. 
    # (Before put the ‘data and time’ data into ML, we need to get it to the pre-processing with the method called ‘datetime’)
    # ( If you see your time-date as strings, you need to convert it in to the timestamp format using ‘to_datetime()’ function in pandas.)

# 1.	Converting Strings to Dates: 

      # Given a vector of strings representing dates and times, you want to transform them into time series data. 

# Load Libraries:
import numpy as np
import pandas as pd

# Create Strings: 
date_strings = np.array(['03-04-2005 11:35 PM', '23-05-2010 12:01 AM', '04-09-2009  09:09 PM']) # Date & time represented as strings. 

# Convert to datetimes: 

datetimes = [pd.to_datetime(date, format= '%d-%m-%Y %I:%M %p') for date in date_strings] 
print(datetimes)

# We might also want to add an argument to the ERRORS parameters to handle problems. 

dt_with_presentingerr = [pd.to_datetime(date, format= '%d-%m-%Y %I:%M %p', errors = "coerce") for date in date_strings]
print(dt_with_presentingerr)

# In general, ‘date & time’ would not consider any errors – whatever the code we written, the program performed, so that we need to write the parameter called ‘errors=”coerce”’ – this will add and shows the value called ‘NaT’ (i.e., a missing value) 
# When dates and times come as strings, we need to convert them into a datatype Python can understand. While there are a number of python tools for converting strings to datetime, following our use of pandas in other recipes we can use ‘to_datetime’ to conduct the transformation. 
# One obstacle to strings representing dates and times is that the format of the strings can vary significantly between data sources. 
# For example, one vector of dates might represent March 23rd, 2015 while another might use “3|23|2015”.
#  We can use the format  parameter to specify the exact format of the string. 

# 2. HANDLING TIME ZONES: 
                           
        # You have the time-series data and want to add or change time zone information. 
        # Eg: Your US client’s time zone should be in IST for your analysis. 
        # If not specified, pandas object has no time zone. However, we can add a time zone using tz during creation: 
        # Eg: You might check IST for your Chicago google meet timing.

# Load Library
import pandas as pd

# Create datetime 
creating_datetime = pd.Timestamp('2017-05-01 06:00:00', tz= "Europe/London")
print(creating_datetime)

  # We can add a time zone to a previously created datetime using tz.localize:

# Create datetime :
date = pd.Timestamp('2017-05-01 06:00:00')
# Create Timezone:
date_in_london = date.tz_localize("Europe/London")
print(date_in_london)

  # We can also convert to a different time zone: 

# Change time zone: 
Africa = date_in_london.tz_convert("Africa/Abidjan")
print(Africa)

# Finally, panda's series objects can apply tz_localize and tz_convert to every element: 
# Previously we created a single timestamp, now we are going to create a series of timestamp. 

# Create three dates:
Dates = pd.Series(pd.date_range("2/2/2002", periods= 3, freq= 'M')) # Add pd.daterange for Pd.Series. 
print(Dates)

# Now apply it to the timezone:
timezone = Dates.dt.tz_localize("Africa/Abidjan")
print(timezone)

# Pandas supports two sets of strings representing timezones: however, I suggest using pytz library’s strings. 
# We can see all the strings used to represent time zones by importing all-timezones:

# Load Library:
from pytz import all_timezones
# Show two time zones: 
time_zones = all_timezones[0:2]
print(time_zones)


# Very important note :When you create a series of time stamp, you should write ‘dt.’ before applying ‘tz_localize’. 



