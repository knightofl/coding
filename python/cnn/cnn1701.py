import numpy as np
import matplotlib.pyplot as plt
from tensorflow.keras.datasets.mnist import load_data
import time
from cnn1004 import *


class TwoLayerNet:
    def __init__(self, input_size, hidden_size, output_size, weight_init_std=0.01):
        self.params = {}
        self.params['W1'] = weight_init_std * np.random.randn(input_size, hidden_size)
        self.params['b1'] = np.zeros(hidden_size)
        self.params['W2'] = weight_init_std * np.random.randn(hidden_size, output_size)
        self.params['b2'] = np.zeros(output_size)

        self.layers = {}
        self.layers['Affine1'] = AffineLayer(self.params['W1'], self.params['b1'])
        self.layers['Relu1'] = ReluLayer()
        self.layers['Affine2'] = AffineLayer(self.params['W2'], self.params['b2'])
        self.layers['SoftmaxWithLoss'] = SoftmaxWithLossLayer()

    def predict(self, x):
        out = self.layers['Affine1'].forward(x)
        out = self.layers['Relu1'].forward(out)
        out = self.layers['Affine2'].forward(out)
        return out

    def loss(self, x, t):
        y = self.predict(x)
        return self.layers['SoftmaxWithLoss'].forward(y, t)

    def accuracy(self, x, t):
        y = self.predict(x)
        y = np.argmax(y, axis=1)
        if t.ndim != 1: t = np.argmax(t, axis=1)
        accuracy = np.sum(y == t) / float(x.shape[0])
        return accuracy

    def numerical_gradient(self, x, t):
        loss_W = lambda W: self.loss(x, t)

        grads = {}
        grads['W1'] = numerical_gradient(loss_W, self.params['W1'])
        grads['b1'] = numerical_gradient(loss_W, self.params['b1'])
        grads['W2'] = numerical_gradient(loss_W, self.params['W2'])
        grads['b2'] = numerical_gradient(loss_W, self.params['b2'])
        return grads

    def gradient(self, x, t):
        self.loss(x, t)

        dout = 1
        dout = self.layers['SoftmaxWithLoss'].backward(dout)
        dout = self.layers['Affine2'].backward(dout)
        dout = self.layers['Relu1'].backward(dout)
        dout = self.layers['Affine1'].backward(dout)

        grads = {}
        grads['W1'] = self.layers['Affine1'].dW
        grads['b1'] = self.layers['Affine1'].db
        grads['W2'] = self.layers['Affine2'].dW
        grads['b2'] = self.layers['Affine2'].db
        return grads


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


network = TwoLayerNet(input_size=784, hidden_size=50, output_size=10)

step = 10000
train_size = x_train.shape[0]
batch_size = 100
lr = 0.1

train_loss_list = []
train_accuracy_list = []
test_accuracy_list = []
per_epoch = max(train_size / batch_size, 1)

start = time.time()
for i in range(step):
    batch_mask = np.random.choice(train_size, batch_size)
    x_batch = x_train[batch_mask]
    t_batch = t_train[batch_mask]

    grad = network.gradient(x_batch, t_batch)
    #grad = network.numerical_gradient(x_batch, t_batch)

    for key in network.params:
        network.params[key] -= lr * grad[key]

    loss = network.loss(x_batch, t_batch)
    train_loss_list.append(loss)

    if i % per_epoch == 0:
        end = time.time()
        print(f'elapsed time: {(end - start):.2f}, train loss: {loss:.2f}')
        start = end
        train_accuracy = network.accuracy(x_train, t_train)
        test_accuracy = network.accuracy(x_test, t_test)
        train_accuracy_list.append(train_accuracy)
        test_accuracy_list.append(test_accuracy)
        print(f'train accuracy: {train_accuracy:.2f}, test accuracy: {test_accuracy:.2f}')


x = np.arange(len(train_loss_list))
plt.plot(x, train_loss_list, label='train loss')
plt.xlabel('step')
plt.ylabel('loss')
plt.ylim(0, 3.0)
plt.legend(loc='center right')
plt.show()

x = np.arange(len(train_accuracy_list))
plt.plot(x, train_accuracy_list, label='train accuracy')
plt.plot(x, test_accuracy_list, label='test accuracy', linestyle='--')
plt.xlabel('epoch')
plt.ylabel('accuracy')
plt.ylim(0, 1.0)
plt.legend(loc='center right')
plt.show()

