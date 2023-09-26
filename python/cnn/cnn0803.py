import numpy as np
import matplotlib.pyplot as plt
from sympy import Derivative, symbols


def num_diff(f, x):
    h = 1e-4
    return (f(x+h) - f(x-h)) / (2*h)

def tangentLine(f, x):
    d = num_diff(f, x)
    print(d)
    y = f(x) - d*x
    print(y)

    return lambda t: d*t + y


x = symbols('x')

f = 20*(x-2)**2 + 500
fprime = Derivative(f, x).doit()
print(fprime)
print(fprime.subs({x: 3}))
print(fprime.subs(x, 3))


def g(x):
    return 20*(x-2)**2 + 500

print(num_diff(g, 3))


x = np.arange(-2, 6, 0.1)
y1 = g(x)
y2 = tangentLine(g, 3)(x)

plt.plot(x, y1)
plt.plot(x, y2)
plt.show()
