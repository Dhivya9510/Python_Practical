# Format the Result:
  # The example above prints a JSON string, but it is not very easy to read, with no indentations and line breaks.
  # The json.dumps() method has parameters to make it easier to read the result:   
  # Example:
    # Use the indent parameter to define the numbers of indents:

import json

r = {                            
    "Name":"Priya",                               
     "Age":30,
     "Height":150.32,
     "Location":["Vellore","Coimbatore"],
     "Food":("Apple","Banana"),
     "Married":True,
     "Children":False
}

print(json.dumps(r,indent=4))

# You can also define the separators, default value is (", ", ": "), which means using a comma and a space to separate each object, and a colon and a space to separate keys from values:
  # Example:
    # Use the separators parameter to change the default separator:

import json

print(json.dumps(r,indent=4,separators=(". ", " = ")))
# use . and a space to separate objects, and a space, a = and a space to separate keys from their values:


# Order the Result:
 # The json.dumps() method has parameters to order the keys in the result:
 # Example:
   # Use the sort_keys parameter to specify if the result should be sorted or not:

import json

print(json.dumps(r, indent=4, sort_keys=True))
