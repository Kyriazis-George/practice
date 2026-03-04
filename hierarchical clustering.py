import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

ds = pd.read_csv('C:\\Users\\kyria\\Documents\\Data Analysis Course\\MACHINE LEARNING\\Unsupervised learning\\hierarchical clustering\\Mall_Customers.csv')
X = ds.iloc[:, 3: ].values
print(X)

import scipy.cluster.hierarchy as sch
dendrogram = sch.dendrogram(sch.linkage(X, method = 'ward'))
plt.title('Dendrogram')
plt.xlabel('Customers')
plt.ylabel('Euclidean distances')
plt.show()

from sklearn.cluster import AgglomerativeClustering
hierarchicalClustering = AgglomerativeClustering(n_clusters = 5, affinity = 'euclidean', linkage = 'ward')
y_hierarchicalClustering = hierarchicalClustering.fit_predict(X)

plt.scatter(X[y_hierarchicalClustering == 0, 0], X[y_hierarchicalClustering == 0, 1], s = 100, c = 'red', label = 'Cluster 1')
plt.scatter(X[y_hierarchicalClustering == 1, 0], X[y_hierarchicalClustering == 1, 1], s = 100, c = 'blue', label = 'Cluster 2')
plt.scatter(X[y_hierarchicalClustering == 2, 0], X[y_hierarchicalClustering == 2, 1], s = 100, c = 'green', label = 'Cluster 3')
plt.scatter(X[y_hierarchicalClustering == 3, 0], X[y_hierarchicalClustering == 3, 1], s = 100, c = 'cyan', label = 'Cluster 4')
plt.scatter(X[y_hierarchicalClustering == 4, 0], X[y_hierarchicalClustering == 4, 1], s = 100, c = 'magenta', label = 'Cluster 5')
plt.title('Clusters of customers')
plt.xlabel('Annual Income (k$)')
plt.ylabel('Spending Score (1-100)')
plt.legend()
plt.show()