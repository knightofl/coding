import numpy as np
from tensorflow.keras.datasets.mnist import load_data


def numerical_gradient(f, x, y):
    h = 1e-4
    grad_x = (f(x+h, 0) - f(x-h, 0)) / (2*h)
    grad_y = (f(0, y+h) - f(0, y-h)) / (2*h)

    return np.array([grad_x, grad_y])

def cross_entropy_error(y, t):
    if y.ndim == 1:
        y = y.reshape(1, y.size)
        t = t.reshape(1, t.size)

    delta = 1e-7
    batch_size = y.shape[0]
    return -np.sum(t * np.log(y+delta)) / batch_size


# mnist data load
(x_train, t_train), (x_test, t_test) = load_data()
print(x_train.shape, x_train.dtype, t_train.shape, t_train.dtype)
print(x_test.shape, x_train.dtype, t_test.shape, t_test.dtype)

# flatten, normalize
x_train = x_train.reshape(-1, 28*28) / 255.0
x_test = x_test.reshape(-1, 28*28) / 255.0
print(x_train.shape, x_test.shape)

# one hot label encoding
element = len(set(t_train))
t_train = np.eye(element)[t_train]
t_test = np.eye(element)[t_test]
print(t_train.shape, t_test.shape)


img = x_train[0].reshape(28, 28)
print(img.shape)

import matplotlib.pyplot as plt
plt.imshow(img)
plt.show()

from PIL import Image
def imgShow(img):
    pilImg = Image.fromarray(np.uint8(img))
    pilImg.show()

imgShow(img)


train_size = x_test.shape[0]
batch_size = 100
batch_mask = np.random.choice(train_size, batch_size)
x_batch = x_train[batch_mask]
t_batch = t_train[batch_mask]

print(x_batch)
print(t_batch)

