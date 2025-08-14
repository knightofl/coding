# seaborn 데이타셋 수정
from numpy.core.fromnumeric import transpose
from sklearn import preprocessing
import seaborn as sns

tips = sns.load_dataset('tips', data_home='practice')
print(type(tips))
print(tips.head(5))
print(tips['day'].unique())

# LabelEncoder
from sklearn.preprocessing import LabelEncoder

encoder = LabelEncoder()
items = tips['day']
encoder.fit(items)
labels = encoder.transform(items)

print('Label Encoding Result:\n', labels)

classes = encoder.classes_
print('Label Encoding Classes:', classes)

inverse_result = encoder.inverse_transform([2])
print('Label Decoding Result:', inverse_result)


# 원핫 인코딩
from sklearn.preprocessing import OneHotEncoder

print(labels.shape, labels)
labels_o = labels.reshape(-1, 1)

one_hot_encoder = OneHotEncoder()
one_hot_encoder.fit(labels_o)
one_hot_labels = one_hot_encoder.transform(labels_o)

print('One Hot Encoding Labels:\n', one_hot_labels.toarray())

one_hot_classes = one_hot_encoder.categories_
print('One Hot Encoding Classes:', one_hot_classes)


# 스케일링
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import MinMaxScaler

df_bike = pd.read_csv('bike_demand_kaggle.csv')
print(df_bike.head(5))

df_bike_num = df_bike.iloc[:, 5:9]
print(df_bike_num.head(5))

print('Average:\n', np.round_(df_bike_num.mean(), 3))
print('Variance:\n', np.round_(df_bike_num.var(), 3))

scaler = StandardScaler()
scaler.fit(df_bike_num)
result = scaler.transform(df_bike_num)

scaled_bike = pd.DataFrame(data=result, columns=df_bike_num.columns)

print('--------- StandardScaler ---------')
print('Average')
print(np.round_(scaled_bike.mean(),3))
print('Variance')
print(np.round_(scaled_bike.var(),3)) 

plt.figure(figsize=(10, 6))
scaled_bike.boxplot(labels=['temp', 'atemp', 'humidity', 'windspeed'])
plt.show()

df_bike_num = df_bike.iloc[:, 5:9]
print(df_bike_num.head(5))

scaler = MinMaxScaler()
scaler.fit(df_bike_num)
result = scaler.transform(df_bike_num)
scaled_bike = pd.DataFrame(data=result, columns=df_bike_num.columns)

print('--------- MinMaxScler ---------')
print('Average')
print(np.round_(scaled_bike.mean(),3))
print('Variance')
print(np.round_(scaled_bike.var(),3))

plt.figure(figsize=(10, 6))
scaled_bike.boxplot(labels=['temp', 'atemp', 'humidity', 'windspeed'])
plt.show()
