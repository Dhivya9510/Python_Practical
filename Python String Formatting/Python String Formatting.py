# Python String Formatting:
  # To make sure a string will display as expected, we can format the result with the format() method.

# String format():
 # The format() method allows you to format selected parts of a string.
 # Sometimes there are parts of a text that you do not control, maybe they come from a database, or user input?
 # To control such values, add placeholders (curly brackets {}) in the text, and run the values through the format() method:
 # Example: Add a placeholder where you want to display the price:

price = 50

text = "The watch price is {}"
print(text.format(price))

# You can add parameters inside the curly brackets to specify how to convert the value:
 # Example: Format the price to be displayed as a number with two decimals:

price = 50

text = "The watch price is {:.2f}"  # Rwmember the dot 2f
print(text.format(price))

# Multiple Values:
 # If you want to use more values, just add more values to the format() method:

price = 50
quantity = 2

text = "The watch price is {} and it quantity is {}" # note equal parameters and it's arguements. 
print(text.format(price,quantity))

# Index Numbers:
 # You can use index numbers (a number inside the curly brackets {0}) to be sure the values are placed in the correct placeholders:
 # Example:

price = 50
quantity = 2

text = "The watch price is {1} and it quantity is {0}" 
print(text.format(price,quantity))

# Also, if you want to refer to the same value more than once, use the index number:
 # Example: 

Name = "John"
Age = 36 

txt = "His name is {0} and {0} age is {1}"
print(txt.format(Name,Age))

# Named Indexes:
 # You can also use named indexes by entering a name inside the curly brackets {carname}, but then you must use names when you pass the parameter values txt.format(carname = "Ford"):
 # Example:

Myorder = "I have a {carname} and it's {model}"
print(Myorder.format(carname = "Ford", model = "1960"))

