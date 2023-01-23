import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.datasets import mnist

(x_train, y_train), (x_test, y_test) = mnist.load_data()

x_data = x_train.reshape(-1, 28*28) / 255.0
print(x_data.shape)
test = x_test.reshape(-1, 28*28) / 255.0

print(y_train.shape)
#y_data = keras.utils.to_categorical(y_train)
y_data = np.eye(10)[y_train]
print(y_data.shape)
true = y_test

mnist_model = keras.Sequential()
mnist_model.add(keras.layers.Dense(50, activation='relu', input_shape=(784,)))
mnist_model.add(keras.layers.Dense(100, activation='relu'))
mnist_model.add(keras.layers.Dense(10, activation='softmax'))

mnist_model.compile(optimizer='Adam', loss='categorical_crossentropy', metrics=['accuracy'])
mnist_model.fit(x_data, y_data, batch_size=500, epochs=10)

print(mnist_model.predict(test))
print(np.round(mnist_model.predict(test)))

predict = np.round(mnist_model.predict(test)).argmax(axis=1)

from sklearn.metrics import confusion_matrix
print(confusion_matrix(predict, true))

miss = np.where(predict != true)
print(miss)

i = np.random.choice(miss[0])
plt.imshow(x_test[i])
plt.title("True : %s, Predict : %s" % (true[i], predict[i]))
plt.show()
