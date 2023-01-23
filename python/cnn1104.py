import numpy as np


def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def softmax(x):
    c = np.max(x, axis=0)
    return np.exp(x - c) / np.sum(np.exp(x - c))

def init_network():
    params = {'W1': np.array([[0.1, 0.2, 0.5], [0.3, 0.4, 1.]]),
               'b1': np.array([0.1, 0.2, 0.3]),
               'W2': np.array([[0.1, 0.2], [0.3, 0.4], [0.2, 0.3]]),
               'b2': np.array([0.1, 0.2]),
               'W3': np.array([[0.1, 0.2], [0.2, 0.3]]),
               'b3': np.array([0.2, 0.1])}
    return params

def forward_propagation(network, x):
    W1, W2, W3 = network['W1'], network['W2'], network['W3']
    b1, b2, b3 = network['b1'], network['b2'], network['b3']

    a1 = np.dot(x, W1) + b1
    z1 = sigmoid(a1)
    a2 = np.dot(z1, W2) + b2
    z2 = sigmoid(a2)
    a3 = np.dot(z2, W3) + b3
    y = softmax(a3)

    return y


x = np.array([1., 5.])
network = init_network()
y = forward_propagation(network, x)
print(y)

