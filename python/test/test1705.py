import numpy as np
import sys
sys.path.append('./scratch1')
from dataset.mnist import load_mnist
import pickle


(x_train, t_train), (x_test, t_test) = load_mnist(flatten=True, normalize=True, one_hot_label=True)

with open('./scratch1/ch03/sample_weight.pkl', 'rb') as f:
    network = pickle.load(f)

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def softmax(x):
    max = np.max(x)
    ex = np.exp(x - max)
    sum = np.sum(ex)
    return ex / sum

def predict(network, x):
    a1 = np.dot(x, network['W1']) + network['b1']
    z1 = sigmoid(a1)

    a2 = np.dot(z1, network['W2']) + network['b2']
    z2 = sigmoid(a2)

    a3 = np.dot(z2, network['W3']) + network['b3']
    z3 = softmax(a3)

    return z3

def cross_entropy_error(y, t):
    if y.ndim == 1:
        t = t.reshape(1, t.size)
        y = y.reshape(1, y.size)
    delta = 1e-7
    batch_size = y.shape[0]
    return -np.sum(t * np.log(y + delta)) / batch_size


print(x_train.shape)
print(t_train.shape)

train_size = x_train.shape[0]
batch_size = 10
batch_mask = np.random.choice(train_size, batch_size)
x_batch = x_train[batch_mask]
t_batch = t_train[batch_mask]

print(train_size, batch_size)
print(batch_mask)
print(x_batch, t_batch)

print(cross_entropy_error(predict(network, x_batch), t_batch))