from sklearn.cluster import DBSCAN
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

data = pd.read_csv('HTRU_2.csv')[:1000]
X=np.array([[i,j] for i,j in zip(data.values[:,0],data.values[:,5])])

clustering = DBSCAN(eps=6,min_samples=5).fit(X)
print(clustering.labels_)

plt.scatter(X[clustering.labels_==0,0],X[clustering.labels_==0,1],color="red")
plt.scatter(X[clustering.labels_==1,0],X[clustering.labels_==1,1],color="blue")
plt.scatter(X[clustering.labels_==2,0],X[clustering.labels_==2,1],color="yellow")
plt.scatter(X[clustering.labels_==3,0],X[clustering.labels_==3,1],color="green")
plt.scatter(X[clustering.labels_==4,0],X[clustering.labels_==4,1],color="brown")
plt.show()