import pandas as pd
import numpy as np

df = pd.read_csv(r'C:\Users\kyria\Documents\Data Analysis Course\Python\MODULES\pandas\Churn_Modelling.csv')

# print(df)
# a = df.Balance
# print(a)

# df['New Balance'] = df['Balance'] + 1000
# df.head(5)
# print(df.head(5))

# df['Randon Column'] = 'Good Day'
# print(df.head(5))

# a = df[10:18]
# print(a)

age_50 = df[df.Age > 50]
b = age_50.head(5)
print(b)