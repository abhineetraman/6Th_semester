import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score

# Load the student dataset
student_data = pd.read_csv("student_data.csv")

# Prepare the data
X = student_data[['feature1', 'feature2', 'feature3', 'feature4']] # Features
y = student_data['label'] # Target variable

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create a multi-layer perceptron (MLP) classifier with SGD optimizer
# You can configure the number of hidden layers and neurons per layer
# Note that MLPClassifier in scikit-learn uses 'relu' as the default activation function
model = MLPClassifier(hidden_layer_sizes=(100,), activation='relu', solver='sgd', learning_rate_init=0.1)

# Train the model
model.fit(X_train, y_train)

# Make predictions on the test data
y_pred = model.predict(X_test)

# Calculate accuracy
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)
