import numpy as np


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


def loss(w, x, t):
    a = np.dot(x, w)
    y = softmax(a)
    e = cross_entropy_error(y, t)
    return e

def numerical_gradient(f, w, x, t):
    h = 1e-4
    gradient = np.zeros_like(w)

    it = np.nditer(w, flags=['multi_index'], op_flags=['readwrite'])
    while not it.finished:
        i = it.multi_index
        tmp = w[i]

        w[i] = tmp + h
        fxh1 = f(w, x, t)
        
        w[i] = tmp - h
        fxh2 = f(w, x, t)

        gradient[i] = (fxh1 - fxh2) / (2 * h)
        w[i] = tmp
        it.iternext()

    return gradient


x = np.array([0.6, 0.9])
t = np.array([0., 0., 1.])
w = np.array([[-0.23471021, -0.59775279, 0.16385148],
    [1.4837155, 1.61777964, 1.59550179]])

g = numerical_gradient(loss, w, x, t)
print(g)

