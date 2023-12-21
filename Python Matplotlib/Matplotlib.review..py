# Draw a line in a diagram from position (0,0) to position (6,250):

import matplotlib.pyplot as plt
import numpy as np

xarray = np.array([0,6])
yarray = np.array([0,250])

plt.plot(xarray,yarray)
plt.show()

# Draw a line in a diagram from position (1, 3) to position (8, 10):

import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array([1,8])
ypoints = np.array([3,10])

plt.plot(xpoints,ypoints)
plt.show()

# Draw two points in the diagram, one at position (1, 3) and one in position (8, 10):

import matplotlib.pyplot as plt
import numpy as np

x_points = np.array([1,8])
y_points = np.array([3,10])

plt.plot(x_points,y_points, "o")
plt.show()

# Mark each point with a circle:

import matplotlib.pyplot as plt
import numpy as np

yAxis = np.array([3, 8, 1, 10])
plt.plot(yAxis, "o:y")
plt.show()

import numpy as np
import matplotlib.pyplot as plt

# Set Font Properties for Title and Labels

x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])

font1 = {'family':'serif','color':'blue','size':20}
font2 = {'family':'serif','color':'darkred','size':15}

plt.title("Sports Watch Data", fontdict = font1)
plt.xlabel("Average Pulse", fontdict = font2)
plt.ylabel("Calorie Burnage", fontdict = font2)

plt.plot(x, y)
plt.show()

# Draw 2 plots:

import matplotlib.pyplot as plt
import numpy as np

x1 = np.array([0,1,2,3])
y1 = np.array([3,8,1,10])

plt.subplot(1,2,1)
plt.plot(x1,y1)
plt.title("Sales")

x2 = np.array([0,1,2,3])
y2 = np.array([10,20,30,40])

plt.subplot(1,2,2)
plt.plot(x2,y2)
plt.title("Income")

plt.suptitle("My Shop")
plt.show()

# Scatter
  # A simple scatter plot:

import matplotlib.pyplot as plt
import numpy as np

xaxis = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
yaxis = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
plt.scatter(xaxis,yaxis)

x1axis = np.array([2,2,8,1,15,8,12,9,7,3,11,4,7,14,12])
y1axis = np.array([100,105,84,105,90,99,90,95,94,100,79,112,91,80,85])
plt.scatter(x1axis,y1axis)

plt.show()

# Create a color array, and specify a colormap in the scatter plot:

import  matplotlib.pyplot as plt
import numpy as np

x= np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
color = np.array([0,10,20,30,40,50,60,70,80,90,100,110,120])

plt.scatter(x, y, c= color, cmap = "viridis")
plt.colorbar()
plt.show()

# Bar chart

import matplotlib.pyplot as plt
import numpy as np

A = np.array(['A','B','C','D'])
B = np.array([3,4,5,6])

plt.barh(A,B, height = 0.1)
plt.show()

# Histogram

# A Normal Data Distribution by NumPy:

import numpy as np

x = np.random.normal(170,10,250)

print(x)

# Draw Histrogram

import matplotlib.pyplot as plt
import numpy as np

x = np.random.normal(170,10,250)
plt.hist(x)
plt.show()

# Pie Chart

import matplotlib.pyplot as plt
import numpy as np

x = np.array([35,25,25,15])
Mylabels = ["Apples","Bananas","Cherry","Dates"]
MyExplode = [0.2,0,0,0]
Mycolors = ["Black","Yellow","Green","Hotpink"]

plt.pie(x, labels = Mylabels, startangle = 90, explode = MyExplode, shadow = True, colors = Mycolors)
plt.legend(title = "Four Fruits:")
plt.show()




