# THE STRFTIME() METHOD:
  # The datetime objecthas a method for formatting date objects into readable strings. 
  # The method is called strftime(), and takes one parameter, format, to specify the format of the returned string:

  # Example:
    # Display the name of the month:

import datetime

h = datetime.datetime(2023,4,6)

print(h.strftime("%B"))   # To return the month, we need to use '%B' with 'strftime' method. 

# for futher '%' alphabets refer - https://www.w3schools.com/python/python_datetime.asp