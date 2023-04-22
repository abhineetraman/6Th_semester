import numpy as np
import pandas as pd
import scipy.cluster.hierarchy as shc
import matplotlib.pyplot as plt
from sklearn.cluster import AgglomerativeClustering
data = pd.read_csv('HTRU_2.csv')[:1000]

plt.figure(figsize=(10,7))
plt.title("Dendogram")
X=np.array([[i,j] for i,j in zip(data.values[:,0],data.values[:,5])])
dend = shc.dendrogram(shc.linkage(X[:,0:2],method="ward"))
plt.show()

cluster = AgglomerativeClustering(n_clusters=4,affinity="euclidean",linkage="ward")
labels_=cluster.fit_predict(X[:,0:])

plt.scatter(X[:,0],X[:,1],c=cluster.labels_,cmap="rainbow")
plt.show()