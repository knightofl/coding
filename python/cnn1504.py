import numpy as np
import matplotlib.pyplot as plt
import pickle
from tensorflow.keras.datasets.mnist import load_data


def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def sigmoid_gradient(x):
    return (1.0 - sigmoid(x)) * sigmoid(x)

def softmax(x):
    if x.ndim == 2:
        x = x.T
        x -= np.max(x, axis=0)
        y = np.exp(x) / np.sum(np.exp(x), axis=0)
        return y.T
    
    x -= np.max(x)
    return np.exp(x) / np.sum(np.exp(x))

def cross_entropy_error(y, t):
    if y.ndim == 1:
        y = y.reshape(1, y.size)
        t = t.reshape(1, t.size)

    if y.size == t.size:
        t = t.argmax(axis=1)

    batch_size = y.shape[0]
    return -np.sum(np.log(y[np.arange(batch_size), t] + 1e-7)) / batch_size


class TwoLayerNet:
    def __init__(self, input_size, hidden_size, output_size, weight_init_std=0.01):
        self.params = {}
        self.params['W1'] = weight_init_std * np.random.randn(input_size, hidden_size)
        self.params['b1'] = np.zeros(hidden_size)
        self.params['W2'] = weight_init_std * np.random.randn(hidden_size, output_size)
        self.params['b2'] = np.zeros(output_size)

    def predict(self, x):
        W1, W2 = self.params['W1'], self.params['W2']
        b1, b2 = self.params['b1'], self.params['b2']

        a1 = np.dot(x, W1) + b1
        z1 = sigmoid(a1)
        a2 = np.dot(z1, W2) + b2
        y = softmax(a2)

        return y

    def loss(self, x, t):
        y = self.predict(x)

        return cross_entropy_error(y, t)

    def accuracy(self, x, t):
        y = self.predict(x)
        y = np.argmax(y, axis=1)
        t = np.argmax(t, axis=1)

        accuracy = np.sum(y==t) / float(x.shape[0])
        return accuracy

    def gradient(self, x, t):
        W1, b1 = self.params['W1'], self.params['b1']
        W2, b2 = self.params['W2'], self.params['b2']

        grads = {}
        batch_size = x.shape[0]

        # forward
        a1 = np.dot(x, W1) + b1
        z1 = sigmoid(a1)
        a2 = np.dot(z1, W2) + b2
        y = softmax(a2)

        #backward
        dy = (y - t) / batch_size
        grads['W2'] = np.dot(z1.T, dy)
        grads['b2'] = np.sum(dy, axis=0)

        da1 = np.dot(dy, W2.T)
        dz1 = sigmoid_gradient(a1) * da1
        grads['W1'] = np.dot(x.T, dz1)
        grads['b1'] = np.sum(dz1, axis=0)

        return grads

        
(x_train, t_train), (x_test, t_test) = load_data()
x_train = x_train.reshape(-1, 28*28) / 255.0
t_train = np.eye(10)[t_train]
x_test = x_test.reshape(-1, 28*28) / 255.0
t_test = np.eye(10)[t_test]
print(x_train.shape, t_train.shape, x_test.shape, t_test.shape)

net = TwoLayerNet(input_size=784, hidden_size=50, output_size=10)

try:
    with open('./tmp/weight.pkl', 'rb') as f:
        net.params, train_accuracy_list, test_accuracy_list, train_loss_list = pickle.load(f)
except:
    train_loss_list = []
    train_accuracy_list = []
    test_accuracy_list =[]

train_size = x_train.shape[0]
batch_size = 100
step = 10000
lr = 0.1
per_epoch = max(train_size / batch_size, 1)


for i in range(step):
    batch_mask = np.random.choice(train_size, batch_size)
    x_batch = x_train[batch_mask]
    t_batch = t_train[batch_mask]

    grad = net.gradient(x_batch, t_batch)

    for key in ('W1', 'b1', 'W2', 'b2'):
        net.params[key] -= lr * grad[key]

    if i % per_epoch == 0:
        loss = net.loss(x_batch, t_batch)
        train_loss_list.append(loss)
        train_accuracy = net.accuracy(x_train, t_train)
        train_accuracy_list.append(train_accuracy)
        test_accuracy = net.accuracy(x_test, t_test)
        test_accuracy_list.append(test_accuracy)
        print(f'train accuracy: {train_accuracy:.2f}, test accuracy: {test_accuracy:.2f}, loss: {loss:.2f}')


with open('./tmp/weight.pkl', 'wb') as f:
    pickle.dump((net.params, train_accuracy_list, test_accuracy_list, train_loss_list), f)


x = np.arange(len(train_loss_list))
plt.plot(x, train_loss_list, label='train loss')
plt.xlabel('epoch')
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

