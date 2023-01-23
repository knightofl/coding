import numpy as np


def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def softmax(x):
    c = np.max(x, axis=0)
    return np.exp(x - c) / np.sum(np.exp(x - c))


x = np.array([1., 5.])
print(x, x.shape, x.ndim)

W1 = np.array([[0.1, 0.2, 0.5], [0.3, 0.4, 1.]])
print(W1, W1.shape, W1.ndim)

b1 = np.array([0.1, 0.2, 0.3])
print(b1, b1.shape, b1.ndim)

a1 = np.dot(x, W1) + b1
print(a1, a1.shape, a1.ndim)

z1 = sigmoid(a1)
print(z1, z1.shape, z1.ndim)


W2 = np.array([[0.1, 0.2], [0.3, 0.4], [0.2, 0.3]])
print(W2, W2.shape, W2.ndim)

b2 = np.array([0.1, 0.2])
print(b2, b2.shape, b2.ndim)

a2 = np.dot(z1, W2) + b2
print(a2, a2.shape, a2.ndim)

z2 = sigmoid(a2)
print(z2, z2.shape, z2.ndim)


W3 = np.array([[0.1, 0.2], [0.2, 0.3]])
print(W3, W3.shape, W3.ndim)

b3 = np.array([0.2, 0.1])
print(b3, b3.shape, b3.ndim)

a3 = np.dot(z2, W3) + b3
print(a3, a3.shape, a3.ndim)


y = softmax(a3)
print(y, y.shape, y.ndim)

