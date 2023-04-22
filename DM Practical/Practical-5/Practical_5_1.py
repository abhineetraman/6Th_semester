# Use Naive bayes, K-nearest, and Decision tree classification algorithms and build classifiers. 
# Divide the data set into training and test set. Compare the accuracy of the different classifiers 
# under the following situations:
# 5.1 a) Training set = 75% Test set = 25% b) Training set = 66.6% (2/3rd of total), Test set = 
# 33.3%
# 5.2 Training set is chosen by i) hold out method ii) Random subsampling iii) Cross-Validation. 
# Compare the accuracy of the classifiers obtained.
# 5.3 Data is scaled to standard format.

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
import statistics
from sklearn.model_selection import StratifiedKFold
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier

def get_Score(model,X_train,Y_train,X_test,Y_test):
    model.fit(X_train,Y_train)
    return model.score(X_test,Y_test)*100

scale = StandardScaler()

data = pd.read_csv('./abalone_csv.csv')
X=data[0:].values[:,1:]
Y=data[0:].values[:,0]
Xval=["Hold-Out","Random Sub-Sampling","Cross-Validation"]

# Decision Tree Classifier
# 5.1
# Training Size:75% and Test Size:25%
print("Decision Tree Classifier")
X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=0.25,random_state=1000)
X_train = scale.fit_transform(X_train)
X_test = scale.fit_transform(X_test)
clf=DecisionTreeClassifier()
clf.fit(X_train,Y_train)

print(f"Accuracy is {get_Score(clf,X_train,Y_train,X_test,Y_test)} with 75% of training data")

# Training Size:66.6% and Test Size:33.3%
X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=0.333,random_state=1000)
X_train = scale.fit_transform(X_train)
X_test = scale.fit_transform(X_test)
clf.fit(X_train,Y_train)

print(f"Accuracy is {get_Score(clf,X_train,Y_train,X_test,Y_test)} with 66.6% of training data")

# 5.2
# Using Hold-Out method for splitting
Accuracy = []
X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.2,random_state=1000)
X_train = scale.fit_transform(X_train)
X_test = scale.fit_transform(X_test)
clf.fit(X_train,Y_train)

Accuracy.append(get_Score(clf,X_train,Y_train,X_test,Y_test))

# using Random Subsampling for splitting
Accuracy_Random=[]
k=6
for i in range(0,k):
    X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.2,random_state=100)
    X_train = scale.fit_transform(X_train)
    X_test = scale.fit_transform(X_test)
    clf.fit(X_train,Y_train)
    prediction = clf.predict(X_test)
    Accuracy_Random.append(accuracy_score(Y_test,prediction)*100)

Accuracy.append(statistics.mean(Accuracy_Random))

# using K-Cross-Validation for splitting
k=9
kf = StratifiedKFold(n_splits=k)
Accuracy_kFold=[]
for train_index,test_index in kf.split(X,Y):
    X_train,X_test,Y_train,Y_test = X[train_index],X[test_index],Y[train_index],Y[test_index]
    X_train = scale.fit_transform(X_train)
    X_test = scale.fit_transform(X_test)
    Accuracy_kFold.append(get_Score(DecisionTreeClassifier(),X_train,Y_train,X_test,Y_test))
Accuracy.append(statistics.mean(Accuracy_kFold))
print("Accuracy: ",Accuracy)

# Visualizing the accuracy of the Decision Tree Model for different Splitting models
Yval = Accuracy
plt.bar(Xval,Yval,color="green",width=0.2)
plt.xlabel("Splitting Method")
plt.title("Decision Tree Classifier Visualization")
plt.show()

# Naive Bayes Classifier
NBclf = GaussianNB()
print("Naive-Bayes Classifier")
# Training Size:75% and Test Size:25%
X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=0.25,random_state=1000)
X_train = scale.fit_transform(X_train)
X_test = scale.fit_transform(X_test)
print(f"Accuracy is {get_Score(NBclf,X_train,Y_train,X_test,Y_test)} with 75% of Training Data")

# Training Size:66.6% and Test Size:33.3%
X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=0.333,random_state=1000)
X_train = scale.fit_transform(X_train)
X_test = scale.fit_transform(X_test)
print(f"Accuracy is {get_Score(NBclf,X_train,Y_train,X_test,Y_test)} with 66.6% of Training Data")

