import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
import pandas as pd
from sklearn.preprocessing import MinMaxScaler


x = np.arange(0, 100, 0.1)
y = np.sin(x)

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

df_train = pd.DataFrame(data=x_train, index=x[:800], columns=['sine wave train'])
df_train.plot()
plt.show()

df_test = pd.DataFrame(data=x_test, index=x[800:], columns=['sine wave test'])
df_test.plot()
plt.show()

rnn_train = tf.keras.preprocessing.sequence.TimeseriesGenerator(
    data=x_train, targets=x_train, length=50, batch_size=1)
print(rnn_train[0], len(rnn_train))

features = 1
model = tf.keras.Sequential()
model.add(tf.keras.layers.SimpleRNN(128, input_shape=(50, features)))
model.add(tf.keras.layers.Dense(1))

model.compile(loss='mse', optimizer='adam')
print(model.summary())
model.fit(rnn_train, epochs=5)

pd.DataFrame(model.history.history).plot()
plt.show()


rnn_test = tf.keras.preprocessing.sequence.TimeseriesGenerator(
    x_test, x_test, 50, batch_size=1)
predict = model.predict(rnn_test)
true_predict = scaler.inverse_transform(predict)


df_test1 = test.drop(test.index[:50])
print(len(true_predict), len(df_test1), df_test1, type(df_test1))
df_test1['true predict wave'] = true_predict
df_test1.plot()
plt.show()


df_test2 = df_test.drop(df_test.index[:50])
print(len(predict), len(df_test2), df_test2, type(df_test2))
df_test2['predict wave'] = predict
df_test2.plot()
plt.show()

