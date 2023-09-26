import numpy as np
import matplotlib.pyplot as plt

def num_grad(f, x, y):
    h = 1e-4
    grad_x = (f(x+h, 0) - f(x-h, 0)) / (2*h)
    grad_y = (f(0, y+h) - f(0, y-h)) / (2*h)
    return np.array([grad_x, grad_y])

def fun(x, y):
    return x**2 + y**2

x = np.arange(-4.0, 4.1, 0.5)
y = np.arange(-4.0, 4.1, 0.5)
print(x, y)
print(num_grad(fun, x, y))
X, Y = np.meshgrid(x, y)

X = X.flatten()
Y = Y.flatten()

grad = num_grad(fun, X, Y)

plt.figure()
plt.quiver(X, Y, -grad[0], -grad[1], angles="xy", color="#666666") 
plt.xlim([-4, 4])
plt.ylim([-4, 4])
plt.xlabel('x')
plt.ylabel('y')
plt.grid()
plt.draw()
plt.show()
