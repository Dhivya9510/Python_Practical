# SciPy Introduction

# What is SciPy?
  # SciPy is a scientific computation library that uses NumPy underneath.
  # SciPy stands for Scientific Python.
  # It provides more utility functions for optimization, stats and signal processing.
  # Like NumPy, SciPy is open source so we can use it freely.
  # SciPy was created by NumPy's creator Travis Olliphant.

# Why Use SciPy?
  # If SciPy uses NumPy underneath, why can we not just use NumPy?
      # SciPy has optimized and added functions that are frequently used in NumPy and Data Science

# Import SciPy
   # Once SciPy is installed, import the SciPy module(s) you want to use in your applications by adding the from scipy import module statement:

# from scipy import constants
 
   # Now we have imported the constants module from SciPy, and the application is ready to use it:

# Example: 
    # How many cubic meters are in one liter:

from scipy import constants

print(constants.liter)

# constants: SciPy offers a set of mathematical constants, one of them is liter which returns 1 liter as cubic meters.
  # You will learn more about constants in the next chapter.

# Checking SciPy Version
   # The version string is stored under the __version__ attribute.

# Example:

import scipy

print(scipy.__version__)




