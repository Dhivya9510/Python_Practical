import pandas as pd

df = pd.DataFrame()

df["Name","Age","Sex","Grade"] = ["Ganga",35,"Female","A"]
print(df)

# Delete a column
dele = df.drop("Age", axis=1)  #type:ignore
dele = df.drop(["Age","Sex"], axis=1)
delete = df.drop(df.columns[0], axis=1)

print(delete)

# Delete a row

elete = df[df["Sex"] != "Male"].head()
elet = df[df["Age"] <=40 & df["Sex"] == "Female"]
ele = df[df.index != 0]

# Create column of random values 
import numpy as np
df["Sales_amount"] = np.random.randint(1,10,1000)

for name in df["Name"][0:2]:
    print(name.upper())

def uppercase(Sex):
    return Sex.upper()

df["Name"].apply(uppercase)[0:2]   # Here 'uppercase' is a created function. 

# load library
from sklearn import preprocessing
# Create Feature
feature = np.array([[-500.5],[-100.1],[0],[100.1],[900.9]])
# Create scalar
minmax_scale = preprocessing.MinMaxScaler(feature_range=(0,1))
# Create Scalad feature
Scaled_feature = minmax_scale.fit_transform(feature)

from sklearn import preprocessing
# Creating a feature
x = np.array([[-1000.1],[-200.2],[500.5],[600.6],[9000.9]])
# Creating scalar
scalar = preprocessing.StandardScaler()
# Creating Standardized scalar
standardized = scalar.fit_transform(x)

print("mean:", round(standardized.mean()))
print("Standard Deviation:", standardized.std())

# Creating a feature
x = np.array([[-1000.1],[-200.2],[500.5],[600.6],[9000.9]])
# Creating scalar
scaled = preprocessing.RobustScaler()
# transform feature
Robust_scale = scaled.fit_transform(x)

# Import Library
import numpy as np
from sklearn.preprocessing import PolynomialFeatures

# Creating feature
feature = np.array([[2,3],[2,3],[2,3],[2,3]])

# Creating polynomial feature objects
polynomial_interaction = PolynomialFeatures(degree=2, include_bias= False)

# Transform feature
polynomial_interaction.fit_transform(feature)

# Import library
import numpy as np
from sklearn.preprocessing import FunctionTransformer
# Creating feature
feature1 = np.array([[2,3],[2,3],[2,3]])
# Creating function
def add_three(x):
    return x + 3
# Creating transformer
transformer = FunctionTransformer(add_three)
# creating function transformer 
function_transformer = transformer.transform(feature1)

# Detecting ourliers

#Import library
import numpy as np
from sklearn.covariance import EllipticEnvelope
from sklearn.datasets import make_blobs
# Creating feature
feature2 = make_blobs(n_samples=10,n_features=2,centers=1, random_state=1)
#Creating outlier values
feature[0,0] = 100000
feature[0,1] = 100000
outliers = EllipticEnvelope(contamination=0.1) # we given small number of contamination value because we
# know that outliers here is just one value. Usually we won't know how many outliers are existing.
# If the number is small we can give small number of contamination else we can give big number of contamination. 

# Fitting outliers. 
Detecting_outliers = outliers.fit(feature)
# Predicting with feature
predicting_outliers = outliers.predict(feature)

# If it's an outlier - the output will showing as -1, otherwise it will be 1. 

# (We can use Elliptic Envelope method when our boss intimate us before that file has ‘this much’ outliers – based on that we put contamination value.
# But what if when our boss did not inform us before out the outliers – we don’t know about the size right? Hence here in this place – we can use 'Inter-Quartile range'.
# ‘Inter-Quartile’ range – a statistical method and a mathematical operation done by using ‘Percentiles’.)

# Iner-Quartile range:
# Import libraries
import numpy as np
# Creating features:
feature = make_blobs(n_samples=10, n_features=2, centers=1, random_state=1)
# Creating a function for outliers:
def indicies_of_outliers(x):
    q3,q1 = np.percentile(x,[25,75])
    iqr =q3-q1
    upper_bound = q3 + (iqr *1.5)
    lower_bound = q1 - (iqr *1.5)
    return np.where ((x > upper_bound) | (x< lower_bound))
# Detecting outliers
indicies_of_outliers(feature)

# (Outliers are commonly defined as any value 1.5 IQRs less than the first quartile or 1.5 IQRs greater than the third quartile)

# Grouping numerical observations using clustering
# Import libraries
import numpy as np
from sklearn.datasets import make_blobs
from sklearn.cluster import KMeans
# Creating a feature 
feature = make_blobs(n_samples= 50, n_features= 2, centers= 3, random_state=1)
# Creating a dataframe
dataframe = pd.DataFrame(feature, columns=["feature1", "feature2"])
# Creating cluster
clusterer = KMeans(3, random_state=1)
# Fitting cluster
hut = clusterer.fit(feature)
# Predicting cluster 
goat = clusterer.predict(feature)
dataframe.head()

# Deleting observations with missing values: 
# Loading libraries
import numpy as np
# Creating a feature
feature3 = np.array([[1.1,11.1],[2.2,22.2],[3.3,33.3],[4.4,44.4],[np.nan,55.5]])
# keep only observations that are not missing (denoted by ~ tilt symbol)
hen = feature3[~np.isnan(feature3).any(axis=1)]

# Loading Libraries
import pandas as pd
# Creating feature 
feature4 = pd.DataFrame(feature3, columns=["feature_a","feature_b"])
# removing missing values
jack = feature4.dropna()

