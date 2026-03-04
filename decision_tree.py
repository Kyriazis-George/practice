# import pandas as pd
# from sklearn.model_selection import train_test_split
# from sklearn.tree import DecisionTreeClassifier, export_graphviz
# from sklearn.metrics import accuracy_score
# import graphviz
# import numpy as np
# from collections import Counter

# from sklearn.preprocessing import LabelEncoder
# label_encoder = LabelEncoder()

# data = pd.read_csv(r"C:\Users\kyria\Documents\Data Analysis Course\MACHINE LEARNING\supervised learning\decision tree\Descion Tree\Employee.csv")
# data.fillna(0)
# data.head()
# head = data.head()


# data['City_encoded'] = label_encoder.fit_transform(data['City'])
# data['Education_encoded'] = label_encoder.fit_transform(data['Education'])
# data['Gender_encoded'] = label_encoder.fit_transform(data['Gender'])
# data['EverBenched_encoded'] = label_encoder.fit_transform(data['EverBenched'])

# data.drop(columns=['Education','City','Gender','EverBenched'],inplace=True)
# y = data['LeaveOrNot']
# # print(y)


# X = data.drop('LeaveOrNot', axis=1)
# X


# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
# decision_tree = DecisionTreeClassifier(random_state=42)
# decision_tree.fit(X_train, y_train)

# y_pred = decision_tree.predict(X_test)
# acc = accuracy_score(y_test, y_pred)
# print(f"Accuracy : {acc}")

# dot_data = export_graphviz(decision_tree, out_file=None,
#                            feature_names=X.columns,
#                            class_names=['Stay', 'Leave'],
#                            filled=True, rounded=True,
#                            special_characters=True)
# graph = graphviz.Source(dot_data)
# graph


# graph.view()


data = [
    ['Sunny', 'Hot', 'High', 'Weak', 'No'],
    ['Sunny', 'Hot', 'High', 'Strong', 'No'],
    ['Overcast', 'Hot', 'High', 'Weak', 'Yes'],
    ['Rain', 'Mild', 'High', 'Weak', 'Yes'],
    ['Rain', 'Cool', 'Normal', 'Weak', 'Yes'],
    ['Rain', 'Cool', 'Normal', 'Strong', 'No'],
    ['Overcast', 'Cool', 'Normal', 'Strong', 'Yes'],
    ['Sunny', 'Mild', 'High', 'Weak', 'No'],
    ['Sunny', 'Cool', 'Normal', 'Weak', 'Yes'],
    ['Rain', 'Mild', 'Normal', 'Weak', 'Yes'],
    ['Sunny', 'Mild', 'Normal', 'Strong', 'Yes'],
    ['Overcast', 'Mild', 'High', 'Strong', 'Yes'],
    ['Overcast', 'Hot', 'Normal', 'Weak', 'Yes'],
    ['Rain', 'Mild', 'High', 'Strong', 'No']
]

header = ['Outlook', 'Temp', 'Humidity', 'Wind', 'PlayTennis']

import numpy as np
from collections import Counter

# Gini Impurity Calculation
def gini_impurity(groups, classes):
    total_instances = sum(len(group) for group in groups)
    gini = 0.0
    
    for group in groups:
        if len(group) == 0:
            continue
        score = 0.0
        class_counts = Counter(row[-1] for row in group)
        for class_val in classes:
            proportion = class_counts[class_val] / len(group)
            score += proportion * proportion
        gini += (1.0 - score) * (len(group) / total_instances)
    
    return gini

# Split Dataset
def split_dataset(index, value, dataset):
    left, right = [], []
    for row in dataset:
        if row[index] == value:
            left.append(row)
        else:
            right.append(row)
    return left, right

# Best Split Function
def get_best_split(dataset):
    class_values = list(set(row[-1] for row in dataset))
    best_index, best_value, best_gini, best_groups = 999, None, 999, None
    
    for index in range(len(dataset[0]) - 1):
        for row in dataset:
            groups = split_dataset(index, row[index], dataset)
            gini = gini_impurity(groups, class_values)
            if gini < best_gini:
                best_index, best_value, best_gini, best_groups = index, row[index], gini, groups
                
    return {'index': best_index, 'value': best_value, 'groups': best_groups}

# Terminal Node
def create_terminal(group):
    outcomes = [row[-1] for row in group]
    return Counter(outcomes).most_common(1)[0][0]

# Recursive Splitting
def split(node, max_depth, min_size, depth):
    left, right = node['groups']
    del(node['groups'])
    
    if not left or not right:
        node['left'] = node['right'] = create_terminal(left + right)
        return
    
    if depth >= max_depth:
        node['left'], node['right'] = create_terminal(left), create_terminal(right)
        return
    
    if len(left) <= min_size:
        node['left'] = create_terminal(left)
    else:
        node['left'] = get_best_split(left)
        split(node['left'], max_depth, min_size, depth + 1)
    
    if len(right) <= min_size:
        node['right'] = create_terminal(right)
    else:
        node['right'] = get_best_split(right)
        split(node['right'], max_depth, min_size, depth + 1)

# Build Tree
def build_tree(train, max_depth, min_size):
    root = get_best_split(train)
    split(root, max_depth, min_size, 1)
    return root

# Prediction
def predict(node, row):
    if row[node['index']] == node['value']:
        if isinstance(node['left'], dict):
            return predict(node['left'], row)
        else:
            return node['left']
    else:
        if isinstance(node['right'], dict):
            return predict(node['right'], row)
        else:
            return node['right']

# Decision Tree
def decision_tree(train, test, max_depth, min_size):
    tree = build_tree(train, max_depth, min_size)
    predictions = [predict(tree, row) for row in test]
    return predictions

# Example usage
# Using entire data as training set
train_data = data
test_data = [
    ['Sunny', 'Cool', 'High', 'Strong'],
    ['Rain', 'Mild', 'Normal', 'Weak']
]

# Build and test the Decision Tree
max_depth = 3
min_size = 1
predictions = decision_tree(train_data, test_data, max_depth, min_size)

# Output predictions
for i, prediction in enumerate(predictions):
    print(f"Test data point {i+1}: Prediction = {prediction}")

