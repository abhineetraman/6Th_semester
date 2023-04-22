
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

data = pd.read_csv('HTRU_2.csv')[:1000]

wcss=[]
for i in range(1,20):
    km=KMeans(n_clusters=i)
    km.fit_predict(data)
    wcss.append(km.inertia_)

plt.plot(range(1,20),wcss)
plt.show()

X=data.iloc[:,:].values
km = KMeans(n_clusters=6)
Y_means = km.fit_predict(X)

first=0
second=5
print(X[Y_means==0,first])
plt.scatter(X[Y_means==0,first],X[Y_means==0,second],color="red")
plt.scatter(X[Y_means==1,first],X[Y_means==1,second],color="blue")
plt.scatter(X[Y_means==2,first],X[Y_means==2,second],color="yellow")
plt.scatter(X[Y_means==3,first],X[Y_means==3,second],color="green")
plt.scatter(X[Y_means==4,first],X[Y_means==4,second],color="brown")

plt.show()

