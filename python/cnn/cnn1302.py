import numpy as np
import matplotlib.pyplot as plt
import pickle
from tensorflow.keras.datasets.mnist import load_data


def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def softmax(x):
    c = np.max(x, axis=0)
    return np.exp(x - c) / np.sum(np.exp(x - c))


(x_train, t_train), (x_test, t_test) = load_data()
x_train = x_train.reshape(-1, 28*28) / 255.0
x_test = x_test.reshape(-1, 28*28) / 255.0
#t_train = np.eye(10)[t_train]
#t_test = np.eye(10)[t_test]


def init_network():
    with open("./scratch1/ch03/sample_weight.pkl", 'rb') as f:
        network = pickle.load(f)
    return network

def predict(network, x):
    W1, W2, W3 = network['W1'], network['W2'], network['W3']
    b1, b2, b3 = network['b1'], network['b2'], network['b3']

    a1 = np.dot(x, W1) + b1
    z1 = sigmoid(a1)
    a2 = np.dot(z1, W2) + b2
    z2 = sigmoid(a2)
    a3 = np.dot(z2, W3) + b3
    y = softmax(a3)

    return np.argmax(y)


network = init_network()
print(t_test[0])
print(predict(network, x_test[0]))

count = 0
for i in range(x_test.shape[0]):
    if t_test[i] == predict(network, x_test[i]):
        count += 1

print(count / x_test.shape[0])

