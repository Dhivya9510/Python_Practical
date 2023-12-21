# Random Permutations:

# Random Permutations of Elements
  # A permutation refers to an arrangement of elements. e.g. [3, 2, 1] is a permutation of [1, 2, 3] and vice-versa.
  # The NumPy Random module provides two methods for this: shuffle() and permutation().

# Shuffling Arrays:
  # Shuffle means changing arrangement of elements in-place. i.e. in the array itself.
  # Example:
    # Randomly shuffle elements of following array:

from numpy import random
import numpy as np

u = np.array([1,2,3,4,5,6])

random.shuffle(u)
print(u)

# Generating Permutation of Arrays
  # Example:
     # Generate a random permutation of elements of following array:

from numpy import random
import numpy as np

t = np.array([1,2,3,4,5,6])

print(random.permutation(t))

# Notes: The shuffle() method makes changes to the original array.
        # The permutation() method returns a re-arranged array (and leaves the original array un-changed).


#  Own notes: REMEMBER THE FORMAT. BOTH FOR SHUFFLE AND PERMUTATIONS. 
           



