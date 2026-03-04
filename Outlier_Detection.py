import numpy as np
import matplotlib.pyplot as plt

import pandas as pd
from scipy import stats
import seaborn as sns

from sklearn.cluster import DBSCAN
from sklearn.preprocessing import StandardScaler

from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

from sklearn.neighbors import LocalOutlierFactor
from sklearn.preprocessing import StandardScaler

#z-score

np.random.seed(42)
data_normal = np.random.normal(0, 1, 1000)
data_outliers = np.random.normal(0, 5, 50)
data = np.concatenate([data_normal, data_outliers])

df = pd.DataFrame(data, columns=['value'])
df['zscore'] = (df['value'] - df['value'].mean()) / df['value'].std()

print(df)

outliers_zscore = df[df['zscore'] > 3]
print("Outliers detected using Z-Score:")
print(outliers_zscore)

#box-plot

