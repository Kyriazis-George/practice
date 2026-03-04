import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

iris = datasets.load_iris()
X = iris.data[:, :2]  # Use only the first two features for visualization
y = iris.target

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


k = 3  
knn = KNeighborsClassifier(n_neighbors=k)
knn.fit(X_train, y_train)


y_pred = knn.predict(X_test)


accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy * 100:.2f}%")


# Visualization
# Create a mesh grid for plotting decision boundaries
x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
xx, yy = np.meshgrid(np.arange(x_min, x_max, 0.01),
                     np.arange(y_min, y_max, 0.01))

# Predict the class for each point in the mesh grid
Z = knn.predict(np.c_[xx.ravel(), yy.ravel()])
Z = Z.reshape(xx.shape)

# Plot the decision boundaries
plt.figure(figsize=(10, 6))
plt.contourf(xx, yy, Z, alpha=0.2, cmap=plt.cm.coolwarm)  # Reduced alpha for clearer view of clusters

# Scatter plot for training and testing data points
plt.scatter(X_train[:, 0], X_train[:, 1], c=y_train, marker='o', label='Training Data', edgecolor='k', alpha=0.7)
plt.scatter(X_test[:, 0], X_test[:, 1], c=y_test, marker='s', label='Test Data', edgecolor='k', alpha=0.9)

plt.title(f"K-Nearest Neighbors (K={k}) Classification")
plt.xlabel(iris.feature_names[0])  # Label for feature 1
plt.ylabel(iris.feature_names[1])  # Label for feature 2
plt.legend()
plt.show()