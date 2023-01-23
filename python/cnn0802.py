import numpy as np
import matplotlib.pyplot as plt


def stepFun(x):
    #return np.array(x>0, dtype=np.int)
    return (x>0).astype(np.int)

a = np.arange(-1, 1.1, 0.4)
print(a, stepFun(a))


def stepFunc(x):
    return np.array(x>0, dtype=np.int)

x = np.arange(-5.0, 5.1, 0.1)
y = stepFunc(x)

fig, sbplts = plt.subplots()
sbplts.plot(x, y)
plt.ylim(-0.1, 1.1)
plt.show()


def sigmoid(x):
    return 1 / (1 + np.exp(-x))

x = np.arange(-5, 5, 0.1)
print(x)
y = sigmoid(x)
plt.plot(x, y)
plt.ylim(-0.1, 1.1)
plt.show()


def relu(x):
    return np.maximum(0, x)

x = np.arange(-5, 5, 0.1)
y = relu(x)
plt.plot(x, y)
plt.show()


def identityFunc(x):
    return x


def softmax(x):
    c = np.max(x)
    return np.exp(x-c) / np.sum(np.exp(x-c))

a = np.array([980, 990, 1010, 1000])
print(softmax(a))
