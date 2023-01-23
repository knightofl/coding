import numpy as np
import matplotlib.pyplot as plt

def num_diff_1(f, x):
    h = 1e-50
    return (f(x+h) - f(x)) / h

def fun_1(x):
    return x**2

print(num_diff_1(fun_1, 1))


def num_diff(f, x):
    h = 1e-7
    return (f(x+h) - f(x)) / h

print(num_diff(fun_1, 1))

def fun_2(x):
    return 0.01*x**2 + 0.1*x

print(num_diff(fun_2, 5))
print(num_diff(fun_2, 10))

x = np.arange(0.0, 20.0, 0.01)
y = fun_2(x)
plt.plot(x, y)
plt.show()
