# Example
   # Import only the person1 dictionary from the module:

from Mymodules6 import person1

r = person1["Age"]
print(person1["Age"])   


# Remember that  -  When importing using the 'from' keyword, do not use the module name when referring to elements 
#          in the module. Example: person1["age"], not 'mymodule.person1["age"]'