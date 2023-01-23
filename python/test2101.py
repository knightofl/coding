import tensorflow as tf

print(tf.__version__)
print(tf.test.is_gpu_available())

tf.config.list_physical_devices('GPU')


import numpy as np
import matplotlib.pyplot as plt

x = np.arange(-3, 3, 0.2)
plt.plot(x, np.tanh(x))
plt.show()