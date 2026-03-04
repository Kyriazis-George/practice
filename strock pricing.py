import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestRegressor
from sklearn.svm import SVC
from sklearn.metrics import confusion_matrix, classification_report, accuracy_score
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.model_selection import train_test_split, GridSearchCV, cross_val_score

stock = pd.read_csv('c:\\Users\\kyria\\Documents\\Data Analysis Course\\MACHINE LEARNING\\MACHINE LEARNING REAL TIME PROJECT\\Predicting Stock Prices\\TSLA.csv')
# print(stock)

h = stock.head()
# print(h)

null = stock.isnull().sum()
# print(null)

d = stock.describe()
# print(d)


plt.figure(figsize=(12,6))
plt.plot(stock['Date'], stock['Close'])
plt.title('TSLA Closing Prices')
plt.xlabel('Date')
plt.ylabel('Close Price')
plt.xticks(rotation=45)
# plt.show()

stock['Date'] = pd.to_datetime(stock['Date'])

# Κινητοί μέσοι όροι
stock['MA_5'] = stock['Close'].rolling(window=5).mean()
stock['MA_10'] = stock['Close'].rolling(window=10).mean()
stock['MA_20'] = stock['Close'].rolling(window=20).mean()

# Ημερήσιες διαφορές
stock['Daily_Return'] = stock['Close'] - stock['Open']
stock['High_Low'] = stock['High'] - stock['Low']

X = stock[['Open', 'High', 'Low', 'Volume', 'MA_5', 'MA_10', 'MA_20', 'Daily_Return', 'High_Low']]
y = stock['Close']

split_index = int(len(stock) * 0.8)
X_train = X.iloc[:split_index]
X_test = X.iloc[split_index:]

y_train = y.iloc[:split_index]
y_test = y.iloc[split_index:]

print(X_train.shape, X_test.shape)
print(y_train.shape, y_test.shape)

from sklearn.ensemble import RandomForestRegressor

rf_model = RandomForestRegressor(
    n_estimators=100,
    random_state=42,
    max_depth=10
)

rf_model.fit(X_train, y_train)
y_pred = rf_model.predict(X_test)

from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import numpy as np

mae = mean_absolute_error(y_test, y_pred)
rmse = np.sqrt(mean_squared_error(y_test, y_pred))
r2 = r2_score(y_test, y_pred)

print(f"MAE: {mae:.2f}")
print(f"RMSE: {rmse:.2f}")
print(f"R² Score: {r2:.3f}")


plt.figure(figsize=(12,6))
plt.plot(y_test.values, label='Actual')
plt.plot(y_pred, label='Predicted')
plt.title('Actual vs Predicted Stock Prices')
plt.xlabel('Time')
plt.ylabel('Close Price')
plt.legend()
# plt.show()

importances = rf_model.feature_importances_
features = X.columns

importance_df = pd.DataFrame({
    'Feature': features,
    'Importance': importances
}).sort_values(by='Importance', ascending=False)

print(importance_df)