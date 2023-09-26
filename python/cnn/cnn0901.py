import numpy as np


# 수치미분
def numerical_differentiation(f, x):
    h = 1e-4
    return (f(x+h) - f(x-h)) / (2*h)


# 경사하강법
def num_grad(f, x):
    h = 1e-4
    gradient = np.zeros_like(x)

    for i in range(x.size):
        tmp = x[i]
        x[i] = tmp + h
        fxh1 = f(x)
        x[i] = tmp - h
        fxh2 = f(x)
        gradient[i] = (fxh1 - fxh2) / (2 * h)
        x[i] = tmp
    
    return gradient


def numerical_gradient(f, x):
    if x.ndim == 1:
        return num_grad(f, x)
    else:
        gradient = np.zeros_like(x)
        
        for i, x in enumerate(x):
            gradient[i] = num_grad(f, x)
        
        return gradient


# 경사하강
def gradient_descent(f, init_x, lr=0.01, step=100):
    x = init_x
    x_history = []

    for i in range(step):
        x_history.append(x.copy())
        gradient = numerical_gradient(f, x)
        print(f'step={i+1}, gradient={gradient}, x={x}')
        x -= lr * gradient

    return x, np.array(x_history)


# 최소제곱법 Method of Least Squares
def method_least_squares(x, y):
    x_avg = np.mean(x)
    y_avg = np.mean(y)

    gradient = np.sum((x-x_avg) * (y-y_avg)) / np.sum((x-x_avg)**2)
    intercept = y_avg - x_avg*gradient

    return gradient, intercept


# 평균제곱오차 Mean Square Error
def mean_squares_error(x, y):
    a,b = method_least_squares(x, y)

    return np.sum((y-(a*x+b))**2) / len(x)


# 오차제곱합 Sum of Squares for Error
def sum_squares_error(x, y):
    a,b = mean_squares_error(x, y)

    return np.sum((y-(a*x+b))**2) / 2


# 교차 엔트로피 오차 Cross Entropy Error
def cross_entropy_error(y, t):
    if y.ndim == 1:
        y = y.reshape(1, y.size)
        t = t.reshape(1, t.size)

    delta = 1e-7
    batch_size = y.shape[0]
    return -np.sum(t * np.log(y+delta)) / batch_size


#########################################################
# 수치편미분(x변수가 여러 개 일때..)
def numerical_gradient_2(f, x, t_data=None):
    h = 1e-4
    gradient = np.zeros_like(x)

    for i in range(x.size):
        tmp = x[i]

        x[i] = tmp + h
        fxh1 = f(x, t_data) if t_data else f(x)

        x[i] = tmp - h
        fxh2 = f(x, t_data) if t_data else f(x)

        gradient[i] = (fxh1 - fxh2) / (2 * h)
        x[i] = tmp

    return gradient


# 경사하강법
def gradient_descent_2(f, init_x, lr=0.01, step=100, t_data=None):
    for i in range(step):
        x = init_x
        gradient = numerical_gradient_2(f, x, t_data)
        print(f'step={i+1}, gradient={gradient}, weight={x}')
        x -= lr * gradient

    return x


# 평균제곱오차(MSE, Mean Squares Error)
def mean_squares_error_2(weight, t_data):
    a, b = weight
    x, y = t_data
    
    return np.sum((a*x + b - y)**2) / len(x)


def mean_squares_error_3(weight, t_data):
    a0, a1, b = weight
    x0, x1, y = t_data

    return np.sum((a0*x0 + a1*x1 + b - y)**2) / len(x0)



if __name__ == '__main__':
    pass
