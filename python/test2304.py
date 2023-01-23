import numpy as np
import matplotlib.pyplot as plt
from tensorflow import keras

(x_train, y_train), (x_test, y_test) = keras.datasets.mnist.load_data()

x_data = x_train / 255.0
y_data = y_train
test = x_test /255.0
true = y_test

input = keras.layers.Input(shape=(28, 28))
output = keras.layers.Flatten()(input)
output = keras.layers.Dense(128, activation='relu')(output)
output = keras.layers.Dense(10, activation='softmax')(output)
mnist_model = keras.Model(input, output)

mnist_model.compile(optimizer='Adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
mnist_model.fit(x_data, y_data, batch_size=500, epochs=10)

print(np.round(mnist_model.predict(test)))
predict = np.round(mnist_model.predict(test)).argmax(axis=1)

from sklearn.metrics import confusion_matrix
print(confusion_matrix(predict, true))

miss = np.where(predict != true)
idx = np.random.choice(miss[0])

plt.imshow(x_test[idx])
plt.title("True : %s, Predict : %s" % (true[idx], predict[idx]))
plt.show()