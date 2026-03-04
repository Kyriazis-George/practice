
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.metrics import confusion_matrix, classification_report, accuracy_score
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.model_selection import train_test_split, GridSearchCV, cross_val_score

wine = pd.read_csv('C:\\Users\\kyria\\Documents\\Data Analysis Course\\MACHINE LEARNING\\MACHINE LEARNING REAL TIME PROJECT\\Wine quality prediction\\data.csv')
# print(wine)

h = wine.head()
# print(h)

null = wine.isnull().sum()
# print(null)

d = wine.describe()
# print(d)

fig = plt.figure(figsize= (10,6))
sns.barplot(x= 'quality',y = 'fixed acidity', data = wine)

# plt.show()

fig = plt.figure(figsize=(10,6))
sns.barplot(x='quality', y='residual sugar', data=wine)
# plt.show()

bins = (2, 6.5, 8)
group_names = ['bad','good']
wine['quality'] = pd.cut(wine['quality'], bins = bins, labels= group_names)
# print(wine['quality'])

label_quality = LabelEncoder()

wine['quality'] = label_quality.fit_transform(wine['quality'])
w = wine['quality'].value_counts()
# print(w)

x = wine.drop('quality', axis=1)
y = wine['quality']

# print(x,y)

X_train, X_test, y_train, y_test = train_test_split(x,y, test_size= 0.2, random_state=42 )

# print(X_train, X_test, y_train, y_test)

from sklearn.metrics import accuracy_score, classification_report

# Εκπαίδευση RandomForest
rfc = RandomForestClassifier(n_estimators=200, random_state=42)
rfc.fit(X_train, y_train)

# Πρόβλεψη
pred_rfc = rfc.predict(X_test)

# Αξιολόγηση
# print('Accuracy Score =', accuracy_score(y_test, pred_rfc))
# print(classification_report(y_test, pred_rfc))

svc = SVC()
svc.fit(X_train, y_train)
pred_svc = svc.predict(X_test)

# print('Accuracy score =', accuracy_score(y_test, pred_svc))
# print(classification_report(y_test, pred_svc))


param = {
    'C': [0.1,0.8,0.9,1,1.1,1.2,1.3,1.4],
    'kernel':['linear', 'rbf'],
    'gamma' :[0.1,0.8,0.9,1,1.1,1.2,1.3,1.4]
}
grid_svc = GridSearchCV(svc,param, cv=10, verbose=2)

# print(grid_svc)

grid_svc.fit(X_train,y_train)

pred = grid_svc.predict(X_test)
# print('Accuracy score=', accuracy_score(y_test, pred))
# print(classification_report(y_test,pred))

rfc_eval = cross_val_score(estimator = rfc, X = X_train, y = y_train, cv = 10, verbose=2)
r = rfc_eval.mean()
# print(r)