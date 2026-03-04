import pandas as pd
import numpy as np

data = {
    'Customer_ID': [101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120],
    'Customer_Age': [25, 30, np.nan, 45, 23, np.nan, 36, 50, np.nan, 29, 42, 38, np.nan, 27, 31, np.nan, 55, 60, np.nan, 33],
    'Customer_Income': [50000, 60000, np.nan, 40000, 45000, np.nan, 55000, 62000, 58000, np.nan, 53000, np.nan, 46000, 50000, 47000, 55000, np.nan, 61000, 48000, np.nan],
    'Purchase_History': [5, np.nan, 2, 8, 4, np.nan, 7, 10, np.nan, 3, 6, np.nan, 9, np.nan, 5, 4, 8, 9, np.nan, 7],
    'Product_Rating': [4, 5, np.nan, np.nan, 3, 4, np.nan, 5, 2, 3, np.nan, 4, 5, 3, np.nan, 5, 4, 5, 3, np.nan]
}

df = pd.DataFrame(data)
print(df)

count = len(data['Customer_Age'])
print(count)




# print(df)

# write your code here for Mean, Mode, Median Imputation

#Mean mputation

# df['Customer_Age_imputated'] = df['Customer_Age'].fillna(df['Customer_Age'].mean())
# # print(df['Customer_Age_imputated'])

# df['Customer_Income_imputated'] = df['Customer_Income'].fillna(df['Customer_Income'].mean())
# # print(df['Customer_Income_imputated'])

# df['Purchase_History_imputated'] = df['Purchase_History'].fillna(df['Purchase_History'].mean())
# # print(df['Purchase_History_imputated'])

# df['Product_Rating'] = df['Product_Rating'].fillna(df['Product_Rating'].mean())
# # print(df['Product_Rating'])

# #Median Imputation

# df['Customer_Age_imputated'] = df['Customer_Age'].fillna(df['Customer_Age'].median())
# # print(df['Customer_Age_imputated'])

# df['Customer_Income_imputated'] = df['Customer_Income'].fillna(df['Customer_Income'].median())
# # print(df['Customer_Income_imputated'])

# df['Purchase_History_imputated'] = df['Purchase_History'].fillna(df['Purchase_History'].median())
# # print(df['Purchase_History_imputated'])

# df['Product_Rating'] = df['Product_Rating'].fillna(df['Product_Rating'].median())
# # print(df['Product_Rating'])

# # mode imputation

# df['Customer_Age_imputated'] = df['Customer_Age'].fillna(df['Customer_Age'].mode()[0])
# # print(df['Customer_Age_imputated'])

# df['Customer_Income_imputated'] = df['Customer_Income'].fillna(df['Customer_Income'].mode()[0])
# # print(df['Customer_Income_imputated'])

# df['Purchase_History_imputated'] = df['Purchase_History'].fillna(df['Purchase_History'].mode()[0])
# # print(df['Purchase_History_imputated'])

# df['Product_Rating'] = df['Product_Rating'].fillna(df['Product_Rating'].mode()[0])
# # print(df['Product_Rating'])

# # write your code here for Removing Rows (IF Necessary)

# df_dropna = df.dropna(subset=['Customer_Age'])
# # print(df_dropna)

# write your code here for Forward Fill, Backward Fill

# Forward Fill

# df['Customer_Age'] = df['Customer_Age'].fillna(method='ffill')
# print(df['Customer_Age'])

# df['Customer_Income'] = df['Customer_Income'].fillna(method='ffill')
# print(df['Customer_Income'])

# df['Purchase_History'] = df['Purchase_History'].fillna(method='ffill')
# print(df['Purchase_History'])

# df['Product_Rating'] = df['Product_Rating'].fillna(method='ffill')
# print(df['Product_Rating'])

# Backward Fill

# df['Customer_Age'] = df['Customer_Age'].fillna(method='bfill')
# print(df['Customer_Age'])

# df['Customer_Income'] = df['Customer_Income'].fillna(method='bfill')
# print(df['Customer_Income'])

# df['Purchase_History'] = df['Purchase_History'].fillna(method='bfill')
# print(df['Purchase_History'])

# df['Product_Rating'] = df['Product_Rating'].fillna(method='bfill')
# print(df['Product_Rating'])