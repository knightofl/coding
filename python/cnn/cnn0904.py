import numpy as np
import matplotlib.pyplot as plt


def numerical_gradient(f, weight, t_data):
    h = 1e-4
    gradient = np.zeros_like(weight)

    for i in range(weight.size):
        tmp = weight[i]

        weight[i] = tmp + h
        fxh1 = f(weight, t_data)

        weight[i] = tmp - h
        fxh2 = f(weight, t_data)

        gradient[i] = (fxh1 - fxh2) / (2 * h)
        weight[i] = tmp

    return gradient

def gradient_descent(f, init_x, lr=0.01, step=100, t_data=None):
    for i in range(step):
        x = init_x
        gradient = numerical_gradient(f, x, t_data)
        print(f'step={i+1}, gradient={gradient}, weight={x}')
        x -= lr * gradient

    return x

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def loss(weight, t_data):
    a,b = weight
    x,y = t_data

    return -np.mean(y * np.log(sigmoid(a*x + b)) + (1-y) * np.log(1 - sigmoid(a*x + b)))


t = np.array([2,4,6,8,10,12,14])
s = np.array([0,0,0,1,1,1,1])
init_x = np.array([0.,0.])
f = loss

result = gradient_descent(f, init_x=init_x, lr=0.5, step=20000, t_data=(t,s))


a, b = result
x = np.arange(1, 15, 0.1)
y = sigmoid(a*x + b)
plt.scatter(t,s)
plt.plot(x, y)
plt.show()


x = 7
y_predict = sigmoid(a*x + b)
print(y_predict)



def ananlytic_gradient(weight, t_data):
    a,b = weight
    x,y = t_data

    dx = np.array([0.,0.])
    dx[0] = x * (sigmoid(a*x + b) - y)
    dx[1] = sigmoid(a*x + b) - y

    return dx

lr = 0.1
step = 5000
weight = init_x
for i in range(step):
    for t_data in zip(t,s):
        dx = ananlytic_gradient(weight, t_data)
        weight -= lr * dx
    print(f'step={i+1}, gradient={dx}, weight={weight}')


a, b = weight
x = np.arange(1, 15, 0.1)
y = sigmoid(a*x + b)
plt.scatter(t,s)
plt.plot(x, y)
plt.show()