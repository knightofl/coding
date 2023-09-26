import numpy as np
from tensorflow import keras

x = np.array([[0,0], [0,1], [1,0], [1,1]])
y = np.array([[0], [1], [1], [0]])

xor = keras.Sequential()

xor.add(keras.layers.Dense(4, activation='tanh'))
xor.add(keras.layers.Dense(2, activation='tanh'))
xor.add(keras.layers.Dense(1, activation="sigmoid"))

optimizer = keras.optimizers.SGD(lr=0.1)
xor.compile(optimizer=optimizer, loss='binary_crossentropy', metrics=['accuracy'])
xor.fit(x, y, batch_size=4, epochs=1000)

print(xor.predict(x))
print(np.around(xor.predict(x)))