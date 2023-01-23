import numpy as np
import matplotlib.pyplot as plt


def num_grad(f, x):
    h = 1e-4
    grad = np.zeros_like(x)
    
    for i in range(x.size):
        tmp = x[i]
        x[i] = tmp + h
        fxh1 = f(x)
        
        x[i] = tmp - h 
        fxh2 = f(x) 
        
        grad[i] = (fxh1 - fxh2) / (2*h)
        x[i] = tmp
        
    return grad


def numerical_gradient(f, x):
    if x.ndim == 1:
        return num_grad(f, x)
    else:
        grad = np.zeros_like(x)
        
        for i, x in enumerate(x):
            grad[i] = num_grad(f, x)
        
        return grad


def f(x):
    #print(x.shape, x.ndim, end=' ')
    if x.ndim == 1:
        return np.sum(x**2, axis=0)
    else:
        return np.sum(x**2, axis=1)


x0 = np.arange(-4, 4.1, 0.5)
x1 = np.arange(-4, 4.1, 0.5)
X0, X1 = np.meshgrid(x0, x1)
X0, X1 = X0.flatten(), X1.flatten()

grad = numerical_gradient(f, np.array([X0, X1]) )

plt.quiver(X0, X1, -grad[0], -grad[1],  angles="xy",color="#666666")
plt.xlim([-4, 4])
plt.ylim([-4, 4])
plt.xlabel('x0')
plt.ylabel('x1')
plt.grid()
plt.show()

