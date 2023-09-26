import numpy as np
import matplotlib.pyplot as plt


# 최소 제곱법 Method of Least Squares
def method_least_squares(x, y):
    x_avg = np.mean(x)
    y_avg = np.mean(y)

    gradient = np.sum((x-x_avg) * (y-y_avg)) / np.sum((x-x_avg)**2)
    intercept = y_avg - x_avg*gradient

    return gradient, intercept

t = np.array([2, 4, 6, 8])
s = np.array([81, 93, 91, 97])

print([i*j for i,j in zip(t, s)])
print([i*j for i in t for j in s])

x = np.arange(1, 10)
a, b = method_least_squares(t, s)
y = a*x + b

plt.scatter(t, s)
plt.plot(x, y)
plt.show()



# 평균제곱오차 Mean Square Error
def mean_square_error(x,y):
    a,b = method_least_squares(x,y)

    return np.sum((y-(a*x+b))**2) / len(x)


# 오차제곱합 Sum of Squares for Error
def sum_squares_error(x,y):
    a,b = method_least_squares(x,y)

    return np.sum((y-(a*x+b))**2) / 2


# 교차 엔트로피 오차 Cross Entropy Error
def cross_entropy_error(y,t):
    delta = 1e-7
    return -np.sum(t * np.log(y+delta))
