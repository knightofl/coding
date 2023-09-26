import numpy as np
from tensorflow.keras.datasets.mnist import load_data
import time
import pickle


def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def softmax(x):
    if x.ndim == 2:
        x = x.T
        x -= np.max(x, axis=0)
        y = np.exp(x) / np.sum(np.exp(x), axis=0)

        return y.T
    
    x -= np.max(x)
    return np.exp(x) / np.sum(np.exp(x))

def cross_entropy_error(y, t):
    if y.ndim == 1:
        y = y.reshape(1, y.size)
        t = t.reshape(1, t.size)

    if y.size == t.size:
        t = t.argmax(axis=1)

    delta = 1e-7
    batch_size = y.shape[0]
    return -np.sum(np.log(y[np.arange(batch_size), t] + delta)) / batch_size

(x_train, t_train), (x_test, t_test) = load_data()
x_train = x_train.reshape(-1, 28*28) / 255.0
x_test = x_test.reshape(-1, 28*28) / 255.0
t_train = np.eye(10)[t_train]
t_test = np.eye(10)[t_test]


def initialize(input_size, hidden_size, output_size, weight_init=0.01):
    params['W1'] = weight_init * np.random.randn(input_size, hidden_size)
    params['b1'] = np.zeros(hidden_size)
    params['W2'] = weight_init * np.random.randn(hidden_size, output_size)
    params['b2'] = np.zeros(output_size)

def forward_propagation(x):
    W1, b1 = params['W1'], params['b1']
    W2, b2 = params['W2'], params['b2']

    a1 = np.dot(x, W1) + b1
    z1 = sigmoid(a1)
    a2 = np.dot(z1, W2) + b2
    y = softmax(a2)

    return y

def loss(x, t):
    y = forward_propagation(x)
    e = cross_entropy_error(y, t)
    return e

def numerical_gradient_net(x, t):
    h = 1e-4
    gradient = dict()

    for key in params:
        param = params[key]
        param_gradient = np.zeros_like(param)

        it = np.nditer(param, flags=['multi_index'], op_flags=['readwrite'])
        while not it.finished:
            i = it.multi_index
            tmp = param[i]
            param[i] = tmp + h
            fxh1 = loss(x, t)
            param[i] = tmp - h
            fxh2 = loss(x, t)
            param_gradient[i] = (fxh1 - fxh2) / (2 * h)
            param[i] = tmp
            it.iternext()
        gradient[key] = param_gradient
    return gradient


x = x_train
t = t_train

step = 10
batch_size = 100
lr = 0.1
params = dict()
loss_list = []

initialize(input_size=x.shape[1], hidden_size=50, output_size=t.shape[1])
print(params['W1'].shape, params['b1'].shape)
print(params['W2'].shape, params['b2'].shape)


for i in range(step):
    start = time.time()
    batch_mask = np.random.choice(x.shape[0], batch_size)
    x_batch = x[batch_mask]
    t_batch = t[batch_mask]

    gradient = numerical_gradient_net(x_batch, t_batch)
    end = time.time()
    
    for key in params:
        params[key] -= lr * gradient[key]

    l = loss(x_batch, t_batch)
    loss_list.append(l)
    print(f'{i} {(end - start):.2f} : {l:.2f}')

print(params)
print(loss_list)


with open('weight1501.pkl', 'wb') as f:
    pickle.dump(params, f)


test_size = x_test.shape[0]
'''
accuracy = 0
for i in range(test_size):
    if np.argmax(forward_propagation(x_test[i])) == np.argmax(t_test[i]):
        accuracy += 1
'''

predict = np.argmax(forward_propagation(x_test), axis=1)
true = np.argmax(t_test, axis=1)
accuracy = np.sum(predict == true)

print(f'Accuracy: {(float(accuracy) / test_size):.2f}')

