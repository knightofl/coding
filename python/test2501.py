import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
from sklearn.metrics import confusion_matrix

from tensorflow.compat.v1 import ConfigProto, InteractiveSession
config = ConfigProto()
config.gpu_options.per_process_gpu_memory_fraction = 0.4
session = InteractiveSession(config=config)

(x_train, y_train), (x_test, y_test) = tf.keras.datasets.fashion_mnist.load_data()

num = len(set(y_train))
print(x_test[0].shape, num)

plt.imshow(x_test[0], 'gray')
plt.show()

print(x_train.shape, y_train.shape, x_test.shape, y_test.shape)
x_data = x_train.reshape(-1, 28, 28, 1) / 255.0 # np.expand_dims(x_train, -1)
y_data = y_train
test = x_test.reshape(-1, 28, 28, 1) / 255.0
true = y_test

fashion_mnist_model = tf.keras.Sequential()
fashion_mnist_model.add(tf.keras.layers.Conv2D(128, kernel_size=(3,3),
    activation='relu', input_shape=(28,28,1)))
fashion_mnist_model.add(tf.keras.layers.MaxPooling2D(pool_size=(2,2)))
fashion_mnist_model.add(tf.keras.layers.Flatten())
fashion_mnist_model.add(tf.keras.layers.Dense(100, activation='relu'))
fashion_mnist_model.add(tf.keras.layers.Dense(num, activation='softmax'))

fashion_mnist_model.compile(loss='sparse_categorical_crossentropy', optimizer='Adam', metrics=['accuracy'])
fashion_mnist_model.fit(x_data, y_data, batch_size=100, epochs=5)

print(np.round(fashion_mnist_model.predict(test)))
predict = fashion_mnist_model.predict(test).argmax(axis=1)
print(confusion_matrix(predict, true))

miss = np.where(predict != true)
print(miss)

idx = np.random.choice(miss[0])
f_name = {0:'T-shirt/top', 1:'Trouser', 2:'Pullover', 3:'Dress', 4:'Coat',
    5:'Sandal', 6:'Shirt', 7:'Sneaker', 8:'Bag', 9:'Ankle boot'}

plt.imshow(x_test[idx])
plt.title("True : %s, Predict : %s" % (f_name[true[idx]], f_name[predict[idx]]))
plt.show()

print(fashion_mnist_model.layers)
print(fashion_mnist_model.layers[0].name)
print(fashion_mnist_model.layers[0].output)

