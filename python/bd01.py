# scikit-learn
import sklearn
print(sklearn.__version__)

# iris dataset load
from sklearn.datasets import load_iris
iris = load_iris()

print(iris.DESCR)
print(iris.feature_names)
print(iris.data)
print(iris.data.shape)
print(iris.target)
print(iris.target_names)
print(type(iris.data))


# pandas 로 변환
import pandas as pd

df = pd.DataFrame(iris.data, columns=iris.feature_names)
print(df)


# 데이터 분할
from sklearn.model_selection import train_test_split

x_train, x_test, y_train, y_test =\
    train_test_split(iris.data, iris.target, test_size=0.3, random_state=12)

print('x_train.shape', x_train.shape)
print('y_train.shape', y_train.shape)
print('x_test.shape', x_test.shape)
print('y_test.shape', y_test.shape)


# K 최근접 이웃 알고리즘 KNN
# https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KNeighborsClassifier.html
from sklearn.neighbors import KNeighborsClassifier

knn = KNeighborsClassifier(n_neighbors=7)
print(type(knn))

knn.fit(x_train, y_train)
y_pred = knn.predict(x_test)
print('Prediction :\n', y_pred)

score = knn.score(x_test, y_test)
print('Accuracy : {0:.5f}'.format(score))

# n_neighbors 값을 변경해 가면서 knn 모델 학습 및 검증
k_list = range(1, 100, 2)
acc_train = []
acc_test = []

for k in k_list:
    knn = KNeighborsClassifier(n_neighbors=k)
    knn.fit(x_train, y_train)
    
    acc_train.append(knn.score(x_train, y_train))
    acc_test.append(knn.score(x_test, y_test))

print(acc_test)

import matplotlib.pyplot as plt

plt.figure(figsize=(10, 4))
plt.plot(k_list, acc_train, 'b--', label='Training Data')
plt.plot(k_list, acc_test, 'g', label='Testing Data')
plt.title("Traning and Testing Accuracy")
plt.xlabel('k')
plt.ylabel('Accuracy')
plt.ylim(0.8, 1.0)
plt.legend()
plt.show()
