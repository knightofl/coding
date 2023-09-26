import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
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

x_train, x_test, t_train, t_test = train_test_split(x, t, test_size=0.2, random_state=0)
print(x_train.shape, x_test.shape, t_train.shape, t_test.shape)


model = keras.Sequential()
model.add(keras.layers.Dense(40, activation='relu', input_dim=x_train.shape[1]))
model.add(keras.layers.Dense(20, activation='relu'))
model.add(keras.layers.Dense(t_train.shape[1], activation='sigmoid'))

model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
history = model.fit(x_train, t_train, validation_data=(x_test, t_test),
    batch_size=5, epochs=70)

loss = history.history['loss']
val_loss = history.history['val_loss']
accuracy = history.history['accuracy']
val_accuracy = history.history['val_accuracy']

x = np.arange(len(loss))
plt.plot(x, loss, label='loss')
plt.plot(x, val_loss, label='val_loss')
plt.legend()
plt.show()

x = np.arange(len(accuracy))
plt.plot(x, accuracy, label='accuracy')
plt.plot(x, val_accuracy, label='val_accuracy')
plt.legend()
plt.show()


model.save('./model1904')
del model
model = keras.models.load_model('./model1904')
result = model.evaluate(x_test, t_test)
print(result)

