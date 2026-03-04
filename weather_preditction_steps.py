# ================================
# 1. Εισαγωγή βιβλιοθηκών
# ================================

import pandas as pd   # Για φόρτωση και επεξεργασία δεδομένων


# ================================
# 2. Φόρτωση του dataset
# ================================

# Διαβάζουμε το αρχείο CSV που περιέχει δεδομένα καιρού
df = pd.read_csv(
    "C:\\Users\\kyria\\Documents\\Data Analysis Course\\MACHINE LEARNING\\MACHINE LEARNING REAL TIME PROJECT\\Weather prediction\\seattle-weather.csv"
)

# Εμφάνιση των 5 πρώτων γραμμών (για έλεγχο)
h = df.head()
# print(h)


# ================================
# 3. Έλεγχος για κενές τιμές
# ================================

# Ελέγχουμε αν υπάρχουν missing values σε κάθε στήλη
null = df.isnull().sum()
# print(null)


# ================================
# 4. Μετατροπή κατηγορικών δεδομένων (Label Encoding)
# ================================

def LabelEncoding(column):
    """
    Μετατρέπει κατηγορικές τιμές (π.χ. rain, sun)
    σε αριθμητικές (0,1,2...)
    """
    from sklearn import preprocessing

    le = preprocessing.LabelEncoder()
    df[column] = le.fit_transform(df[column])

    # Επιστρέφει τις μοναδικές τιμές μετά την κωδικοποίηση
    return df[column].unique()


# Εφαρμογή Label Encoding στη στήλη weather
LabelEncoding("weather")
# print(df)


# ================================
# 5. Επιλογή αριθμητικών χαρακτηριστικών
# ================================

# Στήλες που θα κανονικοποιηθούν
cols = ['precipitation', 'temp_max', 'temp_min', 'wind']


# ================================
# 6. Κανονικοποίηση δεδομένων (Normalization)
# ================================

def normalize(df, columns):
    """
    Κανονικοποιεί τις τιμές κάθε στήλης
    διαιρώντας με τη μέγιστη τιμή της στήλης
    """
    for col in columns:
        df[col] = df[col] / df[col].max()


# Εφαρμογή κανονικοποίησης
normalize(df, cols)
# print(df)


# ================================
# 7. Αφαίρεση μη χρήσιμης στήλης
# ================================

# Η στήλη date δεν βοηθά άμεσα στην πρόβλεψη
df = df.drop('date', axis=1)
# print(df)


# ================================
# 8. Διαχωρισμός δεδομένων (Features & Target)
# ================================

# Χαρακτηριστικά εισόδου
X = df.drop('weather', axis=1)

# Μεταβλητή στόχος
y = df['weather']


# ================================
# 9. Διαχωρισμός σε training & testing set
# ================================

from sklearn.model_selection import train_test_split

# 80% εκπαίδευση - 20% έλεγχος
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=0
)


# ================================
# 10. Δημιουργία και εκπαίδευση μοντέλου XGBoost
# ================================

from xgboost import XGBClassifier

# Δημιουργία μοντέλου
xg_model = XGBClassifier()

# Εκπαίδευση του μοντέλου
xg_model.fit(X_train, y_train)


# ================================
# 11. Πρόβλεψη και αξιολόγηση μοντέλου
# ================================

from sklearn.metrics import accuracy_score, classification_report

# Πρόβλεψη αποτελεσμάτων στο test set
y_pred = xg_model.predict(X_test)

# Υπολογισμός ακρίβειας
# print("Accuracy:", accuracy_score(y_test, y_pred))

# Αναλυτική αναφορά ταξινόμησης
# print(classification_report(y_test, y_pred))


# ================================
# 12. Ορισμός πλέγματος υπερπαραμέτρων
# ================================

# Υπερπαράμετροι προς βελτιστοποίηση
param_grid = {
    'learning_rate': [0.1, 1, 0.01, 0.001],
    'gamma': [0, 1, 10, 100]
}


# ================================
# 13. Grid Search με Cross Validation
# ================================

from sklearn.model_selection import GridSearchCV

# Δημιουργία GridSearch
grid_model = GridSearchCV(
    XGBClassifier(),
    param_grid,
    cv=10,          # 10-fold cross validation
    verbose=2
)

# Εκπαίδευση GridSearch
grid_model.fit(X_train, y_train)


# ================================
# 14. Αξιολόγηση βελτιστοποιημένου μοντέλου
# ================================

# Πρόβλεψη με το καλύτερο μοντέλο
grid_predictions = grid_model.predict(X_test)

# print("Grid Accuracy:", accuracy_score(y_test, grid_predictions))
# print(classification_report(y_test, grid_predictions))


# ================================
# Τέλος προγράμματος
# ================================
