import numpy as np
from tensorflow.keras.datasets.mnist import load_data


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


params = dict()

x = np.array([[0.6, 0.9, 0.11], [0.6, 0.9, 0.11], [0.6, 0.9, 0.11]])
t = np.array([[0., 0., 1.], [0., 1., 0.], [0.6, 0.9, 0.11]])    

initialize(input_size=3, hidden_size=3, output_size=3)
gradient = numerical_gradient_net(x, t)
print(gradient)


