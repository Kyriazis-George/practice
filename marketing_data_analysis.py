import pandas as pd
import matplotlib.pyplot as plt

from sklearn.preprocessing import OrdinalEncoder
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import classification_report, ConfusionMatrixDisplay

path = r"c:\Users\kyria\Documents\Data Analysis Course\MACHINE LEARNING\MACHINE LEARNING REAL TIME PROJECT\Marketing Data Analysis\bank.csv"
df = pd.read_csv(path, sep=';')
df.head()

def wrangle(df):
    # Μετατρέπουμε yes / no σε True / False
    df['y'] = df['y'].map({'yes': True, 'no': False})
    df['default'] = df['default'].map({'yes': True, 'no': False})
    df['housing'] = df['housing'].map({'yes': True, 'no': False})
    df['loan'] = df['loan'].map({'yes': True, 'no': False})

    # Αν ο πελάτης είχε προηγούμενη επαφή
    df['previous_bool'] = df['previous'] > 0

    # Δημιουργία κατηγορίας balance
    q99 = df['balance'].quantile(0.99)

    def balanceator(x):
        if x < 72:
            return 'E'
        elif x < 448:
            return 'D'
        elif x < 1428:
            return 'C'
        elif x < q99:
            return 'B'
        else:
            return 'A'

    df['balance_class'] = df['balance'].apply(balanceator)

    # Στήλες που ΔΕΝ θέλουμε
    drop_cols = ['day', 'poutcome', 'pdays', 'previous']
    df.drop(columns=drop_cols, inplace=True)

    return df

df = wrangle(df)
df.head()

X = df.drop(columns=['y', 'balance', 'duration'])
y = df['y']

encoder = OrdinalEncoder()
X_encoded = encoder.fit_transform(X)

X_train, X_test, y_train, y_test = train_test_split(
    X_encoded,
    y,
    test_size=0.15,
    random_state=42,
    stratify=y
)

params = {
    'max_depth': [5, 10, 20, None],
    'min_samples_split': [2, 5, 10],
    'min_samples_leaf': [1, 2, 5],
    'criterion': ['gini', 'entropy']
}


model = GridSearchCV(
    DecisionTreeClassifier(random_state=42),
    param_grid=params,
    scoring='recall',
    cv=10,
    n_jobs=-1
)


model.fit(X_train, y_train)

y_pred = model.predict(X_test)

print(classification_report(y_test, y_pred))
ConfusionMatrixDisplay.from_estimator(model, X_test, y_test)
plt.show()
