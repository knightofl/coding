from tensorflow import keras
import numpy as np
from tensorflow.compat.v1 import ConfigProto, InteractiveSession
config = ConfigProto()
config.gpu_options.per_process_gpu_memory_fraction = 0.4
session = InteractiveSession(config=config)

x = np.array([[0,0], [0,1], [1,0], [1,1]])
y = np.array([[0], [0], [0], [1]])

print(x.shape, y.shape)

model_and = keras.Sequential()

#help(keras.layers.Dense)
model_and.add(keras.layers.Dense(2, activation='sigmoid', input_shape=(2,)))
model_and.add(keras.layers.Dense(1, activation='sigmoid'))

optimizer = keras.optimizers.SGD(lr=0.1)
model_and.compile(optimizer=optimizer, loss='binary_crossentropy', metrics=['accuracy'])
model_and.fit(x, y, batch_size=4, epochs=1000)

print(model_and.predict(x))
print(np.round(model_and.predict(x)))