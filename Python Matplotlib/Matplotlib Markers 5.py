# Matplotlib Markers:

# Markers
  # You can use the keyword argument marker to emphasize each point with a specified marker:

# Example: 
   # Mark each point with a circle:

import numpy as np
import matplotlib.pyplot as plt

A = np.array([2,4,6,8])
B = np.array([10,20,30,40])

plt.plot(A,B, marker = "o")
plt.show()

# Example
  # Mark each point with a star:

import numpy as np
import matplotlib.pyplot as plt

A = np.array([2,4,6,8])
B = np.array([10,20,30,40])

plt.plot(A,B, marker = "*")
plt.show()

# Marker Reference
  # You can choose any of these markers:

import numpy as np
import matplotlib.pyplot as plt

A = np.array([2,4,6,8])
B = np.array([10,20,30,40])

plt.plot(A,B, marker = "*")
plt.show()

