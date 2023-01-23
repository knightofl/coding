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
        
def grad_desc(f, init_x, lr=0.01, step=100):
    x = init_x
    x_history = []

    for i in range(step):
        x_history.append(x.copy())
        grad = num_grad(f, x)
        x -= lr * grad

    return x, np.array(x_history)

def fun(x):
    return x[0]**2 + x[1]**2

init_x = np.array([-2.0, 2.0])    
lr = 0.1
step = 20
x, x_history = grad_desc(fun, init_x, lr=lr, step=step)

print(x_history[0, :])
plt.plot([-2, 2], [0, 0], '--b')
plt.plot([0, 0], [-2, 2], '--b')
plt.plot(x_history[:, 0], x_history[:, 1], 'o')

plt.xlim(-2.0, 2.0)
plt.ylim(-2.0, 2.0)
plt.xlabel("x0")
plt.ylabel("x1")
plt.show()