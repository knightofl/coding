import re
import numpy as np
import pandas as pd

from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

df_bike = pd.read_csv('./practice/bike_demand_kaggle.csv')
print(df_bike.head(5))

df_bike['y'] = 1
print(df_bike.head(5))

df_bike.loc[df_bike['count'] < 500, 'y'] = 0
print(df_bike.head(5))
print(df_bike.loc[df_bike['count'] >= 500].head(5))

y = df_bike['y']
print(y.value_counts())

x_df_bike = df_bike.iloc[:, 5:9]
print(x_df_bike.head(5))
print(x_df_bike.describe())

scaler = StandardScaler()
scaler.fit(x_df_bike)
result = scaler.transform(x_df_bike)

x_scaled_bike = pd.DataFrame(data=result, columns=x_df_bike.columns)

x_train, x_test, y_train, y_test =\
    train_test_split(x_scaled_bike, y, test_size=0.3, random_state=12)

clf = LogisticRegression()
clf.fit(x_train, y_train)
y_pred = clf.predict(x_test)

train_score = clf.score(x_train, y_train)
test_score = clf.score(x_test,  y_test)
print('Training Data Accuracy: {:0.3f}'.format(train_score))
print('Testing Data Accuracy: {:0.3f}'.format(test_score))


from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score

confusion = confusion_matrix(y_test, y_pred)
print('Confusion Matrixs: \n', confusion)

accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred)
recall = recall_score(y_test, y_pred)
print('Accuracy: {0:.4f}, Precision: {1:.4f}, Recall: {2:.4f}'
    .format(accuracy , precision ,recall))

