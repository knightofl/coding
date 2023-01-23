import numpy as np
import matplotlib.pylab as plt


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


def gradient_descent(f, init_x, lr=0.01, step_num=100):
    x = init_x
    x_history = []

    for i in range(step_num):
        x_history.append(x.copy())

        grad = numerical_gradient(f, x)
        x -= lr * grad

    return x, np.array(x_history)


def f(x):
    return x[0]**2 + x[1]**2

init_x = np.array([-3.0, 4.0])

lr = 0.1
step_num = 50
x, x_history = gradient_descent(f, init_x, lr=lr, step_num=step_num)

plt.plot([-5,5], [0,0], '--b')
plt.plot([0,0], [-5,5], '--b')
plt.plot(x_history[:,0], x_history[:,1], 'o')

plt.xlim(-3.5, 3.5)
plt.ylim(-4.5, 4.5)
plt.xlabel("x0")
plt.ylabel("x1")
plt.show()

