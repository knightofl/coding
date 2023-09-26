import numpy as np
import matplotlib.pyplot as plt


def method_least_squares(x, y):
    x_avg = np.mean(x)
    y_avg = np.mean(y)

    gradient = np.sum((x-x_avg) * (y-y_avg)) / np.sum((x-x_avg)**2)
    intercept = y_avg - x_avg*gradient

    return gradient, intercept

def mean_squares_error(weight, t_data):
    a, b = weight
    x, y = t_data
    
    return np.sum((a*x + b - y)**2) / len(x)

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


t = np.array([2,4,6,8])
s = np.array([81,93,91,97])
print(method_least_squares(t,s))

init_x = np.array([0., 0.])
f = mean_squares_error
result = gradient_descent(f, init_x=init_x, lr=0.02, step=3000, t_data=(t,s))

x = np.arange(1, 10)
a, b = method_least_squares(t, s)
y = a*x + b

plt.scatter(t, s)
plt.plot(x, y)
plt.show()



def mean_squares_error_3(weight, t_data):
    a0, a1, b = weight
    x0, x1, y = t_data

    return np.sum((a0*x0 + a1*x1 + b - y)**2) / len(x0)

p = np.array([0,4,2,3])
init_x = np.array([0.,0.,0.])
f = mean_squares_error_3
result = gradient_descent(f, init_x=init_x, lr=0.02, step=3000, t_data=(t,p,s))


# predict(inference)
x0 = 2
x1 = 2
a,b,c = result
y_predict = a*x0 + b*x1+ c
print(y_predict)


axes = plt.axes(projection='3d')
axes.scatter(t, p, s)
axes.set_xlabel('public study')
axes.set_ylabel('private class')
axes.set_zlabel('scores')
plt.show()

