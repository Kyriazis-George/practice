import pandas as pd
import numpy as np

# Creating a sample real estate dataset
# data = {
#     'Size': [1500, 2000, 2500, 1800, 2300, 1700, 2100, 1600, 2400, 2200],
#     'Price': [300000, 400000, 500000, 350000, 450000, 330000, 380000, 320000, 490000, 430000],
#     'Bedrooms': [3, 4, 5, 3, 4, 2, 4, 3, 5, 4],
#     'Location': ['Urban', 'Suburban', 'Rural', 'Urban', 'Suburban', 'Rural', 'Urban', 'Rural', 'Suburban', 'Urban'],
#     'Has_Garden': [1, 0, 1, 0, 1, 1, 0, 0, 1, 0]
# }

# df = pd.DataFrame(data)

# print(df)

# write your code here for Min-Max Normalization

# df = pd.DataFrame(data)

# df["Size normalized"] = (df['Size'] - df['Size'].min()) / (df["Size"].max() - df["Size"].min())
# df["Price normalized"] = (df['Price'] - df['Price'].min()) / (df["Price"].max() - df["Price"].min())

# print(df)

# write your code here for Encoding Categorical data

#frequency encoding 

import numpy as np
import matplotlib.pyplot as plt

import pandas as pd
from sklearn.preprocessing import LabelEncoder

# data = {'Location': ['Urban', 'Suburban', 'Rural', 'Urban', 'Suburban', 'Rural', 'Urban', 'Rural', 'Suburban', 'Urban']}
# df = pd.DataFrame(data)

# # Frequency Encoding
# freq_encoding = df['Location'].value_counts() / len(df)
# df['Location_Freq_Encoded'] = df['Location'].map(freq_encoding)

# print(df)

#one hot encoding

# data = {'Location': ['Urban', 'Suburban', 'Rural', 'Urban', 'Suburban', 'Rural', 'Urban', 'Rural', 'Suburban', 'Urban']}
# df = pd.DataFrame(data)

# # One-Hot Encoding
# df_one_hot = pd.get_dummies(df['Location'], prefix='Location')

# df = pd.concat([df, df_one_hot], axis=1)

# print(df)

#LABEL ENCODER

# data = {'Location': ['Urban', 'Suburban', 'Rural', 'Urban', 'Suburban', 'Rural', 'Urban', 'Rural', 'Suburban', 'Urban']}
# df = pd.DataFrame(data)

# label_encoder = LabelEncoder()
# df['Location_Label_Encoded'] = label_encoder.fit_transform(df['Location'])

# print(df)

#TARGED ENCODING


# data = {
#     'Size': [1500, 2000, 2500, 1800, 2300, 1700, 2100, 1600, 2400, 2200],
#     'Price': [300000, 400000, 500000, 350000, 450000, 330000, 380000, 320000, 490000, 430000],
#     'Bedrooms': [3, 4, 5, 3, 4, 2, 4, 3, 5, 4],
#      'Location': ['Urban', 'Suburban', 'Rural', 'Urban', 'Suburban', 'Rural', 'Urban', 'Rural', 'Suburban', 'Urban'],
#    'Has_Garden': [1, 0, 1, 0, 1, 1, 0, 0, 1, 0]
# }
# df = pd.DataFrame(data)


# location_means = df.groupby('Location')['Price'].mean()
# df['Location_Target'] = df['Location'].map(location_means)

# bedroom_means = df.groupby('Bedrooms')['Price'].mean()
# df['Bedroom_Target'] = df['Bedrooms'].map(bedroom_means)


# print(df)

