from tensorflow import keras
import numpy as np

x = np.array([[0,0], [0,1], [1,0], [1,1]])
y = np.array([[0], [1], [1], [0]])

print(x.shape, y.shape)

model_xor = keras.Sequential()

model_xor.add(keras.layers.Dense(2, activation='tanh', input_shape=(2,)))
model_xor.add(keras.layers.Dense(1, activation='sigmoid'))

optimizer = keras.optimizers.SGD(lr=0.1)
model_xor.compile(optimizer=optimizer, loss='binary_crossentropy', metrics=['accuracy'])
model_xor.fit(x, y, batch_size=4, epochs=1000)

print(model_xor.predict(x))
print(np.round(model_xor.predict(x)))