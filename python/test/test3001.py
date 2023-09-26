import numpy as np
import matplotlib.pyplot as plt


a = 1/2
b = 2

x = np.arange(-4, 4, 0.1)

plt.plot(x, a ** x)
plt.plot(x, b ** x)
plt.show()


print(np.log(np.e))
x = np.arange(0, 4, 0.1)
plt.plot(x, np.log(x))
plt.show()