import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from tensorflow import keras


'''
 0 : CRIM, 인구 1인당 범죄 수
 1 : ZN, 25,000 평방미터 이상의 주거 구역 비중
 2 : INDUS, 소매업외 상업이 차지하는 비중
 3 : CHAS, 찰스강 위치 변수(1: 강주변, 0:이외)
 4 : NOX, 일산화질소 농도
 5 : RM, 집의 평균 방 수
 6 : AGE, 1940이전에 지어진 비율
 7 : DIS, 5가지 보스턴 시 고용 시설 까지의 거리
 8 : RAD, 순환 고속도로 접근 용이성
 9 : TAX, $10,000 당 부동산 세율
10 : PTRATIO, 지역별 학생과 교사 비율
11 : B, 지역별 흑인 비율
12 : LSTAT, 급여가 낮은 직업에 종사하는 비율
13 : PRICE, 가격(단위: $1,000)
'''

df = pd.read_csv('./practice/housing.csv', header=None, delim_whitespace=True)
print(df.info)

dataset = df.values
print(dataset)
print(dataset.shape)

x = dataset[:, 0:13]
t = dataset[:, 13]

x_train, x_test, t_train, t_test = train_test_split(x, t, test_size=0.2, random_state=0)

model = keras.Sequential()
model.add(keras.layers.Dense(40, activation='relu', input_dim=x_train.shape[1]))
model.add(keras.layers.Dense(20, activation='relu'))
model.add(keras.layers.Dense(1))

model.compile(optimizer='adam', loss='mean_squared_error')
model.fit(x_train, t_train, batch_size=10, epochs=200)

y = model.predict(x_test).flatten()
for i in range(len(t_test)):
    label = t_test[i]
    predict = y[i]
    print(f'실제가격:{label:.3f}, 예상가격:{predict:.3f}')


