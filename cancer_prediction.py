# Βασικές βιβλιοθήκες
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Σταθερότητα αποτελεσμάτων
np.random.seed(42)

# Φόρτωση δεδομένων
data = pd.read_csv('c:\\Users\\kyria\\Documents\\Data Analysis Course\\MACHINE LEARNING\\MACHINE LEARNING REAL TIME PROJECT\\Predicting Cancer Malignant or Benign\\data-cancer.csv')

# Πρώτες γραμμές του dataset
print(data.head())

# Έλεγχος για κενά δεδομένα
print(data.isnull().sum())

# Σχήμα του dataset (γραμμές, στήλες)
print(data.shape)

# Μετατροπή διαγνώσεων σε αριθμούς: M=1, B=0
data['diagnosis'] = data['diagnosis'].map({'M':1,'B':0})

# Διαγραφή της στήλης id (δεν είναι χρήσιμη)
del data['id']

# Διαχωρισμός χαρακτηριστικών και στόχου
X = data.drop('diagnosis', axis=1)  # Χαρακτηριστικά
y = data['diagnosis']               # Στόχος

print(X.head())
print(y.head())

# Κατανομή διαγνώσεων
A = data['diagnosis'].value_counts()

# Bar plot
plt.bar(A.index, A.values, color=['#21908d','#440154'])
plt.title("Distribution of Diagnosis")
plt.xlabel("Diagnosis (0=Benign, 1=Malignant)")
plt.ylabel("Count")
plt.show()

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# Δημιουργία μοντέλου
dt = DecisionTreeClassifier(random_state=42)
dt.fit(X_train, y_train)

# Προβλέψεις
y_pred = dt.predict(X_test)

# Αξιολόγηση
print("Accuracy:", accuracy_score(y_test, y_pred))
print("\nConfusion Matrix:\n", confusion_matrix(y_test, y_pred))
print("\nClassification Report:\n", classification_report(y_test, y_pred))

from sklearn.model_selection import cross_val_score

depths = range(1, 21)
train_acc = []
val_acc = []

for depth in depths:
    dt = DecisionTreeClassifier(max_depth=depth, random_state=42)
    dt.fit(X_train, y_train)
    train_acc.append(accuracy_score(y_train, dt.predict(X_train)))
    val_acc.append(np.mean(cross_val_score(dt, X_train, y_train, cv=10)))

# Plot
plt.plot(depths, train_acc, label='Training Accuracy')
plt.plot(depths, val_acc, label='Cross-Validation Accuracy')
plt.xlabel('Tree Depth')
plt.ylabel('Accuracy')
plt.title('Decision Tree Depth vs Accuracy')
plt.legend()
plt.show()


# Εμφάνιση σημαντικότητας χαρακτηριστικών
importance = pd.Series(dt.feature_importances_, index=X.columns)
importance.sort_values(ascending=False, inplace=True)
print("Feature Importances:\n", importance)

# Plot
plt.figure(figsize=(10,6))
sns.barplot(x=importance.values, y=importance.index, palette="viridis")
plt.title("Feature Importance in Decision Tree")
plt.show()


from sklearn import tree

plt.figure(figsize=(20,10))
tree.plot_tree(dt, feature_names=X.columns, class_names=['Benign','Malignant'], filled=True)
plt.show()
