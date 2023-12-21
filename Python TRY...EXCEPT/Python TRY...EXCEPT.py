# Python Try Except
  # The try block lets you test a block of code for errors.
  # The except block lets you handle the error.
  # The else block lets you execute code when there is no error.
  # The finally block lets you execute code, regardless of the result of the try- and except blocks.

# Exception Handling:
  # When an error occurs, or exception as we call it, Python will normally stop and generate an error message.
  # These exceptions can be handled using the try statement:
  # Example: The try block will generate an exception, because x is not defined:

try:
    print(x)
except:
    print("Something went wrong")

# Since the try block raises an error, the except block will be executed.
# Without the try block, the program will crash and raise an error:
 # Example: This statement will raise an error, because x is not defined:
    # print(x)

# Many Exceptions
 # You can define as many exception blocks as you want, e.g. if you want to execute a special block of code for a special kind of error:
  # Example: Print one message if the try block raises a NameError and another for other errors:

try:
    print(x)
except NameError:                       # Usually we received 'Traceback error message with Name error in last line, by mentioning the 'NameError' beside 'Except', we can only get the NameError directly wihtout messy lines.
    print("Something went wrong")
except:
    print("Nothing went wrong")

# Else:
  # You can use the else keyword to define a block of code to be executed if no errors were raised:
  # Example: In this example, the try block does not generate any error:

try:
    print("Dear")
except:
    print("Something went wrong")
else:
    print("Nothing went wrong")

# Finally:
 # The finally block, if specified, will be executed regardless if the try block raises an error or not.
 # Example: 

try:
    print(x)
except:
    print("Something went wrong")
finally:
    print("All done now")

# Raise an exception:
 # As a Python developer you can choose to throw an exception if a condition occurs.
 # To throw (or raise) an exception, use the raise keyword.
 # Example: Raise an error and stop the program if x is lower than 0:

y = -4

if y<0:
    raise Exception("Below Zeros are not allowed")

#The raise keyword is used to raise an exception. 
# You can define what kind of error to raise, and the text to print to the user.
# Example: Raise a TypeError if x is not an integer:

x = "Hello"

if not type(x) is int:
    raise TypeError("It is not an integer")







