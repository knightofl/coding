import numpy as np
import matplotlib.pyplot as plt


def identity(x):
    return x

def step(x):
    return np.array(x>0, dtype=np.int)

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def relu(x):
    return np.maximum(x, 0)

def softmax(x):
    c = np.max(x, axis=0)
    return np.exp(x - c) / np.sum(np.exp(x - c))


x = np.arange(-4, 4, 0.01)

y = identity(x)
plt.plot(x,y)
plt.show()

y = step(x)
plt.plot(x, y)
plt.show()


y = sigmoid(x)
plt.plot(x, y)
plt.show()


y = relu(x)
plt.plot(x, y)
plt.show()


y = softmax(x)
print(np.sum(y))
plt.plot(x, y)
plt.show()

