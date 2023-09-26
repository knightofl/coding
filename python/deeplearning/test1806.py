import numpy as np
import matplotlib.pyplot as plt

x_old = 0
x_new = 6 
eps = 0.01 
precision = 0.00001

def f_prime(x):
    return 4 * x**3 - 9 * x**2

while abs(x_new - x_old) > precision:
    x_old = x_new
    x_new = x_old - eps * f_prime(x_old)

print(f'Local minimum occurs at: {x_new}')

x = np.arange(-20, 20, 0.01)
y = f_prime(x)
plt.plot(x,y)
plt.show()