import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from tensorflow import keras


data_file = './practice/thoracic-surgery.csv'

df = pd.read_csv(data_file, header=None, delim_whitespace=True)
print(df.info)

dataset = np.loadtxt(data_file, delimiter=',')
print(dataset.shape)

x = np.array(dataset[:, 0:17])
t = np.array(dataset[:, 17])
print(x.shape, t.shape)

t = np.eye(2)[t.astype(int)]
print(t.shape)

model = keras.Sequential()
model.add(keras.layers.Dense(30, activation='relu', input_dim=x.shape[1]))
model.add(keras.layers.Dense(t.shape[1], activation='sigmoid'))

model.compile(optimizer='sgd', loss='binary_crossentropy', metrics=['accuracy'])
history = model.fit(x, t, batch_size=20, epochs=300)

loss = history.history['loss']
accuracy = history.history['accuracy']

x = np.arange(len(loss))
plt.plot(x, loss)
plt.show()

x = np.arange(len(accuracy))
plt.plot(x, accuracy)
plt.show()

