import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

# Load dataset
data = pd.read_csv("house_data.csv")

# Split dataset into training and testing sets
X = data.iloc[:, :-1].values
y = data.iloc[:, -1].values
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

# Create linear regression model and fit it to training data
regressor = LinearRegression()
regressor.fit(X_train, y_train)

# Make predictions on testing data and evaluate performance
y_pred = regressor.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

# Print performance metrics
print("Mean squared error: {:.2f}".format(mse))
print("R-squared value: {:.2f}".format(r2))

# Predict the estimated price of a given house
new_house_size = 1500
new_house_price = regressor.predict([[new_house_size]])
print("Estimated price for a house with size {}: {:.2f}".format(new_house_size, new_house_price[0]))
