import pandas as pd
from sklearn.datasets import load_wine, load_iris
from sklearn.preprocessing import StandardScaler

# Load the wine dataset
wine = load_wine()

# Convert the dataset into a Pandas DataFrame
df_wine = pd.DataFrame(data=wine.data, columns=wine.feature_names)

# Check the mean and standard deviation of each attribute
print(df_wine.mean())
print(df_wine.std())

# Standardize the attributes
scaler = StandardScaler()
df_wine_std = pd.DataFrame(scaler.fit_transform(df_wine), columns=df_wine.columns)

# Check the mean and standard deviation of each attribute after standardization
print(df_wine_std.mean())
print(df_wine_std.std())

# Load the iris dataset
iris = load_iris()

# Convert the dataset into a Pandas DataFrame
df_iris = pd.DataFrame(data=iris.data, columns=iris.feature_names)

# Check the mean and standard deviation of each attribute
print(df_iris.mean())
print(df_iris.std())

# Standardize the attributes
scaler = StandardScaler()
df_iris_std = pd.DataFrame(scaler.fit_transform(df_iris), columns=df_iris.columns)

# Check the mean and standard deviation of each attribute after standardization
print(df_iris_std.mean())
print(df_iris_std.std())