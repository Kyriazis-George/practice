from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score, classification_report

iris = load_iris()
X = iris.data
y = iris.target


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

model = GaussianNB()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

print("Accuracy:", accuracy_score(y_test, y_pred))
print(classification_report(y_test, y_pred))


from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score


# Δείγμα δεδομένων
texts = ["Free money now!!!", "Hello friend", "Win a prize", "How are you?"]
labels = [1, 0, 1, 0]  # 1=spam, 0=ham


# Μετατροπή κειμένου σε αριθμητικά χαρακτηριστικά
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(texts)

# Διαχωρισμός δεδομένων
X_train, X_test, y_train, y_test = train_test_split(X, labels, test_size=0.25)

# Εκπαίδευση μοντέλου
model = MultinomialNB()
model.fit(X_train, y_train)

# Πρόβλεψη & Ακρίβεια
y_pred = model.predict(X_test)
print("Accuracy:", accuracy_score(y_test, y_pred))
