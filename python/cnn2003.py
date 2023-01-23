import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from tensorflow import keras


'''
 0 : 주석산 농도
 1 : 아세트산 농도
 2 : 구연산 농도
 3 : 잔류 당분 농도
 4 : 염화나트륨 농도
 5 : 유리 아황산 농도
 6 : 총 아황산 농도
 7 : 밀도
 8 : pH
 9 : 황산화칼륨 농도
10 : 알코올 도수
11 : 와인의 맛(0~10등급)
12 : class(0:화이트와인, 1: 레드와인)
'''

dateset_file = './practice/wine.csv'
df = pd.read_csv(dateset_file, header=None)
df = df.sample(frac=1)

dataset = df.values
x = dataset[:, 0:12]
t = dataset[:, 12]

t = t[:, np.newaxis]
t = np.c_[t, t == 0]

# 2. model frame config
model = keras.Sequential()
model.add(keras.layers.Dense(30, input_dim=x.shape[1], activation='relu'))
model.add(keras.layers.Dense(16, activation='relu'))
model.add(keras.layers.Dense(8, activation='relu'))
model.add(keras.layers.Dense(2, activation='softmax'))

# 3. model fitting config
model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

# 4. model check point config
checkpoint = keras.callbacks.ModelCheckpoint(
    filepath='{epoch:03d}-{val_loss:.4f}.h5',
    monitor='val_loss',     # val_loss(시험셋 오차), loss(학습셋 오차), val_accuracy(시험셋 정확도), accuracy(학습셋 정확도)
    verbose=1,
    save_best_only=True
)

earlyStopping = keras.callbacks.EarlyStopping(monitor='val_loss', patience=50)

# 4. model fitting
history = model.fit(x, t, validation_split=0.2, epochs=200, batch_size=100,
    verbose=0, callbacks=[checkpoint, earlyStopping])

# 5. result
result = model.evaluate(x, t, verbose=0)
print(f'\n(Loss, Accuracy)=({result[0]}, {result[1]})')

# 6. predict
data = np.array([[5.9, 0.26, 0.21, 12.5, 0.034, 36, 152, 0.9972, 3.28, 0.43, 9.5, 6]])
predict = model.predict(data)
index = np.argmax(predict)
wines = ['Red Wine', 'White Wine']
print(wines[index])



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