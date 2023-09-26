import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from tensorflow import keras
import time

import sys, os
from pathlib import Path
try:
    sys.path.append(os.path.join(Path(os.getcwd()), 'common'))
    from multi_layer_net import MultiLayerNet
except ImportError:
    print('common library error')


df = pd.read_csv('./practice/housing.csv', header=None, delim_whitespace=True)
dataset = df.values

x = dataset[:, 0:13]
t = dataset[:, 13]

x_train, x_test, t_train, t_test = train_test_split(x, t, test_size=0.2, random_state=0)

t_train = t_train[:, np.newaxis]
t_test = t_test[:, np.newaxis]

batch_size = 10
epochs = 200
learning_rate = 0.01

network = MultiLayerNet(input_size=x_train.shape[1], hidden_size_list=[30, 10],
    output_size=t_train.shape[1])

train_size = x_train.shape[0]
epoch_size = int(train_size / batch_size)
iterations = epochs * epoch_size

elapsed = 0
epoch_idx = 0

for idx in range(1, iterations+1):
    # 4-1. fetch mini-batch
    batch_mask = np.random.choice(train_size, batch_size)
    x_batch = x_train[batch_mask]  # 100 x 784
    t_batch = t_train[batch_mask]  # 100 x 10

    print(x_batch.shape, t_batch.shape)

    # 4-2. gradient
    stime = time.time()  # stopwatch: start
    gradient = network.gradient(x_batch, t_batch)
    elapsed += (time.time() - stime)  # stopwatch: end

    # 4-3. update parameter
    for key in network.params:
        network.params[key] -= learning_rate * gradient[key]

    # 4-4. train loss
    loss = network.loss(x_batch, t_batch)

    # 4-5 accuracy per epoch
    if idx % epoch_size == 0:
        epoch_idx += 1

        print(f'\nEpoch {epoch_idx:02d}/{epochs:02d} ')
        print(f'{int(idx/epoch_idx)}/{epoch_size} - {elapsed*1000:.3f}ms - loss:{loss:.3f}')

        elapsed = 0

