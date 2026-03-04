# Importing Libraries 

import numpy as np
import pandas as pd

employe_data = {
    'Age': [25, np.nan, 28, 29, np.nan, 32, 35],
    'Salary': [50000, 54000, np.nan, 58000, 60000, np.nan, 63000],
    'Category': ['A', 'B', 'B', 'A', np.nan, 'B', 'A']
}

df = pd.DataFrame(employe_data)
# print(df)

# 1. Mean, Median, Mode Imputation
# Mean Imputation

df['Age_mean_imputated'] = df['Age'].fillna(df['Age'].mean())
print(df['Age_mean_imputated'])

# df['Age_median_imputated'] = df['Age'].fillna(df['Age'].median())
# # print(df['Age_median_imputated'])

# df['Age_mode']= df['Age'].fillna(df['Age'].mode())
# print(df['Age_mode'])

# df['Salary_median'] = df['Salary'].fillna(df['Salary'].median())
# # print(df['Salary_median'])

# df['Salary_mean'] = df['Salary'].fillna(df['Salary'].mean())
# print(df['Salary_mean'])

# df['Salary_mode'] = df['Salary'].fillna(df['Salary'].mode()[0])
# print(df['Salary_mode'])

# df_dropna = df.dropna()
# print(df_dropna)

# df['Salary_interpolated'] = df['Salary'].interpolate(method='linear')
# print(df['Salary_interpolated'])

# df['Salary_interpolated'] = df['Salary'].interpolate(method='spline')
# print(df['Salary_interpolated'])

# df['Salary_ffill'] = df['Salary'].fillna(method='ffill')
# print(df['Salary_ffill'])

# df['Salary_bfill'] = df['Salary'].fillna(method='bfill')
# print(df['Salary_bfill'])

# df['Age_bfill'] = df['Age'].fillna(method='bfill')
# print(df['Age_bfill'])