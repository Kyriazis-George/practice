import pandas as pd

df = pd.read_csv("C:\\Users\\kyria\\Documents\\Data Analysis Course\\MACHINE LEARNING\\MACHINE LEARNING REAL TIME PROJECT\\Weather prediction\\seattle-weather.csv")
h = df.head()
# print(h)

null = df.isnull().sum()

# print(null)

def LabelEncoding(c):
    from sklearn import preprocessing
    le = preprocessing.LabelEncoder()
    df[c]= le.fit_transform(df[c])
    df[c].unique()
LabelEncoding("weather")
# print(df)    

cols = ['precipitation', 'temp_max', 'temp_min','wind']

def normalize(df,cols):
    for x in cols:
        df[x] = df[x]/df[x].max()

normalize(df,cols)
# print(df)        

df = df.drop('date',axis=1)
# print(df)

x = df.drop('weather',axis=1)
y = df['weather']

from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y , test_size=0.2, random_state=0)

from xgboost import XGBClassifier

xg = XGBClassifier()
xg.fit(x_train, y_train)

# print(xg)

x = xg.get_params()
# print(x)

from sklearn.metrics import classification_report, accuracy_score

y_hat = xg.predict(x_test)
# print(accuracy_score(y_test,y_hat))
# print(classification_report(y_test,y_hat))

grid = {'learning_rate':[0.1,1,0.01, 0.001], 'gamma':[0,1,10,100]}

from sklearn.model_selection import GridSearchCV

model = GridSearchCV(XGBClassifier(), grid, cv=10, verbose=2)

m = model.fit(x_train, y_train)
# print(m)

grid_predictions = model.predict(x_test)
# print(accuracy_score(y_test, grid_predictions))
# print(classification_report(y_test, grid_predictions))

print()