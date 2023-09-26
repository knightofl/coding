import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
import pandas as pd
from sklearn.preprocessing import MinMaxScaler

np.random.seed(2020)

x = np.arange(30 * 12)
time = x / 30.0
print(x, time)
y = 20 * np.where(time < 0.5,
    np.cos(2*np.pi * time),
    np.cos(2*np.pi * time) * np.random.random(360))

plt.figure(figsize=(10, 5))
plt.plot(x, y)
plt.show()

df = pd.DataFrame(data=y, index=x, columns=['month_time'])
scaler = MinMaxScaler()
all_scaler = scaler.fit_transform(df)

all_timeseries = tf.keras.preprocessing.sequence.TimeseriesGenerator(
    all_scaler, all_scaler, 45, batch_size=1)

LSTM_model = tf.keras.Sequential()
LSTM_model.add(tf.keras.layers.LSTM(50, input_shape=(45,1)))
LSTM_model.add(tf.keras.layers.Dense(1))

LSTM_model.compile(loss='mse', optimizer='adam')
LSTM_model.fit(all_timeseries, epochs=5)

forecast = []
batch = all_scaler[-45:]
current_batch = batch.reshape(1, 45, 1)
print(len(batch))

for i in range(40):
    current_predict = LSTM_model.predict(current_batch)
    forecast.append(current_predict[0])
    current_batch = np.append(current_batch[:, 1:, :], [current_predict], axis=1)

print(current_batch, len(current_batch), len(current_batch[0]))

forecast_index = np.arange(360, 400)
print(len(forecast), len(forecast_index))


forecast1 = scaler.inverse_transform(forecast)

plt.plot(df.index, df.month_time)
plt.plot(forecast_index, forecast1)
plt.show()

plt.plot(df.index, all_scaler)
plt.plot(forecast_index, forecast)
plt.show()

