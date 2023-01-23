import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import StratifiedKFold
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
print(t, t.shape)



nfold = 10
skf =  StratifiedKFold(n_splits=nfold, shuffle=True, random_state=0)
accuracy_list = []

for train_mask, test_mask in skf.split(x, t):
    model = keras.Sequential()
    model.add(keras.layers.Dense(40, activation='relu', input_dim=x.shape[1]))
    model.add(keras.layers.Dense(20, activation='relu'))
    model.add(keras.layers.Dense(2, activation='sigmoid'))

    model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
    model.fit(x[train_mask], keras.utils.to_categorical(t[train_mask]), batch_size=5, epochs=70)
    
    result = model.evaluate(x[test_mask], keras.utils.to_categorical(t[test_mask]))
    accuracy_list.append(result[1])

print(f'\n{nfold} fold accuracies:{accuracy_list}')

