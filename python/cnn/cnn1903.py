import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder
from tensorflow import keras


df = pd.read_csv('./practice/sonar.csv', header=None)
print(df.info)

dataset = df.values
print(dataset)

x = dataset[:, 0:60].astype(float)
t = dataset[:, 60]
print(t)

e = LabelEncoder()
e.fit(t)
t = e.transform(t)
t = keras.utils.to_categorical(t)
print(t, t.shape)


model = keras.Sequential()
model.add(keras.layers.Dense(40, activation='relu', input_dim=x.shape[1]))
model.add(keras.layers.Dense(20, activation='relu'))
model.add(keras.layers.Dense(t.shape[1], activation='sigmoid'))

model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
history = model.fit(x, t, batch_size=5, epochs=80)

loss = history.history['loss']
accuracy = history.history['accuracy']

x = np.arange(len(loss))
plt.plot(x, loss)
plt.show()

x = np.arange(len(accuracy))
plt.plot(x, accuracy)
plt.show()

