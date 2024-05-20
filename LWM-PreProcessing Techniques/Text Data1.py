# HANDLING TEXT DATA:

#Here we are going to use ‘Unstructured Data’ to convert into Information-rich data. 
# Unstructured data are nothing but the data which is Unstructured. Example: Tweets, contents of books. 

# 1.CLEANING DATA: 
     # Python’s core string operations, in particular ‘Strip’, ‘Replace’ & ‘Split’.

# a)‘Strip’ is used to eliminate unwanted spaces. 

# Create Text: 

text_data = ["  Interrobang. By Aishwarya Henriette  ", "Parking and Going. By Kark Gautier", " Today Is the night. By Jarek Prakash  "]
   # In the above text - you can see the unwanted spaces after the double apostraphe.We need to remove that. 
   # You can do that using for loops through list comprehension. 

# Strip Whitespace.
strip_whitespace = [strings.strip() for strings in text_data]
print(strip_whitespace)

# b)‘Replace’ is used to replacing the elements. 

remove_periods = [strings.replace(".","") for strings in strip_whitespace]
print(remove_periods)

# c) (Next we are going to see how to ‘transform’ our function using ‘create’ & ‘apply’)
  # We also create and apply a custom transformation function. 

def capitalizer (string:str):
    return string.upper()

  # Apply function: 
capital = [capitalizer(string) for string in remove_periods]
print(capital)

# d) Finally, we can use regular expressions to make powerful string operations: 
# Import Library
import re
# Create function: 
def replace_with_X(string:str):
    return re.sub(r"[a-zA-Z]","X",string)  # note 'r"' is must to put. 
# Apply function: 
X_letter = [replace_with_X(string) for string in remove_periods]
print(X_letter)

# Code Explanation: 
   # Import Library for regular expression called ‘re’
   # Create variable for def function that is ‘Replace_with_X’. As usual put in bracket that (string:str)
   # In return, put ‘re’.sub – means ‘substitute’ wherever you see the string a to z or A to Z, replace them all with ‘X’. 
   # At last write it inside list comprehension. 

# Where we can use it? For passwords when we type for our social profile account - should be only visible with this ‘X’ letter. 

# 2.PARCING AND CLEANING HTML:
     # As we all know, HTML is a front-end tool for creating web applications, through that we can create a webpage. 
     # In that whole HTML page - we can extract the particular information that we need (term called as ‘Scraping’)– for that we will use the function named ‘Beautiful Soup’. (name might be very strange for you however this is one of the powerful tools)
     # Despite the strange name, Beautiful soup is a powerful python library designed for scraping HTML. 
     # Typically 'BeautifulSoup' is used scrap live websites, but we can just as easily use it to extract text data embedded in HTML. 
     # The full range of 'BeautifulSoup' is beyond the scope of this book, but even the few methods used in our solution show how easily we can parse HTML code to extract the data we want. 

# Load Library
from bs4 import BeautifulSoup
# Create some HTML code:
html = """<div class = "full name"><span style = font-weiht:bold">Masego</span> Azra</div>"""
# Parse HTML:
   # soup = BeautifulSoup(html,"lxml")  #type: ignore
# Find the div with the class "full name", show text. 
   # tan =soup.find("div",{"class" : "full name"}).text  # type: ignore
   # print(tan)
  
# 3. REMOVING PUNCTUATION: 

  # This is going to remove unwanted punctuations in a text. For that we need to go to the library called ‘Unicodedata’ & ‘sys’. 
  # Due to the below code is almost difficult for you to understand – don’t worry about it. 
  # As of now, Just remembered it as a snipped for ‘Removing punctuations’. You will get this later when practicing and practicing.

# Import Libraries
import unicodedata
import sys

# Create text
text_data1 = ["Hi!!!! I. Love. This. Song....", "100000% Agree!!!!  #LoveIT", "Right?!?!"]

# Create a dictionary of punctuation chartacters.
puntuation = dict.fromkeys(i for i in range(sys.maxunicode)
if unicodedata.category(chr(i)).startswith('P'))
   # No problem if you can’t understand the two coding lines given in the variable ‘Punctuation’ as it seems a bit difficult for you. 
   # The output will remove all the unnecessary punctuation not changing the upper/lower cases. 

# For each string, remove any punctuation characters: 
removed_punctuations = [string.translate(puntuation) for string in text_data1]
print(removed_punctuations)

# Note: Mostly using List comprehension here.  
       # Remember that ‘Tokenization’ is a simple and common task that we do after preprocessing and before giving it to the ML. 
       # Removed_stopwords = [word for word in tokenized_words if word not in stop_words ]  # understand the concept of this code. 
       # Create a dictionary of punctuation chartacters.
               # puntuation = dict.fromkeys(i for i in range(sys.maxunicode)
               # if unicodedata.category(chr(i)).startswith('P'))
       # For each string, remove any punctuation characters: 
               # removed_punctuations = [string.translate(puntuation) for string in text_data1]
       
 