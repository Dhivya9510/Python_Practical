# 8. USING ROLLING TIME IN WINDOWS: (Per my understanding – it’s like a cumulative)

       # Can we apply our Statistical methods such as mean, median, mode and so on.. with our Panda’s dataframes to get the desired output? 
       # The answer is ‘Yes’ – with the help of ‘Using rolling time in windows’.

       # Given time series data, you want to calculate some statistic for a rolling time. 

# Load Library: 
import pandas as pd

# Create datetimes: 
time_index = pd.date_range("01/01/2010", periods= 5, freq= "M")

# Create datetime, set index: 
dataframe = pd.DataFrame(index=time_index)

# Create feature: 
dataframe["Stock_price"] = [1,2,3,4,5]
print(dataframe)

      # So far the above thing is an usual one. Now we will going to apply some statistical methods on it. 

 # calculate rolling mean: 

rolling_mean = dataframe.rolling(window=2).mean()   # For better understanding refer the note's screenshot. 
print(rolling_mean)     
      # 'windows=2' means take the first two values and do those mean. 
      # Here we took the values of 1&2 - sum is 3, divided by 2 (number of observation (mean))
      # So, 3/2 is 1.5. Similarly do the same thing for the next others. 


# Rolling (also called moving) time windows are conceptually simple but can be difficult to understand at first. 
# Imagine we have monthly observations for a stock’s price. It is often useful to have a time window of a certain number of months.

# Another way to put it: our three-month time window “walks” over the observations, calculating the window’s mean at each step. 
# Panda’s ‘rolling’ allows us to specify the size of the windows using window and then quickly calculate some common statistics, including the max value (max()), mean value (mean()), count of values (count()), and rolling correlation (corr()). 
# Rolling means are often used to smooth out time series data because using the mean of the entire time window dampens the effect of short-term fluctuations. 


# 9. HANDLING MISSING DATA IN TIME SERIES: 

       # You have missing values in time series data. 
       # In addition to the missing data strategies previously discussed, when we have time series data we can use interpolation to fill in gaps caused by missing values. 

# Load Libraries: 
import numpy as np
import pandas as pd

# Create date: 
time_index = pd.date_range("01/01/2010", periods= 5, freq= "M")

# Create datetime, set index: 
dataframe = pd.DataFrame(index=time_index)

# Create feature with a gap of missing values: 
dataframe["sales"] = [1.0,2.0,np.nan,np.nan,5.0]

# Interpolate missing values: 
interpolate = dataframe.interpolate()
print(interpolate)

# (See the magic that when we applied the INTERPOLATE function – it fills the right values in the missing places as showing in the output below). 
# (We use ‘Interpolate’ function exclusively under ‘Date and time’ handlings). 
# (We used this function only when the values are constantly occurring (exactly saying the distance between the data points should be linear). Example: 1,3,5,7,np.nan,11). 
# (Here the distance between two elements is 2 units (3-1 = 2, 5-3 = 2, 7-5 = 2..). So, it interpolates the next missing number as 9). 
# (What if 1,4,5,8,3,np.nan,no.nan,np.nan,12? Like this, in some places – ‘Interpolate’ function could not be used). 
# (In such instance – we will use, forward-filling or backward-filling method). 

# That means, alternatively, we can replace missing values with the last known value (i.e – forwardfilling). 
# We can also replace missing values with the latest known value (i.e – back-filling)

forward_fill = dataframe.ffill()
print(forward_fill)

    # Number 2 will be substituted forward-wise in the place of missing values. 

backward_fill = dataframe.bfill()
print(backward_fill)

     # Number 5 will be substituted backward-wise in the place of missing values. 

# Interpolation is a technique for filling in gaps caused by missing values by, in effect, drawing a line or curve between the known values bordering the gap and using that line or curve to predict reasonable values. 
# Interpolation can be particularly useful when the time intervals between are constant, the data is not prone to noisy fluctuations, and the gaps caused by missing values are small. 
# For example, in our solution a gap of two missing values are bordered by 2.0 and 5.0. By fitting a line started at 2.0 and ending at 5.0, we can make reasonable guesses for the two missing values in between of 3.0 and 4.0. 
# If we believe the line between the two known points is non-linear, we can use interpo late's method to specify the interpolation method: 

   # Interpolate missing values: 

method = dataframe.interpolate(method= "quadratic")
print(method)

# (Inside the ‘Interpolate’s method – there is a parameter called “method”).  
# (There are many methods such as Quadratic, linear, polynomial, pad, etc.. (You can check in google about this various methods)). 
# (Here we going to use ‘Quadratic’ method whereas our computer understands that there are some quadratic relations among the missing values and imputed the data based on that)

# Finally there might be cases when we have large gaps of missing values and do not want to interpolate values across the entire gap.
#  In these cases, we can use limit to restrict the number of interpolated values and limit_direction to set whether to interpolate values forward from at the last known value before the gap or vice versa. 

# (Simply saying, when we do not want to find the values for entire missing data, but for some missing data, here we can use the parameter called ‘limit’ and it’s ‘limit-direction’).

   # Interpolate missing values: 
limit_method = dataframe.interpolate(limit= 1, limit_direction= "forward")
print(limit_method)

# Back-filling and forward-filling can be thought as a form of naïve interpolation, where we draw a flat line from a known value and use it to fill in missing values. 
# One minor advantage back- and forward filling have over interpolation is the lack of the need for known values on both sides of missing value(s). 


# Note that when writing code under - 'rolling windows', we should include the 'windows' parameter. 
