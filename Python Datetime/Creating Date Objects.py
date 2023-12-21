
# CREATING DATE OBJECTS
  # To create a date, we can use the datetime() class (constructor) of the datetime module.
  # The datetime() class requires three parameters to create a date: year, month, day.

  # Example:
     # Create a date object:

import datetime

i = datetime.datetime(2023,6,4)
print(i)


# The datetime() class also takes parameters for time and timezone (hour, minute, second, microsecond, tzone), but they are optional, and has a default value of 0, (None for timezone).