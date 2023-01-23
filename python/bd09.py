from re import L
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import VotingClassifier

cancer = load_breast_cancer()
x_train, x_test, y_train, y_test = train_test_split(
    cancer.data, cancer.target, test_size=0.3, random_state=12)

lr = LogisticRegression(random_state=12, max_iter=5000)
dt = DecisionTreeClassifier(random_state=12)
knn_clf = KNeighborsClassifier(n_neighbors=8)
voting = VotingClassifier(estimators=[('LR',lr), ('DT', dt), ('KNN', knn_clf)], voting='soft')

voting.fit(x_train, y_train)
y_pred = voting.predict(x_test)
print('Accuracy: {0:.3f}'.format(accuracy_score(y_test, y_pred)))


classifiers = [lr, dt, knn_clf]

for classifier in classifiers :
    classifier.fit(x_train, y_train)
    y_pred = classifier.predict(x_test)
    class_name = classifier.__class__.__name__
    
    print('{0} Accuracy:{1:.4f}'. format(class_name, accuracy_score(y_test, y_pred)))


from sklearn.ensemble import RandomForestClassifier

rf = RandomForestClassifier(random_state=12)
rf.fit(x_train, y_train)
y_pred = rf.predict(x_test)
print('Accuracy: {0:.3f}'.format(accuracy_score(y_test, y_pred)))


from sklearn.model_selection import GridSearchCV

params = {'n_estimators':[100],
        'max_depth':[6, 8, 10, 12],
        'min_samples_leaf':[8, 12, 18 ],
        'min_samples_split':[8, 16, 20]}

rf_clf = RandomForestClassifier(random_state=0, n_jobs=-1)

grid_cv = GridSearchCV(rf_clf, param_grid=params, cv=2, n_jobs=-1)
grid_cv.fit(x_train, y_train)

print('Optimal Hyper Parameter') 
print(grid_cv.best_params_)
print('Max Accuracy: {0:.4f}'.format(grid_cv.best_score_)) 

rf_clf1 = RandomForestClassifier(n_estimators=300,
                                 max_depth=6,
                                 min_samples_leaf=8,
                                 min_samples_split=8,
                                 random_state=0)

rf_clf1.fit(x_train , y_train)
y_pred = rf_clf1.predict(x_test) 

print('Accuracy: {0:.4f}'.format(accuracy_score(y_test , y_pred))) 


import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

ftr_importances_values = rf_clf1.feature_importances_
ftr_importances = pd.Series(ftr_importances_values, index=cancer.feature_names)

ftr_top20 = ftr_importances.sort_values(ascending=False)[:20]

plt.figure(figsize=(8, 6))
plt.title('Feature importances Top 20')
sns.barplot(x=ftr_top20, y=ftr_top20.index)
plt.show()
