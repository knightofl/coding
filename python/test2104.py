from tensorflow import keras
import numpy as np

x = np.array([[0,0], [0,1], [1,0], [1,1]])
y = np.array([[0], [1], [1], [1]])

print(x.shape, y.shape)

model_or = keras.Sequential()

model_or.add(keras.layers.Dense(2, activation='tanh', input_shape=(2,)))
model_or.add(keras.layers.Dense(1, activation='sigmoid'))

optimizer = keras.optimizers.SGD(lr=0.1)
model_or.compile(optimizer=optimizer, loss='binary_crossentropy', metrics=['accuracy'])
model_or.fit(x, y, batch_size=4, epochs=200)

print(model_or.predict(x))
print(np.round(model_or.predict(x)))