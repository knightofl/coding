import numpy as np
import sys
sys.path.append("./scratch1/")
from common.layers import *
from common.gradient import numerical_gradient
from collections import OrderedDict
from dataset.mnist import load_mnist

class TwoLayerNet:
    def __init__(self, input_size, hidden_size, output_size, weight_init=0.01):
        self.params = {}
        self.params['w1'] = weight_init * np.random.randn(input_size, hidden_size)
        self.params['b1'] = np.zeros(hidden_size)
        self.params['w2'] = weight_init * np.random.randn(hidden_size, output_size)
        self.params['b2'] = np.zeros(output_size)

        self.layers = OrderedDict()
        self.layers['affine1'] = Affine(self.params['w1'], self.params['b1'])
        self.layers['relu1'] = Relu()
        self.layers['affine2'] = Affine(self.params['w2'], self.params['b2'])
        self.lastlayer = SoftmaxWithLoss()

    def predict(self, x):
        for layer in self. layers.values():
            x = layer.forward(x)

        return x

    def loss(self, x, t):
        y = self.predict(x)
        return self.lastlayer.forward(y, t)
        
    def accuracy(self, x, t):
        y = self.predict(x)
        y = np.argmax(y, axis=1)

        if t.ndim != 1 : t = np.argmax(t, axis=1)

        accuracy = np.sum(y==t) / float(x.shape[0])
        return accuracy

    def numerical_gradient(self, x, t):
        loss_w = lambda w: self.loss(x, t)

        grads = {}
        grads['w1'] = numerical_gradient(loss_w, self.params['w1'])
        grads['b1'] = numerical_gradient(loss_w, self.params['b1'])
        grads['w2'] = numerical_gradient(loss_w, self.params['w2'])
        grads['b2'] = numerical_gradient(loss_w, self.params['b2'])
        
        return grads

    def gradient(self, x, t):
        self.loss(x, t)

        dout = 1
        dout = self.lastlayer.backward(dout)

        layers = list(self.layers.values())
        layers.reverse()
        for layer in layers:
            dout = layer.backward(dout)

        grads = {}
        grads['w1'] = self.layers['affine1'].dW
        grads['b1'] = self.layers['affine1'].db
        grads['w2'] = self.layers['affine2'].dW
        grads['b2'] = self.layers['affine2'].db

        return grads
 
(x_train, t_train), (x_test, t_test) = load_mnist(normalize=True, one_hot_label=True)
network = TwoLayerNet(input_size=784, hidden_size=50, output_size=10)
x_batch = x_train[:3]
t_batch = t_train[:3]

grad_numerical = network.numerical_gradient(x_batch, t_batch)
grad_backdrop = network.gradient(x_batch, t_batch)

for key in grad_numerical.keys():
    diff = np.average(np.abs(grad_backdrop[key] - grad_numerical[key]))
    print(f'key : {diff}')