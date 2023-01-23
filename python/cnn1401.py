import numpy as np
from cnn1004 import *


x = np.random.randn(2, 3)
print(x)

x = x.reshape(x.shape[0], -1)
print(x)

x = np.random.randn(3)
print(x)

x = x.reshape(x.shape[0], -1)
print(x)


x = np.array([2, 3])
w = np.random.randn(2, 3)
b = np.array([5, 6, 7])
print(np.dot(x, w) + b)

a = AffineLayer(w, b)
a1 = a.forward(x)


it = np.nditer(x, flags=['multi_index'], op_flags=['readwrite'])

'''
for i in it:
    print(i)
'''

while not it.finished:
    i = it.multi_index
    print(i, x[i])
    it.iternext()



from pathlib import Path
import sys, os
print(os.getcwd())
print(Path(os.getcwd()))
print(Path(os.getcwd()).parent, 'common')

try:
    sys.path.append(os.path.join(Path(os.getcwd()).parent, 'common'))
    import layers
except ImportError:
    print('Library Module Can Not Found')


import datetime
now = datetime.datetime.now()

dstr = f'{now:%Y-%m-%d-%H%M%S}'
print(dstr)



import tensorflow as tf
print(tf.__version__)
print(tf.test.is_built_with_cuda())
print(tf.test.is_built_with_gpu_support())
print(tf.test.gpu_device_name())


from tensorflow.python.client import device_lib
device_lib.list_local_devices()

