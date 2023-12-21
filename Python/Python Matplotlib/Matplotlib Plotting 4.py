# Matplotlib Plotting

# Plotting x and y points
  # The plot() function is used to draw points (markers) in a diagram.
  # By default, the plot() function draws a line from point to point.
  # The function takes parameters for specifying points in the diagram.
         # Parameter 1 is an array containing the points on the x-axis.
         # Parameter 2 is an array containing the points on the y-axis.

# If we need to plot a line from (1, 3) to (8, 10), we have to pass two arrays [1, 8] and [3, 10] to the plot function.
   # (Own notes : Above (1,3) & (8,10) where we asked to connect 1 (in X) to 3 (in Y) & 8 (in X) to 10 (in Y),
      # - We need to plot (1,8) means it's in the X axis (to point) & (3,10) means it's in the Y axis (to point)

# Example: 
    # Draw a line in a diagram from position (1, 3) to position (8, 10):

import numpy as np
import matplotlib.pyplot as plt

Xaxis = np.array([1,8])
Yaxis = np.array([3,10])

plt.plot(Xaxis,Yaxis)
plt.show()

# The x-axis is the horizontal axis.
# The y-axis is the vertical axis.

# Plotting Without Line
   # To plot only the markers, you can use shortcut string notation parameter 'o', which means 'rings'.

# Example
   # Draw two points in the diagram, one at position (1, 3) and one in position (8, 10):

import numpy as np
import matplotlib.pyplot as plt

Paxis = np.array([1,8])
Qaxis = np.array([3,10])

plt.plot(Paxis,Qaxis, 'o')
plt.show()

# Multiple Points
  # You can plot as many points as you like, just make sure you have the same number of points in both axis.

# Example
   # Draw a line in a diagram from position (1, 3) to (2, 8) then to (6, 1) and finally to position (8, 10):

import numpy as np
import matplotlib.pyplot as plt

Haxis = np.array([1,2,6,8])
Uaxis = np.array([3,8,1,10])

plt.plot(Haxis,Uaxis)
plt.show()

# Default X-Points
  # If we do not specify the points on the x-axis, they will get the default values 0, 1, 2, 3 (etc., depending on the length of the y-points.
  # So, if we take the same example as above, and leave out the x-points, the diagram will look like this:

# Example:
   # Plotting without x-points:

import numpy as np
import matplotlib.pyplot as plt

Ypoints = np.array([3,5,6,7])

plt.plot(Ypoints)
plt.show()

# The x-points in the example above are [0, 1, 2, 3].

# Own notes: 'o' indicates only marking points without a line
          # If no X-axis inputed, it will defaultedly taken X-axis as 0,1,2,3...
          # Multiple lines can also be drawn but the number of value inputted in X & Y would be the same.
          # For (1,3) & (8,10) where we asked to connect. Means 1 (in X) to 3 (in Y) & 8 (in X) to 10 (in Y),
             # - We need to plot (1,8) means it's in the X axis (to point) & (3,10) means it's in the Y axis (to point)

