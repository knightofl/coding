import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import tensorflow as tf
from tensorflow import keras


df = pd.read_csv('./practice/pimaindians-diabetes.csv',
    names=['pregnant', 'plasma', 'pressure', 'thickness',
        'insulin', 'BMI', 'pedigree', 'age', 'class'])

print(df.dtypes)
print(df.info())
print(df.head())
print(df.tail())

print(df[['thickness', 'class']])


dataset = np.loadtxt('./practice/pimaindians-diabetes.csv', delimiter=',')
print(dataset.shape)

x_train = dataset[:, 0:8]
t_train = dataset[:, 8]
print(x_train, x_train.shape)
print(t_train, t_train.shape)

t_train = np.eye(2)[t_train.astype(int)]
print(t_train, t_train.shape)

model = keras.Sequential()
model.add(keras.layers.Dense(40, activation='relu', input_dim=x_train.shape[1]))
model.add(keras.layers.Dense(80, activation='relu'))
model.add(keras.layers.Dense(t_train.shape[1], activation='sigmoid'))

model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
history = model.fit(x_train, t_train, batch_size=10, epochs=200)


result = model.evaluate(x_train, t_train)
print(result)

print(x_train[0])
predict = model.predict([[6., 148., 72., 35.,  0., 33.6, 0.627, 50.]])
print(predict)


loss = history.history['loss']
accuracy = history.history['accuracy']

x = np.arange(len(loss))
plt.plot(x, loss, label='train loss')
plt.xlabel('epoch')
plt.ylabel('loss')
plt.legend(loc='best')
plt.show()

x = np.arange(len(accuracy))
plt.plot(x, accuracy, label='train accuracy')
plt.xlabel('epoch')
plt.ylabel('accuracy')
plt.legend(loc='best')
plt.show()

