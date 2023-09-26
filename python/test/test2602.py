import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
import pandas as pd
from sklearn.preprocessing import MinMaxScaler


x = np.arange(0, 100, 0.1)
y = np.sin(x)

#plt.plot(x, y)
#plt.show()

df = pd.DataFrame(data=y, index=x, columns=['sine wave'])
print(df, df.shape, df.ndim)
df.plot()
plt.show()

train = df.iloc[:800]
test = df.iloc[800:]
print(train)

scaler = MinMaxScaler()
scaler.fit(train)
x_train = scaler.transform(train)
scaler.fit(test)
x_test = scaler.transform(test)
print(x_train)

df_train = pd.DataFrame(data=x_train, index=x[:800], columns=['sine wave train'])
df_train.plot()
plt.show()

df_test = pd.DataFrame(data=x_test, index=x[800:], columns=['sine wave test'])
df_test.plot()
plt.show()

#help(tf.keras.preprocessing.sequence.TimeseriesGenerator)
rnn_train = tf.keras.preprocessing.sequence.TimeseriesGenerator(
    data=x_train, targets=x_train, length=2, batch_size=1)
print(rnn_train, len(rnn_train))

print(x_train[:5])
print(rnn_train[0])
print(rnn_train[1])

rnn_train = tf.keras.preprocessing.sequence.TimeseriesGenerator(
    x_train, x_train, 10, batch_size=1)
print(rnn_train[0], len(rnn_train))

features = 1
model = tf.keras.Sequential()
model.add(tf.keras.layers.LSTM(128, input_shape=(10, features)))
model.add(tf.keras.layers.Dense(1))

model.compile(loss='mse', optimizer='adam')
print(model.summary())
model.fit(rnn_train, epochs=5)

pd.DataFrame(model.history.history).plot()
plt.show()

rnn_test = tf.keras.preprocessing.sequence.TimeseriesGenerator(
    x_test, x_test, 10, batch_size=1)
predict = model.predict(rnn_test)
print(len(predict), len(df_test))

df_test1 = df_test.drop(df_test.index[:10])
print(df_test1, len(df_test1))
df_test1['predict wave'] = predict
df_test1.plot()
plt.show()