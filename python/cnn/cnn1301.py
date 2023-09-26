import numpy as np
import matplotlib.pyplot as plt
import pickle
from tensorflow.keras.datasets.mnist import load_data


def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def softmax(x):
    c = np.max(x, axis=0)
    return np.exp(x - c) / np.sum(np.exp(x - c))


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


def init_network():
    with open("./scratch1/ch03/sample_weight.pkl", 'rb') as f:
        network = pickle.load(f)
    return network


x_test_len = x_test.shape[0]
print(x_test_len)
random_index = np.random.choice(x_test_len)
print(random_index)

x = x_test[random_index]
print(x.shape)
t = t_test[random_index]
print(t.shape)


network = init_network()

print(network['W1'].shape)
print(network['b1'].shape)
a1 = np.dot(x, network['W1']) + network['b1']
print(a1.shape)
z1 = sigmoid(a1)
print(z1.shape)

print(network['W2'].shape)
print(network['b2'].shape)
a2 = np.dot(z1, network['W2']) + network['b2']
print(a2.shape)
z2 = sigmoid(a2)
print(z2.shape)

print(network['W3'].shape)
print(network['b3'].shape)
a3 = np.dot(z2, network['W3']) + network['b3']
print(a3.shape)
y = softmax(a3)
print(y, y.shape)
print(np.argmax(y), np.argmax(t))


def predict(network, x):
    W1, W2, W3 = network['W1'], network['W2'], network['W3']
    b1, b2, b3 = network['b1'], network['b2'], network['b3']

    a1 = np.dot(x, W1) + b1
    z1 = sigmoid(a1)
    a2 = np.dot(z1, W2) + b2
    z2 = sigmoid(a2)
    a3 = np.dot(z2, W3) + b3
    y = softmax(a3)

    return y

y = predict(network, x)
print(y, y.shape)
print(np.argmax(y), np.argmax(t))


plt.imshow(x_test[random_index].reshape(28, 28))
plt.show()


