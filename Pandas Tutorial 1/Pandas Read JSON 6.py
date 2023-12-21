# Pandas Read JSON

# Read JSON
  # Big data sets are often stored, or extracted as JSON.
  # JSON is plain text, but has the format of an object, and is well known in the world of programming, including Pandas.
  # In our examples we will be using a JSON file called 'data.json'.

 # Open data.json.

# Example:
  # Load the JSON file into a DataFrame:

import pandas as pd

jack = pd.read_json("resources/data.json")
print(jack.to_string())

# Tip: use to_string() to print the entire DataFrame.

# Dictionary as JSON
  # JSON = Python Dictionary
  # JSON objects have the same format as Python dictionaries.
  # If your JSON code is not in a file, but in a Python Dictionary, you can load it into a DataFrame directly:
  # Example:
      # Load a Python Dictionary into a DataFrame:

import pandas as pd
hulk = {
  "Duration":{
    "0":60,
    "1":60,
    "2":60,
    "3":45,
    "4":45,
    "5":60
 },
  "Pulse":{
    "0":200,
    "1":117,
    "2":103,
    "3":109,
    "4":117,
    "5":102  
  },
  "Maxpulse":{
    "0":130,
    "1":145,
    "2":135,
    "3":175,
    "4":148,
    "5":127
 },
  "Calories":{
    "0":409.1,
    "1":479.0,
    "2":340.0,
    "3":282.4,
    "4":406.0,
    "5":300.5
 }
} 

o = pd.DataFrame(hulk)
print(o)


# Own notes: JSON = Python Dictionary
           # JSON objects have the same format as Python dictionaries.
           # If your JSON code is not in a file, but in a Python Dictionary, you can load it into a DataFrame directly:
           
    # Main note: Use DataFrame function if your code is not in the file, but to load it in your Json.  