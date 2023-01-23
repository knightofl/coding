import numpy as np
import matplotlib.pyplot as plt

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def diff_sig(x):
    return sigmoid(x) * (1 - sigmoid(x))

x = np.arange(-4.0, 4.0, 0.2)
print(diff_sig(0))

plt.plot(x, sigmoid(x), linestyle='--', label='sigmoid')
plt.plot(x, diff_sig(x), label='diff_sig')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()