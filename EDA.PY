import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from scipy.stats import chi2_contingency
import seaborn as sns
from scipy.stats import ttest_ind
import matplotlib.pyplot as plt

# x = [10, 20, 30, 40, 50]
# y = [15, 30, 45, 60, 75]

# plt.scatter(x, y)
# plt.title("Scatter Plot")
# plt.xlabel("Variable X")
# plt.ylabel("Variable Y")
# plt.show()


#pIERSON CORRELATED

# x = np.array([10, 20, 30, 40, 50])
# y = np.array([15, 30, 45, 60, 75])

# correlation = np.corrcoef(x, y)
# print(f"Pearson Correlation Coefficient: {correlation[0,1]}")


# Linear regration

# x = np.array([10, 20, 30, 40, 50]).reshape(-1, 1)
# y = np.array([15, 30, 45, 60, 75])

# model = LinearRegression()
# model.fit(x, y)
# y_pred = model.predict(x)

# plt.scatter(x, y)
# plt.plot(x, y_pred, color='red')
# plt.title("Linear Regression")
# plt.xlabel("Variable X")
# plt.ylabel("Variable Y")
# plt.show()


# contignency table

# data = {'Gender': ['Male', 'Female', 'Male', 'Female'],
#         'Preference': ['Tea', 'Coffee', 'Tea', 'Coffee']}

# df = pd.DataFrame(data)
# contingency_table = pd.crosstab(df['Gender'], df['Preference'])
# print(contingency_table)


# chi - square test

#Box plot


# data = {'Category': ['A', 'B','C','A', 'B','C'],
#         'Values': [100, 150,200, 120, 180, 220]}

# df = pd.DataFrame(data)

# sns.boxplot(x='Category', y='Values', data=df)
# plt.title("Box Plot")
# plt.show()

#TEST NUMERICAL

group_A = [100, 120, 110, 105, 115]
group_B = [130, 140, 135, 125, 145]

t_stat, p_value = ttest_ind(group_A, group_B)
print(f"T-Test Statistic: {t_stat}, p-value: {p_value}")


#HEATMAP

data = np.array([[1, 2], [3, 4]])

sns.heatmap(data, annot=True)
plt.title("Heatmap")
plt.show()
