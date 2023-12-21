# Pandas Getting Started

import pandas

# Pandas as pd
  # Pandas is usually imported under the pd alias.

import pandas as pd

mydata = {"Cars":["BMW","Volvo","Maruthi"], "Numbers":[2,4,6]}

u = pd.DataFrame(mydata)
print(u)

# Checking Pandas Version
  # The version string is stored under __version__ attribute.
  # Example

import pandas as pd

print(pd.__version__)

