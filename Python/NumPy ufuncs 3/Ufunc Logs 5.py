# NumPy Logs:

# Logs
   # NumPy provides functions to perform log at the base 2, e and 10.
   # We will also explore how we can take log for any base by creating a custom ufunc.
   # All of the log functions will place -inf or inf in the elements if the log can not be computed.

# Log at Base 2:
   # Use the log2() function to perform log at the base 2.
   # Example:
        # Find log at base 2 of all elements of following array:

import numpy as np

arr = np.arange(1,10)
print(np.log2(arr))

# Note: The arange(1, 10) function returns an array with integers starting from 1 (included) to 10 (not included).

# Log at Base 10
  # Use the log10() function to perform log at the base 10.

# Example
   # Find log at base 10 of all elements of following array:

import numpy as np
arr = np.arange(1,10)
print(np.log10(arr))

# Natural Log, or Log at Base e
   # Use the log() function to perform log at the base e.

# Example
   # Find log at base e of all elements of following array:

import numpy as np

arr = np.arange(1,10)
print(np.log(arr))

# Log at Any Base
  # NumPy does not provide any function to take log at any base, so we can use the frompyfunc() function along with inbuilt function math.log() with two input parameters and one output parameter:
  # Example:

from math import log
import numpy as np

nplog = np.frompyfunc(log,2,1)
print(nplog(100,20))

# Own notes : As per mathematics - 3 power of 2 = 8 means 2*2*2 = 8
            # Here 3 is the log of 8 with base 2. 

            # 'arange' needs to be used at all log 2,e and 10. Note this. 
            # In last example, 2 is the number of parameters given as input and 1 is the number of output value expected.
            # Remember the format. (Not any important understanding other than this on log)
    
































