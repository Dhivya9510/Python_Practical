# DATE OUTPUT:

  # When we execute the code from the example above the result will be:
     # 2023-04-06 08:19:32.249902
  # The date contains year, month, day, hour, minute, second, and microsecond.

  # The datetime module has many methods to return information about the date object.
  
  # Here are a few examples, you will learn more about them later in this chapter:

  # Example:
     # Return the year and name of weekday:

import datetime

y = datetime.datetime.now()

print(y.year)
print(y.strftime("%A"))    # To return the weekday, we need to use '%A' with 'strftime' method. 