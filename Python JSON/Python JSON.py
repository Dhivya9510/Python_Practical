# Python JSON
  # JSON is a syntax for storing and exchanging data.
  # JSON is text, written with JavaScript object notation.

# JSON in Python
  # Python has a built-in package called json, which can be used to work with JSON data.

# Parse JSON - Convert from JSON to Python:
  # If you have a JSON string, you can parse it by using the json.loads() method.

# Example:
  # Convert from JSON to Python:

import json

x = '{"Name":"Dhivya","Age":30,"Gender":"Female","Location":"Vellore"}'   #some JSON -single quote b4 & after dict

y = json.loads(x)

print(y["Location"])

# Convert from Python to JSON:
  # If you have a Python object, you can convert it into a JSON string by using the json.dumps() method.
  # Example
    # Convert from Python to JSON:

import json

x = {"Name":"Dhivya","Age":30,"Gender":"Female","Location":"Vellore"} 

y = json.dumps(x)

print(y)

# You can convert Python objects of the following types, into JSON strings:
 # Example
   # Convert a Python object containing all the legal data types:

import json

r = {                            # This is the Python data types. Here we convert this as JSON
    "Name":"Priya",                               
     "Age":30,
     "Height":150.32,
     "Location":["Vellore","Coimbatore"],
     "Food":("Apple","Banana"),
     "Married":True,
     "Children":False
}

T = json.dumps(r)
print(T)




  

