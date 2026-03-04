import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

# 1️⃣ Φόρτωση δεδομένων
ds = pd.read_csv('C:\\Users\\kyria\\Documents\\Data Analysis Course\\MACHINE LEARNING\\Unsupervised learning\\k-means clustering\\Mall_Customers1.csv')
X = ds.iloc[:, [3, 4]].values  # Annual Income & Spending Score

# 2️⃣ Elbow Method για να βρούμε το κατάλληλο πλήθος clusters
wcss = [KMeans(n_clusters=i, init='k-means++', random_state=42).fit(X).inertia_ for i in range(1, 11)]

plt.plot(range(1, 11), wcss, marker='o')
plt.title('Elbow Method')
plt.xlabel('Number of clusters')
plt.ylabel('WCSS')
plt.show()

# 3️⃣ K-Means Clustering με 5 clusters (σύμφωνα με το Elbow)
kmeans = KMeans(n_clusters=5, init='k-means++', random_state=42)
y_kmeans = kmeans.fit_predict(X)

# 4️⃣ Οπτικοποίηση clusters
colors = ['red', 'blue', 'green', 'cyan', 'magenta']
labels = ['Cluster 1', 'Cluster 2', 'Cluster 3', 'Cluster 4', 'Cluster 5']

for i in range(5):
    plt.scatter(X[y_kmeans == i, 0], X[y_kmeans == i, 1], s=100, c=colors[i], label=labels[i])

plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], s=300, c='yellow', label='Centroids')
plt.title('Clusters of Customers')
plt.xlabel('Annual Income')
plt.ylabel('Spending Score (1-100)')
plt.legend()
plt.show()