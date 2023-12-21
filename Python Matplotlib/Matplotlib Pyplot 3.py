# Matplotlib Pyplot

# Pyplot
   # Most of the Matplotlib utilities lies under the pyplot submodule, and are usually imported under the plt alias:

       # import matplotlib.pyplot as plt

# Now the Pyplot package can be referred to as plt.

# Example:
   # Draw a line in a diagram from position (0,0) to position (6,250):

import numpy as np
import matplotlib.pyplot as plt

Xaxis = np.array([0,6])
Yaxis = np.array([0,250])

plt.plot(Xaxis,Yaxis)
plt.show()

# Own Example:
   # Draw a line in a diagram from position (5,30) to position (10,60):

import numpy as np
import matplotlib.pyplot as plt

P = np.array([5,10])
Q = np.array([30,60])

plt.plot(P,Q)
plt.show()




