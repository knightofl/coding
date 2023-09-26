import numpy as np
import matplotlib.pyplot as plt

def num_diff(f, x):
    h = 1e-4
    return (f(x+h) - f(x-h)) / (2*h)

def fun(x):
    return 1 / (1 + np.exp(-x))

def tangent(f, x):
    d = num_diff(f, x)
    print(d)
    y = f(x) - d*x
    print(y)
    return lambda t: d*t + y

x = np.arange(-4.0, 4.0, 0.1)
y = fun(x)

tf = tangent(fun, 0)
y2 = tf(x)

plt.plot(x, y)
plt.plot(x, y2)
plt.ylim(0, 1)
plt.show()