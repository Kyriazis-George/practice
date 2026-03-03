import numpy as np
from scipy.cluster.hierarchy import linkage

# Μικρό dataset 2D
X = np.array([[1, 2],
              [3, 4],
              [5, 6],
              [7, 8],
              [1, 0],
              [0, 1]])

# Δημιουργία linkage matrix με μέθοδο 'ward'
Z = linkage(X, method='ward')

print("Linkage matrix:\n", Z)