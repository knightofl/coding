import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import tensorflow as tf


def make_dataset(data, label, window_size=20):
    feature_list = []
    label_list = []
    for i in range(len(data) - window_size):
        feature_list.append(np.array(data.iloc[i:i+window_size]))
        label_list.append(np.array(label.iloc[i+window_size]))
    return np.array(feature_list), np.array(label_list)

df_price = pd.read_csv('./practice/01-삼성전자-주가.csv', encoding='utf8')
print(df_price.describe())

df_price['일자'] = pd.to_datetime(df_price['일자'], format='%Y%m%d')
df_price['연도'] = df_price['일자'].dt.year
df_price['월'] = df_price['일자'].dt.month
df_price['일'] = df_price['일자'].dt.day

df = df_price.loc[df_price['연도']>=1990]

plt.figure(figsize=(16, 9))
plt.plot(df['일자'], df['종가'])
plt.xlabel('time')
plt.ylabel('price')
plt.show()

from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler()
scale_cols = ['시가', '고가', '저가', '종가', '거래량']
df_scaled = scaler.fit_transform(df[scale_cols])
df_scaled = pd.DataFrame(df_scaled)
df_scaled.columns = scale_cols
print(df_scaled)

TEST_SIZE = 200
train = df_scaled[:-TEST_SIZE]
test = df_scaled[-TEST_SIZE:]

feature_cols = ['시가', '고가', '저가', '거래량']
label_cols = ['종가']

train_feature = train[feature_cols]
train_label = train[label_cols]

from sklearn.model_selection import train_test_split
train_feature, train_label = make_dataset(train_feature, train_label, 20)
x_train, x_valid, y_train, y_valid = train_test_split(train_feature, train_label, test_size=0.2)
print(x_train.shape, x_valid.shape)

test_feature = test[feature_cols]
test_label = test[label_cols]
test_feature, test_label = make_dataset(test_feature, test_label, 20)
print(test_feature.shape, test_label.shape)

model = tf.keras.Sequential()
model.add(tf.keras.layers.LSTM(16, input_shape=(train_feature.shape[1],
    train_feature.shape[2]), activation='relu', return_sequences=False))
model.add(tf.keras.layers.Dense(1))

model.compile(loss='mean_squared_error', optimizer='adam')
early_stop = tf.keras.callbacks.EarlyStopping(monitor='val_loss', patience=5)
filename = './tmp/checkpoint.h5'
checkpoint = tf.keras.callbacks.ModelCheckpoint(
    filename, monitor='val_loss', verbose=1, save_best_only=True, mode='auto')

history = model.fit(x_train, y_train, epochs=200, batch_size=16,
    validation_data=(x_valid, y_valid), callbacks=[early_stop, checkpoint])

model.load_weights(filename)
predict = model.predict(test_feature)

plt.figure(figsize=(12, 9))
plt.plot(test_label, label='actual')
plt.plot(predict, label='predict')
plt.legend()
plt.show()
