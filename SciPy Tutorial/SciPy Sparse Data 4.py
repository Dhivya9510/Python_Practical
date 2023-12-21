# SciPy Sparse Data

# What is Sparse Data
   # Sparse data is data that has mostly unused elements (elements that don't carry any information ).
   # It can be an array like this one:
       # [1, 0, 2, 0, 0, 3, 0, 0, 0, 0, 0, 0]

# Sparse Data: is a data set where most of the item values are zero.
# Dense Array: is the opposite of a sparse array: most of the values are not zero.

# In scientific computing, when we are dealing with partial derivatives in linear algebra we will come across sparse data.

# How to Work With Sparse Data
   # SciPy has a module, scipy.sparse that provides functions to deal with sparse data.
   # There are primarily two types of sparse matrices that we use:
   # CSC - Compressed Sparse Column. For efficient arithmetic, fast column slicing.
   # CSR - Compressed Sparse Row. For fast row slicing, faster matrix vector products

# We will use the CSR matrix in this tutorial.

# CSR Matrix
   # We can create CSR matrix by passing an arrray into function scipy.sparse.csr_matrix().

# Example
   # Create a CSR matrix from an array:

import numpy as np
from scipy.sparse import csr_matrix

arr = np.array([0,0,1,0,0,2,0,0,0,0,3]) 

print(csr_matrix(arr))

# The example above returns:
  # (0, 2)	1
  # (0, 5)	2
  # (0, 10)	3

# From the result we can see that there are 3 items with value.
  # The 1. item is in row 0 position 2 and has the value 1.
  # The 2. item is in row 0 position 5 and has the value 2.
  # The 3. item is in row 0 position 10 and has the value 3.

# Sparse Matrix Methods
   # Viewing stored data (not the zero items) with the data property:
   # Example

import numpy as np
from scipy.sparse import csr_matrix

arr = np.array([0,0,1,0,2,0,0,0,3,0,0,4,0])

print(csr_matrix(arr).data)

# Counting nonzeros with the count_nonzero() method:
  # Example

import numpy as np
from scipy.sparse import csr_matrix

jack = np.array([[0,0,1],[0,1,0],[6,2,2]])

print(csr_matrix(jack).count_nonzero())     # Note the inner bracket beside NONZERO

# Removing zero-entries from the matrix with the eliminate_zeros() method:
  # Example

import numpy as np
from scipy.sparse import csr_matrix

run = np.array([[0,0,1],[0,1,0],[6,2,2]])

newrun = csr_matrix(run)
newrun.eliminate_zeros()
print(newrun)

# Eliminating duplicate entries with the sum_duplicates() method:

# Example
  # Eliminating duplicates by adding them:

import numpy as np
from scipy.sparse import csr_matrix

nod = np.array([[0,0,1],[0,1,0],[6,2,2]])

newnod = csr_matrix(nod)
newnod.sum_duplicates()
print(newnod)

# Converting from csr to csc with the tocsc() method:
  # Example

import numpy as np
from scipy.sparse import csc_matrix

monk = np.array([[0,0,1],[0,1,0],[6,2,2]])

newmonk = csr_matrix(monk).tocsc()
print(newmonk)

# Note: Apart from the mentioned sparse specific operations, sparse matrices support all of the operations that normal matrices support e.g. reshaping, summing, arithemetic, broadcasting etc.


# Own Notes: csr_matrix()
           # .data
           # .count_nonzero()
           # .eliminate_zeros()
           # .sum_duplicates()
           # .tocsc()


