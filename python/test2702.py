import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
import pandas as pd
from sklearn.preprocessing import MinMaxScaler

x = np.arange(0, 100, 0.1)
y = np.sin(x)

df = pd.DataFrame(data=y, index=x, columns=['sinewave'])

scaler = MinMaxScaler()
all_scaler = scaler.fit_transform(df)
print(all_scaler)

all_timeseries = tf.keras.preprocessing.sequence.TimeseriesGenerator(
    all_scaler, all_scaler, 50, batch_size=1)

LSTM_model = tf.keras.Sequential()
LSTM_model.add(tf.keras.layers.LSTM(128, input_shape=(50,1)))
LSTM_model.add(tf.keras.layers.Dense(1))

LSTM_model.compile(loss='mse', optimizer='adam')
LSTM_model.fit(all_timeseries, epochs=5)

forecast = []
batch = all_scaler[-50:]
current_batch = batch.reshape(1, 50, 1)
print(len(batch))

for i in range(100):
    current_predict = LSTM_model.predict(current_batch)
    forecast.append(current_predict[0])
    current_batch = np.append(current_batch[:, 1:, :] , [current_predict], axis=1)

print(current_batch, len(current_batch), len(current_batch[0]))

forecast_index = np.arange(100, 110, 0.1)
print(len(forecast), len(forecast_index))


forecast1 = scaler.inverse_transform(forecast)

plt.plot(df.index, df.sinewave)
plt.plot(forecast_index, forecast1)
plt.show()


plt.plot(df.index, all_scaler)
plt.plot(forecast_index, forecast)
plt.show()

