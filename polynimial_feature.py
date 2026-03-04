import pandas as pd

# Δημιουργία ενός μικρού dataset
data = {
    'Age': [25, 32, 47, 51],
    'Income': [50000, 60000, 80000, 90000]
}

df = pd.DataFrame(data)
print("Αρχικό DataFrame:")
print(df)

# Δημιουργία ενός interaction feature: προϊόν Age και Income
df['Age_Income'] = df['Age'] * df['Income']

# Δημιουργία άλλου interaction feature: λόγος Income / Age
df['Income_per_Age'] = df['Income'] / df['Age']

print("\nDataFrame με interaction features:")
print(df)