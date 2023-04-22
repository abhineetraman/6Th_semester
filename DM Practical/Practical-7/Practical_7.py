# Students should be promoted to take up one project on any UCI/kaggle/data.gov.in or a dataset
# verified by the teacher. Preprocessing steps and at least one data mining technique should be shown
# on the selected dataset. This will allow the students to have a practical knowledge of how to apply
# the various skills learnt in the subject for a single problem/project.

import pandas as pd
from sklearn import preprocessing
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

print("Data Set : Dry_Bean.")
data = pd.read_csv('Dry_Bean.csv')
X = data.values[:, 0:16]
Y = data.values[:, 16]

# Applying preprocessing technique that is standardization
scaler = preprocessing.StandardScaler().fit(X)
# Applying Scaler tranformation
X = scaler.transform(X)

# Splitting the data into training and testing data using hold out method
X_train, X_test, Y_train, Y_test = train_test_split(
    X, Y, test_size=0.25, shuffle=True)

decision_Tree = DecisionTreeClassifier()

# Training the model on training data set
decision_Tree.fit(X_train, Y_train)

# Applying the model on the testing data set
Y_predicted = decision_Tree.predict(X_test)

# Computing the accuracy of the decision tree classifier model
print(("Accuracy is "), accuracy_score(Y_test, Y_predicted) * 100,
      ("when using Decision Tree with 75 % of training data"))
