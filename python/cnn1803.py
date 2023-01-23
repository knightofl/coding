import numpy as np
import matplotlib.pyplot as plt
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


dataset = np.loadtxt('./practice/pimaindians-diabetes.csv', delimiter=',')
print(dataset.shape)

x_train = dataset[:, 0:8]
t_train = dataset[:, 8]
print(x_train, x_train.shape)
print(t_train, t_train.shape)

t_train = np.eye(2)[t_train.astype(int)]
print(t_train, t_train.shape)
print(x_train.shape[1], t_train.shape[1])

network = TwoLayerNet(input_size=x_train.shape[1], hidden_size=30, output_size=t_train.shape[1])

step = 1000
train_size = x_train.shape[0]
batch_size = 10
lr = 0.1

train_loss_list = []
train_accuracy_list = []
per_epoch = int(max(train_size / batch_size, 1))


for i in range(step):
    batch_mask = np.random.choice(train_size, batch_size)
    x_batch = x_train[batch_mask]
    t_batch = t_train[batch_mask]

    grad = network.gradient(x_batch, t_batch)

    for key in network.params:
        network.params[key] -= lr * grad[key]


    if i % per_epoch == 0:
        loss = network.loss(x_batch, t_batch)
        train_loss_list.append(loss)
        train_accuracy = network.accuracy(x_train, t_train)
        train_accuracy_list.append(train_accuracy)
        print(f'train loss: {loss}, train accuracy: {train_accuracy}')


x = np.arange(len(train_loss_list))
plt.plot(x, train_loss_list, label='train loss')
plt.xlabel('epoch')
plt.ylabel('loss')
plt.ylim(0, 3.0)
plt.legend(loc='center right')
plt.show()

x = np.arange(len(train_accuracy_list))
plt.plot(x, train_accuracy_list, label='train accuracy')
plt.xlabel('epoch')
plt.ylabel('accuracy')
plt.ylim(0, 1.0)
plt.legend(loc='center right')
plt.show()

