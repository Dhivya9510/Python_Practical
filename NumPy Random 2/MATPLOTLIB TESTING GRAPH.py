# MATPLOTLIP

# https://www.youtube.com/watch?v=oRu4_j6r1bc

#matplotlib.pyplot
  # Here "Matplotlib" is the main module and "pyplot" is a sub-module
  
import matplotlib as mlb
print(mlb.__version__)

# version showing as output only for main module and not for sub-module. See example below:

  # import matplotlib.pyplot as plt
  # print(plt.__version__)  # Output only showing the Attribute error. 

# Graphical representation
# 1.
import  matplotlib.pyplot as plt
import numpy as np

x = np.array([2,8])
y = np.array([10,50])

plt.plot(x,y)
plt.show()

# 2. We can also give 3 values in 1 dimension array. 

x = np.array([1,5,10])
y = np.array([0,3,7])

plt.plot(x,y)
plt.show()

# We can also marked point when X & Y intersects. using - s,o,*,p,P,D, can also use numbers. 
# S means square, o means round, * means *, p means Pentagon and P means +, D means Diamond symbol. 
# If we need the line along with the point, we need to give - marker = "s"

# 3.
x = np.array([1,5,10])
y = np.array([0,3,7])

plt.plot(x,y, marker="s")
plt.show()

# When we give only one axis by commenting other axis and when plot that coded axis 
    # - the output showing as x axis defaulted by 0,1,2.. and y axis as the plotted axis's value. 

# 4.
x = np.array([1,5,10])
# y = np.array([0,3,7])

plt.plot(x,marker="o")  # Here plotted the coded axis.
plt.show()


# We can also use coloured curve lines. 
# Have to remove the text "marker" and have to add "(symbol) : (colour intial name)"
# if we need to see solid line instead dotted line have to give "hyphen" instead ":"
# If we need to see double dash neither dotted lines or solid line,we can give "double hyphen" instead ":". 
# Similarly we can give "hyphen dot" (-.)

# 5.

x = np.array([1,5,10])
# y = np.array([0,3,7])

plt.plot(x,"o:r") 
plt.show()

# 6.
# x = np.array([1,5,10])
y = np.array([0,3,7])

plt.plot(x,"o-y")  
plt.show()

# Can we increase the marker size? The answer is "Yes", simply by putting ms=(size).
# Can we change color also when increasing the marker size? Yes. Simply by putting ms=(size), mec="r"
# if we want that outline border colour inside, change 'mec' as 'mfc'.

#7.
x = np.array([1,5,10])
# y = np.array([0,3,7])

plt.plot(x, marker="o",ms=20,mec="y")  
plt.show()

# if we need double lines in the same axis that is X means, we can change Y as X1. Let's see below.

# 8.

X = np.array([1,5,10])
X1 = np.array([20,35,60])

plt.plot(X, linewidth = 20)
plt.plot(X1, linewidth = 5)
plt.show()

# 9.

X = np.array([1,5,10])
Y= np.array([20,35,60])

plt.plot(X, y,linewidth = 10)
plt.title("Graphical representation")
plt.ylabel("Population")
plt.xlabel("score")
plt.grid(axis = "y", color = "b")  # When we give only grid() without giving axis, it showing both Vertically & Horizontally.
plt.suptitle("Matplotlib Visual graphs")
plt.show()


# We can see more than 1 graphs also horizontally and vertically as showing below:

# 10.
# Plot 1
X = np.array([1,5,10])
Y= np.array([20,35,60])
plt.subplot(2,2,1)
plt.plot(X, y)

# Plot 2:

X = np.array([1,5,10])
Y= np.array([25,45,50])
plt.subplot(1,2,2)
plt.plot(X, y)

plt.title("Graphical representation")
plt.ylabel("Population")
plt.xlabel("score")
plt.grid(axis = "y", color = "g")  
plt.show()


# 11.
import  matplotlib.pyplot as plt
import numpy as np

x = np.array(["A","B","C","D","E"])
y = np.array([10,35,50,45,30])

plt.bar(x,y, color = "r")
plt.show()


# Histogram - The graph changes each time when running it. 
# 12.

import  matplotlib.pyplot as plt
import numpy as np

x = np.random.normal(10,50,20)

plt.hist(x)
plt.show()

# Piechart

# 13.
import  matplotlib.pyplot as plt
import numpy as np

x = np.array([10,35,50,45,30])
mylabel = ["Apple","Berry","Cherry","Grapes","Orange"]

plt.pie(x, labels = mylabel)  # We can add names as labels. 
plt.show()

# If we want to highlight a part of the piechart, we need to include 'SEPERATE & EXPLODE" in our code as below:
# We can change colour also in the piechart by giving colors array. 
# 14.

import  matplotlib.pyplot as plt
import numpy as np

x = np.array([10,35,50,45,30])
mylabel = ["Apple","Berry","Cherry","Grapes","Orange"]
seperate = [0,0,0,0.2,0]                            # Have to give a decimal place for which needs to be highlighted.
mycolor = ["black","pink","green","red","purple"]

plt.pie(x, labels = mylabel, explode = seperate, colors = mycolor)  # Here we should add 'explode' & if needed we can give colors to change chart color
plt.show()

# _____________________________________________________________________________

# Marker ~  s,o,*,p,P,D, can also use numbers.
# coloured line with dotted ~ ':'
# Solid line instead dotted means ~   '-' instead ':'
# Double dash ~ "--"
# Hyphen dot line ~ "-."
# Instead(While coding itself) to change the line style ~ Linestyle = "dashed/dotted"
# (Else write as linestyle) ~ ls = "--"
# To increase the intersect mark ~ ms=20 
# To apply the color also ~ mec
# To apply inner side color ~ mfc
# For thickness of the curve ~ linewidth = "20"
# Same axis two seperate curves needed means, have to give two plots with axis1 i.e. X1/Y1.. 
# Title, label, Grid.
# For more than 1 graphs, have to give 'subplot' by mentioning (row,column,plot number i.e 1st/2nd..)
# Supertitle
# Barchart
# Piechart
# Histogram - to analysis the frequency occurance.
# To highlight a part in piechart - need to include "SEPERATE" & "EXPLODE". 
# Can change colors also in the piechart by mentioning the color array.
   # Color codes availble in websites, we can apply that code also.








