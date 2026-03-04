# ============================================================
# PREDICTING STOCK PRICES USING RANDOM FOREST REGRESSOR
# ============================================================

# ----------------------------
# 1. ΕΙΣΑΓΩΓΗ ΒΙΒΛΙΟΘΗΚΩΝ
# ----------------------------
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

# ----------------------------
# 2. ΦΟΡΤΩΣΗ ΔΕΔΟΜΕΝΩΝ
# ----------------------------
# Διαβάζουμε το αρχείο CSV με τα ιστορικά δεδομένα της TSLA
stock = pd.read_csv(
    'c:\\Users\\kyria\\Documents\\Data Analysis Course\\MACHINE LEARNING\\MACHINE LEARNING REAL TIME PROJECT\\Predicting Stock Prices\\TSLA.csv'
)

# ----------------------------
# 3. ΕΞΕΡΕΥΝΗΣΗ ΔΕΔΟΜΕΝΩΝ
# ----------------------------

# Εμφάνιση πρώτων γραμμών
print(stock.head())

# Έλεγχος για κενές τιμές
print(stock.isnull().sum())

# Στατιστική περιγραφή
print(stock.describe())

# ----------------------------
# 4. ΠΡΟΕΠΕΞΕΡΓΑΣΙΑ ΔΕΔΟΜΕΝΩΝ
# ----------------------------

# Μετατροπή της στήλης Date σε datetime format
stock['Date'] = pd.to_datetime(stock['Date'])

# ----------------------------
# 5. ΟΠΤΙΚΟΠΟΙΗΣΗ ΤΙΜΩΝ
# ----------------------------

plt.figure(figsize=(12,6))
plt.plot(stock['Date'], stock['Close'])
plt.title('TSLA Closing Prices Over Time')
plt.xlabel('Date')
plt.ylabel('Close Price')
plt.xticks(rotation=45)
plt.show()

# ----------------------------
# 6. FEATURE ENGINEERING
# ----------------------------

# Δημιουργία κινητών μέσων όρων
stock['MA_5'] = stock['Close'].rolling(window=5).mean()
stock['MA_10'] = stock['Close'].rolling(window=10).mean()
stock['MA_20'] = stock['Close'].rolling(window=20).mean()

# Ημερήσια μεταβολή τιμής
stock['Daily_Return'] = stock['Close'] - stock['Open']

# Διακύμανση ημέρας
stock['High_Low'] = stock['High'] - stock['Low']

# Αφαίρεση γραμμών με NaN τιμές
stock.dropna(inplace=True)

# ----------------------------
# 7. ΟΡΙΣΜΟΣ FEATURES ΚΑΙ TARGET
# ----------------------------

X = stock[['Open', 'High', 'Low', 'Volume',
           'MA_5', 'MA_10', 'MA_20',
           'Daily_Return', 'High_Low']]

# Στόχος: τιμή κλεισίματος
y = stock['Close']

# ----------------------------
# 8. TRAIN / TEST SPLIT (TIME SERIES)
# ----------------------------

# Χωρίζουμε τα δεδομένα χρονικά (80% train, 20% test)
split_index = int(len(stock) * 0.8)

X_train = X.iloc[:split_index]
X_test = X.iloc[split_index:]

y_train = y.iloc[:split_index]
y_test = y.iloc[split_index:]

# ----------------------------
# 9. ΔΗΜΙΟΥΡΓΙΑ & ΕΚΠΑΙΔΕΥΣΗ ΜΟΝΤΕΛΟΥ
# ----------------------------

rf_model = RandomForestRegressor(
    n_estimators=100,
    max_depth=10,
    random_state=42
)

# Εκπαίδευση μοντέλου
rf_model.fit(X_train, y_train)

# ----------------------------
# 10. ΠΡΟΒΛΕΨΕΙΣ
# ----------------------------

y_pred = rf_model.predict(X_test)

# ----------------------------
# 11. ΑΞΙΟΛΟΓΗΣΗ ΜΟΝΤΕΛΟΥ
# ----------------------------

mae = mean_absolute_error(y_test, y_pred)
rmse = np.sqrt(mean_squared_error(y_test, y_pred))
r2 = r2_score(y_test, y_pred)

print(f"MAE: {mae:.2f}")
print(f"RMSE: {rmse:.2f}")
print(f"R² Score: {r2:.3f}")

# ----------------------------
# 12. ΟΠΤΙΚΟΠΟΙΗΣΗ ΠΡΑΓΜΑΤΙΚΩΝ vs ΠΡΟΒΛΕΨΕΩΝ
# ----------------------------

plt.figure(figsize=(12,6))
plt.plot(y_test.values, label='Actual Prices')
plt.plot(y_pred, label='Predicted Prices')
plt.title('Actual vs Predicted TSLA Prices')
plt.xlabel('Time')
plt.ylabel('Close Price')
plt.legend()
plt.show()

# ----------------------------
# 13. FEATURE IMPORTANCE
# ----------------------------

importances = rf_model.feature_importances_

importance_df = pd.DataFrame({
    'Feature': X.columns,
    'Importance': importances
}).sort_values(by='Importance', ascending=False)

print(importance_df)
