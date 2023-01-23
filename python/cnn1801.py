import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
from tensorflow import keras


# mnist data load
(x_train, t_train), (x_test, t_test) = keras.datasets.mnist.load_data()
print(x_train.shape, x_train.dtype, t_train.shape, t_train.dtype)
print(x_test.shape, x_train.dtype, t_test.shape, t_test.dtype)

# flatten, normalize
x_train = x_train.reshape(-1, 28*28) / 255.0
x_test = x_test.reshape(-1, 28*28) / 255.0
print(x_train.shape, x_test.shape)

# one hot label encoding
element = len(set(t_train))
t_train = np.eye(element)[t_train]
t_test = np.eye(element)[t_test]
print(t_train.shape, t_test.shape)


print(tf.__version__)
print(keras.__version__)


model = keras.Sequential()
model.add(keras.layers.Dense(50, activation='relu', input_dim=x_train.shape[1]))
model.add(keras.layers.Dense(t_train.shape[1], activation='softmax'))

model.compile(optimizer='sgd', loss='categorical_crossentropy', metrics=['accuracy'])
history = model.fit(x_train, t_train, validation_data=(x_test, t_test),
    batch_size=100, epochs=20, verbose=1)

loss = history.history['loss']
val_loss = history.history['val_loss']
accuracy = history.history['accuracy']
val_accuracy = history.history['val_accuracy']


result = model.evaluate(x_test, t_test)
print(result)

x = np.arange(len(loss))
plt.plot(x, loss, marker='.', c='blue', label='train loss')
plt.plot(x, val_loss, marker='.', c='red', label='test loss')
plt.xlabel('epoch')
plt.ylabel('loss')
plt.legend(loc='best')
plt.show()

plt.plot(x, accuracy, marker='.', c='blue', label='train accuracy')
plt.plot(x, val_accuracy, marker='.', c='red', label='test accuracy')
plt.xlabel('epoch')
plt.ylabel('accuracy')
plt.legend(loc='best')
plt.show()

