import pandas as pd
from sklearn.linear_model import LinearRegression

# Load the dataset
data = pd.read_csv('house_data1.csv')

# Select the relevant features as independent variables
X = data[['bedrooms', 'servant_room', 'balconies', 'years_old']]

# Select the price column as the dependent variable
y = data['price']

# Fit a multiple linear regression model
model = LinearRegression()
model.fit(X, y)

# Predict the price of a new house based on its features
new_house = [[3, 1, 2, 5]]
predicted_price = model.predict(new_house)
print(predicted_price)
