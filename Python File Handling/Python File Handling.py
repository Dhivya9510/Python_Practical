# Python File Open
  # File handling is an important part of any web application.
  # Python has several functions for creating, reading, updating, and deleting files.

# File Handling
   # The key function for working with files in Python is the open() function.
   # The open() function takes two parameters; filename, and mode.
      # There are four different methods (modes) for opening a file:
        # "r" - Read - Default value. Opens a file for reading, error if the file does not exist
        # "a" - Append - Opens a file for appending, creates the file if it does not exist
        # "w" - Write - Opens a file for writing, creates the file if it does not exist
        # "x" - Create - Creates the specified file, returns an error if the file exists

  # In addition you can specify if the file should be handled as binary or text mode
    # "t" - Text - Default value. Text mode
    # "b" - Binary - Binary mode (e.g. images)

# Note: Make sure the file exists, or else you will get an error.

# Python File Open:
  # Open a File on the Server:

f = open("demofile.txt","w")
f.write("This file is now ready to use")

f = open("demofile.txt","r")
print(f.read())

# Read Only Parts of the File
  # By default the read() method returns the whole text, but you can also specify how many characters you want to return:
  # Example
     # Return the 5 first characters of the file:

f = open("demofile.txt","r")
print(f.read(9))

# Read Lines
   # You can return one line by using the readline() method:

t = open("abc.txt","w")
t.write(
        " Hello, Good Morning"
        " How you doing"
        " And hope all are good there"
        )

t = open("abc.txt", "r")
print(t.readline())

t = open("abc.txt", "r")
print(t.readline())
print(t.readline())

# By looping through the lines of the file, you can read the whole file, line by line:
t = open("abc.txt","r")
for x in t:
    print(x)

# Close Files
  # It is a good practice to always close the file when you are done with it.
  # Example
    # Close the file when you are finish with it:

t = open("abc.txt", "r")
print(t.readline())
t.close()

# Note: You should always close your files, in some cases, due to buffering, changes made to a file may not show until you close the file.

# Python File Write
   # Write to an Existing File
   # To write to an existing file, you must add a parameter to the open() function:
        #  "a" - Append - will append to the end of the file
        #  "w" - Write - will overwrite any existing content
 # Example:
    # Open the file "abc.txt2" and append content to the file:

t = open("abc.txt2","a")
t.write("This is going to end")
t.close()

t = open("abc.txt2","r")
print(t.read())


# Python Delete File
   # Delete a File
   # To delete a file, you must import the OS module, and run its os.remove() function:
   #  Example:
      # Remove the file "abc.txt":

import os
os.remove("abc.txt")

# Check if File exist:
   # To avoid getting an error, you might want to check if the file exists before you try to delete it:
   # Example:
   # Check if file exists, then delete it:

import os
if os.path.exists("abc.txt"):
    os.remove("abc.txt")
else:
    print("Sorry, The file does not exist")

# Delete Folder
    # To delete an entire folder, use the os.rmdir() method:
    # Example:
       # Remove the folder "Python deleted":

import os
os.rmdir("Python deleted")





















