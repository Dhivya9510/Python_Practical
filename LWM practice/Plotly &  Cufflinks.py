# PLOTLY AND CUFFLINKS INTRO: 

# Plotly : It’s a Graphics library for interactive plots. Flexible for number of programming languages. 
# Cufflinks: It combines and binds the panda’s dataframes and Plotly’s visualization power for best interaction. 

# Generally in seaborn, it shows the graph plots, But in this – It shows along with the data (like a tooltip) whenever we placed a cursor anywhere inside the graph. 


from plotly import __version__
from plotly.offline import download_plotlyjs, plot, iplot , init_notebook_mode
print(__version__)


import cufflinks as cf
import pandas as pd
import numpy as np

# Fake Data: 

df = pd.DataFrame(np.random.randn(100,4), columns= 'A B C D'.split())
df.head()
print(df)


# Note: 
# For Notebooks: 

init_notebook_mode(connected = True)

# For Offline use: 
cf.go_offline()

# Using Cufflinks and iplot():
    # Scatter                      # Bar
    # Box                          # Spread
    # Ratio                        # Heatmap
	# Surface                      # Histogram
    # Bubbles





















