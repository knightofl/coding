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


x = np.array([0.6, 0.9])
t = np.array([0., 0., 1.])
params = {'W1': np.array([[-0.23471021, -0.59775279, 0.16385148],
                [1.4837155, 1.61777964, 1.59550179]]),
          'b1': np.array([0.2, 0.4, 0.3])}
          
def forward_propagation():
    W1 = params['W1']
    b1 = params['b1']
    a = np.dot(x, W1) + b1
    y = softmax(a)
    return y

def loss():
    y = forward_propagation()
    e = cross_entropy_error(y, t)
    return e

def numerical_gradient_net():
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
            fxh1 = loss()

            param[i] = tmp - h
            fxh2 = loss()

            param_gradient[i] = (fxh1 - fxh2) / (2 * h)

            param[i] = tmp
            it.iternext()

        gradient[key] = param_gradient

    return gradient


g = numerical_gradient_net()
print(g)