# 5.2
# Using Hold-Out method for splitting
Accuracy = []
X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.2,random_state=1000,shuffle=True,stratify=Y)
X_train = scale.fit_transform(X_train)
X_test = scale.fit_transform(X_test)
Accuracy.append(get_Score(NBclf,X_train,Y_train,X_test,Y_test))

# using Random Subsampling for splitting
Accuracy_Random=[]
k=6
for i in range(0,k):
    X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.2,random_state=1000,shuffle=True,stratify=Y)
    X_train = scale.fit_transform(X_train)
    X_test = scale.fit_transform(X_test)
    Accuracy_Random.append(get_Score(NBclf,X_train,Y_train,X_test,Y_test))
Accuracy.append(statistics.mean(Accuracy_Random))

# using K-Cross-Validation for splitting
k=9
kf = StratifiedKFold(n_splits=k)
Accuracy_kFold=[]
for train_index,test_index in kf.split(X,Y):
    X_train,X_test,Y_train,Y_test = X[train_index],X[test_index],Y[train_index],Y[test_index]
    X_train = scale.fit_transform(X_train)
    X_test = scale.fit_transform(X_test)
    Accuracy_kFold.append(get_Score(NBclf,X_train,Y_train,X_test,Y_test))
Accuracy.append(statistics.mean(Accuracy_kFold))
print("Accuracy: ",Accuracy)

# Visualizing the accuracy of the Naive-Bayes Classifier Model for different Splitting models
Yval = Accuracy
plt.bar(Xval,Yval,color="green",width=0.2)
plt.xlabel("Splitting Method")
plt.title("Naive Bayes Classifier Visualization")
plt.show()


# K-Nearest Neighbour Classifier
knn = KNeighborsClassifier(n_neighbors=8)
print("K-Nearest Neighbour")
# Training Size:75% and Test Size:25%
X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=0.25,random_state=1000)
X_train = scale.fit_transform(X_train)
X_test = scale.fit_transform(X_test)
print(f"Accuracy is {get_Score(knn,X_train,Y_train,X_test,Y_test)} with 75% of Training Data")

# Training Size:66.6% and Test Size:33.3%
X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=0.333,random_state=1000)
X_train = scale.fit_transform(X_train)
X_test = scale.fit_transform(X_test)
print(f"Accuracy is {get_Score(knn,X_train,Y_train,X_test,Y_test)} with 66.6% of Training Data")

# 5.2
# Using Hold-Out method for splitting
Accuracy = []
X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.2,random_state=1000,shuffle=True,stratify=Y)
X_train = scale.fit_transform(X_train)
X_test = scale.fit_transform(X_test)
Accuracy.append(get_Score(knn,X_train,Y_train,X_test,Y_test))

# using Random Subsampling for splitting
Accuracy_Random=[]
k=6
for i in range(0,k):
    X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.2,random_state=1000,shuffle=True,stratify=Y)
    X_train = scale.fit_transform(X_train)
    X_test = scale.fit_transform(X_test)
    Accuracy_Random.append(get_Score(knn,X_train,Y_train,X_test,Y_test))
Accuracy.append(statistics.mean(Accuracy_Random))

# using K-Cross-Validation for splitting
k=9
kf = StratifiedKFold(n_splits=k)
Accuracy_kFold=[]
for train_index,test_index in kf.split(X,Y):
    X_train,X_test,Y_train,Y_test = X[train_index],X[test_index],Y[train_index],Y[test_index]
    X_train = scale.fit_transform(X_train)
    X_test = scale.fit_transform(X_test)
    Accuracy_kFold.append(get_Score(knn,X_train,Y_train,X_test,Y_test))
Accuracy.append(statistics.mean(Accuracy_kFold))
print("Accuracy: ",Accuracy)

# Visualizing the accuracy of the K-Nearest Neighbour Model for different Splitting models
Yval = Accuracy
plt.bar(Xval,Yval,color="green",width=0.2)
plt.xlabel("Splitting Method")
plt.title("K-Nearest Neighbor Classifier Visualization")
plt.show()
