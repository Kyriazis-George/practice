import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

data = {
    'Test Score': [35, 45, 50, 60, 70, 80, 90, 20, 30, 55, 65, 75],
    'Pass/Fail': [0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 1, 1]  # 0 = Fail, 1 = Pass
}

df = pd.DataFrame(data)

# Display first few rows of the dataset
df.head()
print(df)


# plt.scatter(df['Test Score'], df['Pass/Fail'], color="blue")
# plt.title("Scatter plot of Test Scores vs Pass/Fail")
# plt.xlabel("Test Score")
# plt.ylabel("Pass (1) / Fail (0)")
# plt.show()

X = df[['Test Score']]  # Features are in a 2D array
y = df['Pass/Fail']   

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

log_reg = LogisticRegression()
log_reg.fit(X_train, y_train)

print(log_reg)

y_pred = log_reg.predict(X_test)
print(y_pred)

accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)

X_new = np.linspace(10, 100, 1000).reshape(-1, 1)
y_proba = log_reg.predict_proba(X_new)[:, 1]  # Probabilities for class 1

plt.plot(X_new, y_proba, "g-", label="Probability of Passing (Class 1)")
plt.scatter(df['Test Score'], df['Pass/Fail'], color="blue", label="Data Points")
plt.axhline(0.5, color="red", linestyle="--", label="Decision Boundary (p=0.5)")
plt.title("Logistic Regression Decision Boundary")
plt.xlabel("Test Score")
plt.ylabel("Probability of Passing")
plt.legend()
plt.show()