import math
import matplotlib.pyplot as plt
import numpy as np

print(math.e)

x = np.arange(-10, 10, 0.1)
y = 1 / (1 + math.e ** (-x))

plt.figure(figsize=(10, 5))
plt.plot(x,y)
plt.show()