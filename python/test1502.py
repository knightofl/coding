import numpy as np
import matplotlib.pyplot as plt

def stepFunction(x):
    return (x>1).astype(int)

x1 = np.array([-1.0, 1.0, -2.0, 0.5])
print(x1)

y1 = x1 > 0
print(y1, type(y1))

print(y1.astype(np.int))
print(type(y1.astype(np.int)))

y1 = stepFunction(x1)

x2 = np.arange(-5.0, 5.0, 0.1)
y2 = stepFunction(x2)
plt.plot(x2,y2)
plt.ylim(-0.1, 1.1)
plt.show()


def sigmoid(x):
    return 1 / (1 + np.exp(-x))

y2 = sigmoid(x2)

plt.plot(x2, y2)
plt.ylim(-0.1, 1.1)
plt.show()