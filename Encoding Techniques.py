import numpy as np
import matplotlib.pyplot as plt

import pandas as pd
from sklearn.preprocessing import LabelEncoder


# frequancy encoding


# data = {'Color': ['Red', 'Green', 'Blue', 'Green', 'Red', 'Red']}
# df = pd.DataFrame(data)

# freq_encoding = df['Color'].value_counts() / len(df)
# df['Color_Freq_Encoded'] = df['Color'].map(freq_encoding)

# print(df)

#target encoding

# data = {'Color': ['Red', 'Green', 'Blue', 'Green', 'Red', 'Red'],
#         'Sale_Price': [100, 150, 200, 150, 100, 120]}
# df = pd.DataFrame(data)

# target_means = df.groupby('Color')['Sale_Price'].mean()
# df['Color_Target_Encoded'] = df['Color'].map(target_means)

# print(df)

#one hot encoding

# data = {'Color': ['Red', 'Green', 'Blue', 'Green', 'Red', 'Red']}
# df = pd.DataFrame(data)

# df_one_hot = pd.get_dummies(df['Color'], prefix='Color')

# print(df)

# label encoding

data = {'Color': ['Red', 'Green', 'Blue', 'Green', 'Red', 'Red']}
df = pd.DataFrame(data)

label_encoder = LabelEncoder()
df['Color_Label_Encoded'] = label_encoder.fit_transform(df['Color'])

print(df)
