import numpy as np
import matplotlib.pyplot as plt
from tensorflow import keras

(x_train, y_train), (x_test, y_test) = keras.datasets.mnist.load_data()

x_data = x_train.reshape(-1, 28, 28, 1) / 255.0
y_data = y_train
test = x_test.reshape(-1, 28, 28, 1) / 255.0
true = y_test

callbacks = [
    keras.callbacks.EarlyStopping(patience=3, monitor='val_loss'),
    keras.callbacks.TensorBoard(log_dir='./logs', histogram_freq=1)]

mnist_model = keras.Sequential()
mnist_model.add(keras.layers.Conv2D(28, kernel_size=(3,3), input_shape=(28,28,1)))
mnist_model.add(keras.layers.MaxPooling2D(pool_size=(2,2)))
mnist_model.add(keras.layers.Flatten())
mnist_model.add(keras.layers.Dense(128, activation='relu'))
mnist_model.add(keras.layers.Dense(10, activation='softmax'))

mnist_model.compile(optimizer='Adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
mnist_model.fit(x_data, y_data, batch_size=100, epochs=5,
    validation_data=(x_data, y_data), callbacks=callbacks)

print(np.round(mnist_model.predict(test)))
predict = np.round(mnist_model.predict(test)).argmax(axis=1)

from sklearn.metrics import confusion_matrix
print(confusion_matrix(predict, true))

miss = np.where(predict != true)
idx = np.random.choice(miss[0])

plt.imshow(x_test[idx])
plt.title("True : %s, Predict : %s" % (true[idx], predict[idx]))
plt.show()