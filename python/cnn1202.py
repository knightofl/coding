import numpy as np
import matplotlib.pyplot as plt
from collections import OrderedDict
from tensorflow.keras.datasets.mnist import load_data

import sys, os
from pathlib import Path
try:
    sys.path.append(os.path.join(Path(os.getcwd()), 'common'))
    from multi_layer_net import MultiLayerNet
    from util import smooth_curve
    from optimizer import *
except ImportError:
    print('common library error')


# mnist data load
(x_train, t_train), (x_test, t_test) = load_data()
print(x_train.shape, x_train.dtype, t_train.shape, t_train.dtype)
print(x_test.shape, x_train.dtype, t_test.shape, t_test.dtype)

# flatten, normalize
x_train = x_train.reshape(-1, 28*28) / 255.0
x_test = x_test.reshape(-1, 28*28) / 255.0
print(x_train.shape, x_test.shape)

# one hot label encoding
element = len(set(t_train))
t_train = np.eye(element)[t_train]
t_test = np.eye(element)[t_test]
print(t_train.shape, t_test.shape)


train_size = x_train.shape[0]
batch_size = 128
max_iterations = 2000


# 1. 실험용 설정==========
optimizers = {}
optimizers['SGD'] = SGD()
optimizers['Momentum'] = Momentum()
optimizers['AdaGrad'] = AdaGrad()
optimizers['Adam'] = Adam()
#optimizers['RMSprop'] = RMSprop()

networks = {}
train_loss = {}
for key in optimizers.keys():
    networks[key] = MultiLayerNet(
        input_size=784, hidden_size_list=[100, 100, 100, 100],
        output_size=10)
    train_loss[key] = []    


# 2. 훈련 시작==========
for i in range(max_iterations):
    batch_mask = np.random.choice(train_size, batch_size)
    x_batch = x_train[batch_mask]
    t_batch = t_train[batch_mask]
    
    for key in optimizers.keys():
        grads = networks[key].gradient(x_batch, t_batch)
        optimizers[key].update(networks[key].params, grads)
    
        loss = networks[key].loss(x_batch, t_batch)
        train_loss[key].append(loss)
    
    if i % 100 == 0:
        print( "===========" + "iteration:" + str(i) + "===========")
        for key in optimizers.keys():
            loss = networks[key].loss(x_batch, t_batch)
            print(key + ":" + str(loss))


# 3. 그래프 그리기==========
markers = {"SGD": "o", "Momentum": "x", "AdaGrad": "s", "Adam": "D"}
x = np.arange(max_iterations)
for key in optimizers.keys():
    plt.plot(x, smooth_curve(train_loss[key]), marker=markers[key], markevery=100, label=key)
plt.xlabel("iterations")
plt.ylabel("loss")
plt.ylim(0, 1)
plt.legend()
plt.show()
