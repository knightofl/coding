from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split

cancer = load_breast_cancer()
x_train, x_test, y_train, y_test = train_test_split(
    cancer.data, cancer.target, test_size=0.3, random_state=12)


from sklearn.tree import DecisionTreeClassifier

dt = DecisionTreeClassifier()
dt.fit(x_train, y_train)

print('Depth of tree: ', dt.get_depth())
print('Number of leaves: ', dt.get_n_leaves())

y_pred = dt.predict(x_test)
print(y_pred[0:3])

dt_score = dt.score(x_test, y_test)
print('Accuracy: ', dt_score)


from sklearn.metrics import accuracy_score, precision_score, recall_score

accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred)
recall = recall_score(y_test, y_pred)

print('Accuracy: {0:.4f}, Precision: {1:.4f}, Recall: {2:.4f}'
    .format(accuracy , precision ,recall))


dt = DecisionTreeClassifier(random_state=12)
dt.fit(x_train, y_train)

for i in range(0, len(cancer.feature_names)):
    print('{0}: {1:.3f}'.format(cancer.feature_names[i], dt.feature_importances_[i]))

print('Depth of tree: ', dt.get_depth())
print('Number of leaves: ', dt.get_n_leaves())

dt = DecisionTreeClassifier(max_depth=3, random_state=12)
dt.fit(x_train, y_train)
y_pred = dt.predict(x_test)

accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred)
recall = recall_score(y_test, y_pred)

print('Depth of tree: ', dt.get_depth())
print('Number of leaves: ', dt.get_n_leaves())

print('Accuracy: {0:.4f}, Precision: {1:.4f}, Recall: {2:.4f}'
    .format(accuracy , precision ,recall))

dt = DecisionTreeClassifier(max_depth=9, random_state=12)
dt.fit(x_train, y_train)
y_pred = dt.predict(x_test)

accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred)
recall = recall_score(y_test, y_pred)

print('Depth of tree: ', dt.get_depth())
print('Number of leaves: ', dt.get_n_leaves())

print('Accuracy: {0:.4f}, Precision: {1:.4f}, Recall: {2:.4f}'
    .format(accuracy , precision ,recall))
