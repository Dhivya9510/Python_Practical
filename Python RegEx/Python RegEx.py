# Python RegEx
 # A RegEx, or Regular Expression, is a sequence of characters that forms a search pattern.
 # RegEx can be used to check if a string contains the specified search pattern.

# RegEx Module:
  # Python has a built-in package called re, which can be used to work with Regular Expressions.
  # Import the re module:
  
  #   import re

# RegEx in Python:
  # When you have imported the re module, you can start using regular expressions:
  # Example:
     # Search the string to see if it starts with "The" and ends with "Spain":

import re

yolk = "The egg is good for health"

u = re.search("^The.*health$",yolk)

if u:
    print("Yes! We have a match")
else:
    print("No match")

# Go through 'Metacharacters' , 'Special Sequences' & 'Sets' in https://www.w3schools.com/python/python_regex.asp

 # RegEx Functions:
  # The re module offers a set of functions that allows us to search a string for a match:
  # findall, search, split & sub

  # The findall() Function:
      #Example: Print a list of all matches:

import re

Rain = "The rain in Spain"

t = re.findall("ai",Rain)
print(t)            # Return a list containing every occurrence of "ai"

# The list contains the matches in the order they are found.
# If no matches are found, an empty list is returned:

Rain = "The rain in Spain"
t = re.findall("good",Rain)
print(t)

# The search() Function:
 # The search() function searches the string for a match, and returns a Match object if there is a match.
 # If there is more than one match, only the first occurrence of the match will be returned:

 # Example: 

import re

Rain = "The rain in Spain"
t = re.search("rain",Rain)   
print(t)

# If no matches are found, the value None is returned:
# Example: 
 # Make a search that returns no match:

import re

Rain = "The rain in Spain"
t = re.search("good",Rain)   
print(t)

# The split() Function:
 # The split() function returns a list where the string has been split at each match:
 #Example:  Split at each white-space character:

import re

Rain = "The rain in Spain"
t = re.split("\s",Rain)     # #Split the string at every white-space character
print(t)

# You can control the number of occurrences by specifying the maxsplit parameter:

# Example: Split the string only at the first occurrence:

Rain = "The rain in Spain"
t = re.split("\s",Rain,1)     # Split the string at the first white-space character:
print(t)

# The sub() Function:
  # The sub() function replaces the matches with the text of your choice:
  # Example:  Replace every white-space character with the symbol '-':

Rain = "The rain in Spain"
t = re.sub("\s","-",Rain)     # Replace all white-space characters with the symbol "-":
print(t)

# You can control the number of replacements by specifying the count parameter:
#Example: Replace the first 2 occurrences:

Rain = "The rain in Spain"
t = re.sub("\s","-",Rain,2)     # Replace the first two occurrences of a white-space character with the symbol '-':
print(t)

# Match Object:
  # A Match Object is an object containing information about the search and the result.






  
  
  
