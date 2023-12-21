import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df1= pd.read_csv("resources/df1.txt", index_col = 0)
#print(df1)

#df2= pd.read_csv("resources/df2.txt")
#print(df2)

# Normal Histogram:

df1['A'].hist()
plt.show()

# STYLE SHEETS

plt.style.use("ggplot")
df1['A'].hist()
plt.show()

# STYLE SHEETS

plt.style.use("bmh")
df1['A'].hist()
plt.show()

# STYLE SHEETS

plt.style.use("fivethirtyeight")
df1['A'].hist()
plt.show()

# STYLE SHEETS

plt.style.use("dark_background")
df1['A'].hist()
plt.show()


