from tensorflow import keras
import numpy as np

x = np.array([[0,0], [0,1], [1,0], [1,1]])
y = np.array([[1], [1], [1], [0]])

print(x.shape, y.shape)

model_nand = keras.Sequential()

model_nand.add(keras.layers.Dense(2, activation='tanh', input_shape=(2,)))
model_nand.add(keras.layers.Dense(1, activation='sigmoid'))

optimizer = keras.optimizers.SGD(lr=0.1)
model_nand.compile(optimizer=optimizer, loss='binary_crossentropy', metrics=['accuracy'])
model_nand.fit(x, y, batch_size=4, epochs=200)

print(model_nand.predict(x))
print(np.round(model_nand.predict(x)))