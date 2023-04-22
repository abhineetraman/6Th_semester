import pandas as pd
import math
import csv
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

data = pd.read_csv('./breast-cancer.csv')
updatedData=[[] for i in range(10)]
updatedData[0]=(list(data.values[:,0]))
X=data.values[:,1:]
i=0
for i in range(0,len(X)):
    index = X[i][0].index("-")
    lval = int(X[i][0][0:index])
    gval = int(X[i][0][index+1:])
    temp = lval + math.ceil((gval-lval)/2)
    updatedData[1].append(temp)

    if X[i][1] == "premeno":
        updatedData[2].append(0)
    elif X[i][1] == "ge40":
        updatedData[2].append(1)
    elif X[i][1] == "lt40":
        updatedData[2].append(2)
    else:
        updatedData[2].append(3)

    index = X[i][2].index("-")
    lval = int(X[i][2][0:index])
    gval = int(X[i][2][index+1:])
    temp = lval + math.ceil((gval-lval)/2)
    updatedData[3].append(temp)

    index = X[i][3].index("-")
    lval = int(X[i][3][0:index])
    gval = int(X[i][3][index+1:])
    temp = lval + math.ceil((gval-lval)/2)
    updatedData[4].append(temp)

    if X[i][4]=="no":
        updatedData[5].append(0)
    else:
        updatedData[5].append(1)
    
    updatedData[6].append(X[i][5])

    if X[i][6]=="left":
        updatedData[7].append(0)
    else:
        updatedData[7].append(1)

    if X[i][7]=="left_low":
        updatedData[8].append(0)
    elif X[i][7]=="left_up":
        updatedData[8].append(1)
    elif X[i][7]=="right_low":
        updatedData[8].append(2)
    elif X[i][7]=="right_up":
        updatedData[8].append(3)
    else:
        updatedData[8].append(4)

    if X[i][8]=="no":
        updatedData[9].append(0)
    else:
        updatedData[9].append(1)

with open("breast_cancer_updated.csv",'w',newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Class","Age","Menopause","Tumor-Size","Inv-nodes","Node-Caps","Deg-Malig","Breast","Breast-Quad","Irradiat"])
    for i in range(0,len(updatedData[0])):
        temp = [updatedData[j][i] for j in range(0,10)]
        print(temp)
        writer.writerow(temp)

def get_Score(model,X_train,Y_train,X_test,Y_test):
    model.fit(X_train,Y_train)
    return model.score(X_test,Y_test)*100

scale = StandardScaler()

newData = pd.read_csv("./breast_cancer_updated.csv")
X=newData[0:].values[:,1:]
Y=newData[0:].values[:,0]
Xval=["Hold-Out","Random Sub-Sampling","Cross-Validation"]

# Decision Tree Classifier
# Training Size:75% and Test Size:25%
print("Decision-Tree Classifier")
clf=DecisionTreeClassifier()
X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=0.25,random_state=1000)
X_train = scale.fit_transform(X_train)
X_test = scale.fit_transform(X_test)
clf.fit(X_train,Y_train)

print("Accuracy is {0:.3f} with 75% of training data".format(get_Score(clf,X_train,Y_train,X_test,Y_test)))

# Training Size:66.6% and Test Size:33.3%
X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=0.333,random_state=1000)
X_train = scale.fit_transform(X_train)
X_test = scale.fit_transform(X_test)
clf=DecisionTreeClassifier()
clf.fit(X_train,Y_train)

print("Accuracy is {0:.3f} with 66.6% of training data".format(get_Score(clf,X_train,Y_train,X_test,Y_test)))

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
